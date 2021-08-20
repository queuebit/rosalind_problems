#! /usr/local/bin/python3

from itertools import combinations
import sys

problem = "LCSM"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.")
print(f"> **Return**: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)")

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

n = len(strings.values())
print(f"n = {n}")
print(strings.values())

## start with the shortest sequence
shortest = min(strings.values(), key=lambda s: len(s))
print(shortest)

## find all substrings and sort to start with longest
substrings = [shortest[x:y] for x, y in combinations(range(len(shortest)+1), r=2)]
print(substrings)
s_substrings = sorted(substrings, key=lambda s: -len(s))
print(s_substrings)

## check each substring against other sequences until one is found that is in each
for substring in s_substrings:
    for i, s in enumerate(strings.values()):
        if i < n - 1:
            if not substring in s:
                break
        elif i == n - 1 and substring in s:
            print(substring)
            sys.exit()
