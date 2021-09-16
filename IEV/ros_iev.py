#! /usr/local/bin/python3

import sys

problem = "IEV"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"""> **Given**: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa""")
print(f"> **Return**: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.")

data = sys.stdin.readline()

print(f"{data}")
nAAAA, nAAAa, nAAaa, nAaAa, nAaaa, naaaa = [int(i) for i in data.strip().split(' ')]

print(f"1. AA-AA: {nAAAA}")
print(f"2. AA-Aa: {nAAAa}")
print(f"3. AA-aa: {nAAaa}")
print(f"4. Aa-Aa: {nAaAa}")
print(f"5. Aa-aa: {nAaaa}")
print(f"6. aa-aa: {naaaa}")

print(f"")
