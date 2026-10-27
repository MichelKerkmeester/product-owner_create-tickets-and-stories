"""Redact a run folder in place before it is published.

The runners redact replies as they write them, but the raw event streams, the
transcripts, the manifest and each scenario's meta carry the test file's key, board
and asset links, plan names, plan keys and the account id as the tools returned them. This pass
covers every text file under the folder except the harness itself.

Usage: RUN_REDACT_FILE=<names file> RUN_FILE_KEY=<key> [RUN_EXTRA_KEYS=<keys file>]
       python3 run/redact_run.py <run folder>
       python3 run/redact_run.py <folder or file> [<folder or file> ...]
The names file holds one plan or team name per line and stays outside the repository.
The keys file holds the key of each new file a run made in drafts, the first word of a
line, and stays outside the repository too.
Names that are also the system's own public words belong out of that file.
A file path redacts that file alone, so a batch can redact one scenario's own output and
leave the older records in the same run folder as they are.
The substitutions are also importable (`settings`, `redact_text`), so the driver can redact
a log line the same way before it writes it.
"""
import os
import re
import sys

URL = re.compile(r"https?://(?:www\.)?figma\.com/[^\s\"'<>)\]\\]+")
USER_ID = re.compile(r'(\\*"user_id\\*":\s*\\*")\d+')
# A plan key names the team or organization the account belongs to, so it is redacted like a plan name
PLAN_KEY = re.compile(r"\b(team|organization)::\d+")


def settings():
    """The test file key, the draft keys and the numbered plan names the environment names."""
    key = os.environ.get("RUN_FILE_KEY", "")
    path = os.environ.get("RUN_REDACT_FILE", "")
    names = [n.strip() for n in open(path, encoding="utf-8") if n.strip()] if path else []
    extra_path = os.environ.get("RUN_EXTRA_KEYS", "")
    extra = [ln.split()[0] for ln in open(extra_path, encoding="utf-8") if ln.split()] if extra_path else []
    # Longest first, so a name that contains another is replaced whole.
    return key, extra, sorted(enumerate(names, 1), key=lambda x: -len(x[1]))


def redact_text(text, cfg):
    """The text with every substitution the folder pass applies to a file."""
    key, extra, order = cfg
    new = URL.sub("<figma-url>", text)
    if key:
        new = new.replace(key, "<test-file-key>")
    for k in extra:
        new = new.replace(k, "<draft-file-key>")
    for n, name in order:
        new = new.replace(name, f"<figma-plan-{n}>")
    new = USER_ID.sub(r"\g<1><user-id>", new)
    return PLAN_KEY.sub(r"\g<1>::<plan-id>", new)


def redact_file(p, cfg):
    """Rewrite one text file in place, and say whether it changed."""
    try:
        text = open(p, encoding="utf-8").read()
    except UnicodeDecodeError:
        return False
    new = redact_text(text, cfg)
    if new == text:
        return False
    open(p, "w", encoding="utf-8").write(new)
    return True


def main(paths):
    cfg = settings()
    changed = 0
    for path in paths:
        if os.path.isfile(path):
            # A named file is redacted alone, and the harness stays out of reach here too
            if os.path.basename(os.path.dirname(os.path.abspath(path))) != "run":
                changed += redact_file(path, cfg)
            continue
        for root, _, files in os.walk(path):
            if os.path.basename(root) == "run":
                continue
            for f in files:
                changed += redact_file(os.path.join(root, f), cfg)
    print(f"redacted {changed} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["."]))
