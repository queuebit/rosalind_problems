#! /usr/local/bin/python3

import re
import sys

problem = "SUBS"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: Two DNA strings s and t (each of length at most 1 kbp).")
print(f"> **Return**: All locations of t as a substring of s.")

data = sys.stdin.readlines()
print(f"")

s = data[0].strip()
t = data[1].strip()

print(f"s: {s}")
print(f"t: {t}")

### Doesn't include overlapping matches
# for m in re.finditer(t, s):
#     print(f"{m}")
#     print(f"{m.start() + 1}")

motif_locs = []

for i, _ in enumerate(s):
    if s[i:].startswith(t):
        motif_locs.append(str(i+1))

print(f"{' '.join(motif_locs)}")
