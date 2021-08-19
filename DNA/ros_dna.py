#! /usr/local/bin/python3

import sys

problem = "DNA"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A DNA string s of length at most 1000 nt.")
print(f"> **Return**: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.")

data = sys.stdin.readline()
print(f"")
print(f"String length: {len(data)}.")
print(f"{data}")
print(f"{data.count('A')} {data.count('C')} {data.count('G')} {data.count('T')}")

