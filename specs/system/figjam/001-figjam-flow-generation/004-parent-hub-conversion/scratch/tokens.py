import sys, tiktoken, pathlib
enc=tiktoken.get_encoding("o200k_base")
root=pathlib.Path(sys.argv[1]); files=sys.argv[2:]
tot=0
for f in files:
    p=root/f
    if p.exists():
        n=len(enc.encode(p.read_text())); tot+=n; print(f"{n:6d} {f}")
    else: print("   --- missing", f)
print(f"{tot:6d} TOTAL")
