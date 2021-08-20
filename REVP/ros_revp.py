#! /usr/local/bin/python3

from itertools import combinations
import sys

problem = "REVP"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A DNA string of length at most 1 kbp in FASTA format.")
print(f"> **Return**: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.")

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

## ========

def revc(string): 
    rev_data = string[::-1]
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

    return rev_comp_data

n = len(strings.values())
s = list(strings.values())[0].strip()
print(f"n = {n}")
print(f"{s}")
print(f"len: {len(s)}")
print(f"{revc(s)}")

for i, _ in enumerate(s):
    rem = len(s[i:])
    for l in range(min(12, rem),3,-1):
        spq = s[i:i+l]
        if len(spq) == l and spq == revc(spq):
            # print(i, l, spq)
            print(f"{i+1} {l}")
            break


## find all substrings and sort to start with longest

## check each substring against other sequences until one is found that is in each
