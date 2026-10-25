"""Redact a run folder in place before it is published.

The runners redact replies as they write them, but the raw event streams, the
transcripts, the manifest and each scenario's meta carry the test file's key, board
and asset links, plan names and the account id as the tools returned them. This pass
covers every text file under the folder except the harness itself.

Usage: RUN_REDACT_FILE=<names file> RUN_FILE_KEY=<key> python3 run/redact_run.py <run folder>
The names file holds one plan or team name per line and stays outside the repository.
Names that are also the system's own public words belong out of that file.
"""
import os
import re
import sys

URL = re.compile(r"https?://(?:www\.)?figma\.com/[^\s\"'<>)\]\\]+")
USER_ID = re.compile(r'(\\*"user_id\\*":\s*\\*")\d+')


def main(folder):
    key = os.environ.get("RUN_FILE_KEY", "")
    path = os.environ.get("RUN_REDACT_FILE", "")
    names = [n.strip() for n in open(path, encoding="utf-8") if n.strip()] if path else []
    # Longest first, so a name that contains another is replaced whole.
    order = sorted(enumerate(names, 1), key=lambda x: -len(x[1]))
    changed = 0
    for root, _, files in os.walk(folder):
        if os.path.basename(root) == "run":
            continue
        for f in files:
            p = os.path.join(root, f)
            try:
                text = open(p, encoding="utf-8").read()
            except UnicodeDecodeError:
                continue
            new = URL.sub("<figma-url>", text)
            if key:
                new = new.replace(key, "<test-file-key>")
            for n, name in order:
                new = new.replace(name, f"<figma-plan-{n}>")
            new = USER_ID.sub(r"\g<1><user-id>", new)
            if new != text:
                open(p, "w", encoding="utf-8").write(new)
                changed += 1
    print(f"redacted {changed} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
