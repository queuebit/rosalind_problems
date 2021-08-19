#! /usr/local/bin/python3

import sys

problem = "GC"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).")
print(f"> **Return**: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.")

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

strings_gc = {}
for k,v in strings.items():
    print(k, v)
    gc_content = (v.count('C') + v.count('G')) / len(v)
    strings_gc[k] = gc_content * 100.0

print(f"DNA Strings: {len(data) / 2}.")
print(f"{strings}")
print(f"{strings_gc}")

highest_gc_string = max(strings_gc, key=strings_gc.get)
highest_gc_content = max(strings_gc.values())
print(f"{highest_gc_string}")
print(f"{highest_gc_content}")
