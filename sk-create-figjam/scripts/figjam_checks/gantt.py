#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: GANTT PROFILE
# ───────────────────────────────────────────────────────────────

"""A gantt chart, parsed here because the shared extractor refuses gantt.

The generator draws sections as lanes, tasks as bars and milestones as points.
It strips every colour and ignores the axis, weekend and marker settings, so a
model holding one of those would promise what the board never shows. Colour
and notes go on afterwards through the hybrid workflow.
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta

from .common import CAMEL_CASE_ID, content_lines, length_problems, raw_problems

MAX_TASKS = 12
MAX_PARALLEL = 5
SECTIONS_FROM = 8
FORMATS = {"YYYY-MM-DD": "%Y-%m-%d", "HH:mm": "%H:%M"}
TAGS = {"done", "active", "crit", "milestone"}
REFUSED_DIRECTIVES = {
    "classdef", "class", "style", "click", "call", "tickinterval", "axisformat", "excludes", "includes",
    "weekday", "weekend", "todaymarker", "displaymode", "inclusiveenddates", "topaxis",
}
DURATION = re.compile(r"^(\d+(?:\.\d+)?)(ms|[yMwdhms])$")
# Units read in minutes. A month and a year are approximate, which is enough to
# count how many bars overlap.
MINUTES = {"ms": 1 / 60000, "s": 1 / 60, "m": 1, "h": 60, "d": 1440, "w": 10080, "M": 43200, "y": 525600}
DATE_UNITS, TIME_UNITS = {"y", "M", "w", "d"}, {"h", "m", "s", "ms"}


def check_gantt(block_text: str) -> tuple[list[str], int, int]:
    """The problems with a gantt block, and how many tasks and sections it holds."""
    problems = raw_problems(block_text)
    lines = content_lines(block_text)
    if not lines or lines[0][1] != "gantt":
        return problems + ["a gantt chart starts with the line gantt"], 0, 0
    date_format, section, sections, tasks, ids = "", None, [], [], {}
    for number, text in lines[1:]:
        first = text.split()[0]
        if first.lower() in REFUSED_DIRECTIVES:
            problems.append(f"line {number}: {first} is stripped or ignored by the generator: drop it")
            continue
        if first == "title":
            continue
        if first == "dateFormat":
            date_format = text[len(first):].strip()
            if date_format not in FORMATS:
                problems.append(
                    f"line {number}: dateFormat {date_format}, write YYYY-MM-DD for dates or "
                    "HH:mm for one day"
                )
            continue
        if first == "section":
            section = text[len(first):].strip()
            sections.append(section)
            continue
        name, separator, meta = text.partition(":")
        if not separator:
            problems.append(f"line {number} is outside the gantt grammar the generator draws: {text!r}")
            continue
        if not date_format and not tasks:
            problems.append(f"line {number}: a task comes before dateFormat")
        task, found = parse_task(number, name.strip(), meta, date_format, ids)
        problems += found
        task["section"] = section
        tasks.append(task)
        if task["id"]:
            ids[task["id"]] = task
    if not date_format:
        problems.append("the chart has no dateFormat")
    if tasks and tasks[0]["after"]:
        problems.append(
            f"task {tasks[0]['name']} starts after another task: "
            "the first task needs a date to anchor the chart"
        )
    if len(tasks) > MAX_TASKS:
        problems.append(f"{len(tasks)} tasks, at most {MAX_TASKS}: split into phase charts")
    if len(tasks) > SECTIONS_FROM and len(sections) < 2:
        problems.append(
            f"{len(tasks)} tasks in {len(sections)} section(s): "
            f"group a chart over {SECTIONS_FROM} tasks into sections"
        )
    problems += overlap_problems(tasks, date_format)
    return problems, len(tasks), len(sections)


def parse_task(number: int, name: str, meta: str, date_format: str, ids: dict) -> tuple[dict, list[str]]:
    """One task line read into its name, id, tags, start and length, with the problems found on it."""
    problems = length_problems(f"line {number}: the task", name)
    parts = [part.strip() for part in meta.split(",") if part.strip()]
    tags = []
    while parts and parts[0].lower() in TAGS | {"vert"}:
        tags.append(parts.pop(0).lower())
    if "vert" in tags:
        problems.append(f"line {number}: the vert tag makes the generator skip the task")
    task = {"name": name, "id": "", "after": [], "start": None, "minutes": None, "tags": tags}
    if len(parts) == 3:
        task["id"] = parts.pop(0)
        if not CAMEL_CASE_ID.fullmatch(task["id"]):
            problems.append(f"line {number}: the task id {task['id']} is not camelCase")
        elif task["id"] in ids:
            problems.append(f"line {number}: the task id {task['id']} is used twice")
    if len(parts) != 2:
        return task, problems + [f"line {number}: a task is written name :tags, id, start, duration or end"]
    start, end = parts
    if start.startswith("after "):
        task["after"] = start.split()[1:]
        for reference in task["after"]:
            if reference not in ids:
                problems.append(f"line {number}: after {reference} names no task defined above it")
    elif date_format in FORMATS and not parses(start, date_format):
        problems.append(f"line {number}: the start {start} does not match dateFormat {date_format}")
    else:
        task["start"] = start
    duration = DURATION.match(end)
    if duration:
        amount, unit = float(duration.group(1)), duration.group(2)
        task["minutes"] = amount * MINUTES[unit]
        if date_format == "YYYY-MM-DD" and unit in TIME_UNITS:
            problems.append(f"line {number}: the duration {end} is in {'minutes' if unit == 'm' else 'a time unit'} "
                            "on a date chart: write M for months, d for days or w for weeks")
        if date_format == "HH:mm" and unit in DATE_UNITS:
            problems.append(f"line {number}: the duration {end} is a date unit on a one-day chart: write h or m")
        if "milestone" in tags and amount:
            problems.append(f"line {number}: the milestone {name} lasts {end}: a milestone has a zero duration")
    elif date_format in FORMATS and parses(end, date_format):
        task["end"] = end
    else:
        problems.append(
            f"line {number}: the end {end} is neither a duration such as 5d "
            f"nor a {date_format or 'dated'} end"
        )
    return task, problems


def parses(value: str, date_format: str) -> datetime | None:
    """The moment a value stands for under the chart's dateFormat, or None when it does not parse."""
    try:
        return datetime.strptime(value, FORMATS[date_format])
    except (KeyError, ValueError):
        return None


def overlap_problems(tasks: list[dict], date_format: str) -> list[str]:
    """Count how many bars share a moment in each section, which stack as parallel tracks on the board."""
    spans, previous_end = {}, None
    for task in tasks:
        if task["start"]:
            begin = parses(task["start"], date_format)
        elif task["after"]:
            ends = [spans.get(reference) for reference in task["after"]]
            begin = max(end[1] for end in ends) if ends and all(ends) else None
        else:
            begin = previous_end
        if begin is None:
            return []
        if task["minutes"] is not None:
            finish = begin + timedelta(minutes=task["minutes"])
        elif task.get("end"):
            finish = parses(task["end"], date_format)
        else:
            return []
        if task["id"]:
            spans[task["id"]] = (begin, finish)
        task["span"] = (begin, finish)
        previous_end = finish
    problems = []
    for section in dict.fromkeys(task["section"] for task in tasks):
        bars = [task["span"] for task in tasks if task["section"] == section and task["span"][1] > task["span"][0]]
        moments = sorted([(begin, 1) for begin, _ in bars] + [(finish, -1) for _, finish in bars])
        running = peak = 0
        for _, step in moments:
            running += step
            peak = max(peak, running)
        if peak > MAX_PARALLEL:
            problems.append(f"section {section or 'the first'} runs {peak} bars at once, at most {MAX_PARALLEL}: "
                            "split the section")
    return problems
