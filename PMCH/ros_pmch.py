#! /usr/local/bin/python3

from math import factorial
import sys

problem = "PMCH"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.")
print(f"> **Return**: The total possible number of perfect matchings of basepair edges in the bonding graph of s.")

data = sys.stdin.readlines()
print(f"")

strings = {}
label = None
string = None

for line in data:
    if line.startswith(">"):
        label = line[1:].strip()
        print(label)
    elif label:
        if strings.get(label):
            strings[label] += line.strip()
        else:
            strings[label] = line.strip()
    else:
        print("ERROR: no label")

s = list(strings.values())[0]
print(f"{s}")

a = s.count('A')
g = s.count('G')

print(f"{factorial(a)*factorial(g)}")
