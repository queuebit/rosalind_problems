#! /usr/local/bin/python3

import sys

problem = "HAMM"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: Two DNA strings s and t of equal length (not exceeding 1 kbp).")
print(f"> **Return**: The Hamming distance dH(s,t).")

s, t = [l.strip() for l in sys.stdin.readlines()]
print(f"")
print(f"s: {s}")
print(f"t: {t}")

dh = 0

for i,n in enumerate(s):
    if s[i] != t[i]:
        dh += 1

print(dh)
