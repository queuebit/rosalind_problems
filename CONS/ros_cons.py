#! /usr/local/bin/python3

import sys

problem = "ROS"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.")
print(f"> **Return**: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)")

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

print(strings.values())
zi = zip(*strings.values())

pa = []
pc = []
pg = []
pt = []

for jt in zi:
    j = ''.join(jt)
    pa.append(str(j.count('A')))
    pc.append(str(j.count('C')))
    pg.append(str(j.count('G')))
    pt.append(str(j.count('T')))

common_count = list(zip(pa, pc, pg, pt))
common_anc = []
print(common_count)
for it in common_count:
    max_i = max(it)
    max_il = it.index(max_i)
    if max_il == 0:
        common_anc.append('A')
    elif max_il == 1:
        common_anc.append('C')
    elif max_il == 2:
        common_anc.append('G')
    elif max_il == 3:
        common_anc.append('T')

print(f"{''.join(common_anc)}")
print(f"A: {' '.join(pa)}")
print(f"C: {' '.join(pc)}")
print(f"G: {' '.join(pg)}")
print(f"T: {' '.join(pt)}")
