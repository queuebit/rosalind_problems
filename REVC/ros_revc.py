#! /usr/local/bin/python3

import sys

problem = "REVC"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A DNA string s of length at most 1000 bp.")
print(f"> **Return**: The reverse complement s^c of s.")

data = sys.stdin.readline()
print(f"")
print(f"String length: {len(data)}.")
print(f"{data}")

rev_data = data[::-1]
rev_comp_data = ""

for b in rev_data:
    bc = ""
    if b == "A":
        bc = "T"
    elif b == "T":
        bc = "A"
    elif b == "C":
        bc = "G"
    elif b == "G":
        bc = "C"
    rev_comp_data += bc

print(f"{rev_data}")
print(f"{rev_comp_data}")

