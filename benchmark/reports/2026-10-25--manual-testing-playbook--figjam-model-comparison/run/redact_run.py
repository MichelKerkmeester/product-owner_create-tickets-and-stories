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
A key a tool call or a response names in a `file_key` or `fileKey` field is redacted in every file
of the batch as well, so a file a run creates for itself never needs a keys file entry.
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
# A file the run creates for itself has a key no keys file can name ahead of time, so the key is read off
# the tool call or the response that carries it, escaped or not, and every copy of it is redacted.
KEY_FIELD = re.compile(r'\\*"(?:file_key|fileKey)\\*"\s*:\s*\\*"([A-Za-z0-9]{15,})')


def settings():
    """The test file key, the draft keys and the numbered plan names the environment names."""
    key = os.environ.get("RUN_FILE_KEY", "")
    path = os.environ.get("RUN_REDACT_FILE", "")
    names = [n.strip() for n in open(path, encoding="utf-8") if n.strip()] if path else []
    extra_path = os.environ.get("RUN_EXTRA_KEYS", "")
    extra = [ln.split()[0] for ln in open(extra_path, encoding="utf-8") if ln.split()] if extra_path else []
    # Longest first, so a name that contains another is replaced whole.
    return key, extra, sorted(enumerate(names, 1), key=lambda x: -len(x[1]))


def found_keys(text):
    """The file keys a tool call or a response in the text names."""
    return set(KEY_FIELD.findall(text))


def redact_text(text, cfg):
    """The text with every substitution the folder pass applies to a file."""
    key, extra, order = cfg
    extra = list(extra) + sorted(found_keys(text) - {key} - set(extra))
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


def texts(paths):
    """Every text file the paths name, a folder walked without its harness."""
    for path in paths:
        if os.path.isfile(path):
            if os.path.basename(os.path.dirname(os.path.abspath(path))) != "run":
                yield path
            continue
        for root, _, files in os.walk(path):
            if os.path.basename(root) != "run":
                yield from (os.path.join(root, f) for f in files)


def main(paths):
    cfg = settings()
    # A key one file names, such as a new file's key in the call that made it, is redacted in every file of
    # the batch, since a reply or a transcript may carry it with no field around it.
    seen = set()
    for p in texts(paths):
        try:
            seen |= found_keys(open(p, encoding="utf-8").read())
        except UnicodeDecodeError:
            pass
    key, extra, order = cfg
    cfg = (key, list(extra) + sorted(seen - {key} - set(extra)), order)
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
