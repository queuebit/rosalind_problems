#! /usr/local/bin/python3

import sys

problem = "GRPH"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A collection of DNA strings in FASTA format having total length at most 10 kbp.")
print(f"> **Return**: The adjacency list corresponding to O3. You may return edges in any order.")

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

for k in strings:
    v = strings[k]
    for ko in strings:
        vo = strings[ko]
        if k == ko:
            continue

        if v[-3:] == vo[0:3]:
            print(f"{k} {ko}")
