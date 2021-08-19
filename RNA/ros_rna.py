#! /usr/local/bin/python3

import sys

problem = "RNA"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A DNA string t having length at most 1000 nt.")
print(f"> **Return**: The transcribed RNA string of t.")

data = sys.stdin.readline()
print(f"")
print(f"String length: {len(data)}.")
print(f"{data}")
print(f"{data.replace('T','U')}")

