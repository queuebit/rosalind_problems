#! /usr/local/bin/python3

from itertools import permutations
import sys

problem = "PROT"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).")
print(f"> **Return**: The protein string encoded by s.")

data = sys.stdin.readline()
s = data.strip()
print(f"{s}")

rna_codons = {
        'UUU': 'F',
        'CUU': 'L',
        'AUU': 'I',
        'GUU': 'V',
        'UUC': 'F',
        'CUC': 'L',
        'AUC': 'I',
        'GUC': 'V',
        'UUA': 'L',
        'CUA': 'L',
        'AUA': 'I',
        'GUA': 'V',
        'UUG': 'L',
        'CUG': 'L',
        'AUG': 'M',
        'GUG': 'V',
        'UCU': 'S',
        'CCU': 'P',
        'ACU': 'T',
        'GCU': 'A',
        'UCC': 'S',
        'CCC': 'P',
        'ACC': 'T',
        'GCC': 'A',
        'UCA': 'S',
        'CCA': 'P',
        'ACA': 'T',
        'GCA': 'A',
        'UCG': 'S',
        'CCG': 'P',
        'ACG': 'T',
        'GCG': 'A',
        'UAU': 'Y',
        'CAU': 'H',
        'AAU': 'N',
        'GAU': 'D',
        'UAC': 'Y',
        'CAC': 'H',
        'AAC': 'N',
        'GAC': 'D',
        'UAA': 'Stop',
        'CAA': 'Q',
        'AAA': 'K',
        'GAA': 'E',
        'UAG': 'Stop',
        'CAG': 'Q',
        'AAG': 'K',
        'GAG': 'E',
        'UGU': 'C',
        'CGU': 'R',
        'AGU': 'S',
        'GGU': 'G',
        'UGC': 'C',
        'CGC': 'R',
        'AGC': 'S',
        'GGC': 'G',
        'UGA': 'Stop',
        'CGA': 'R',
        'AGA': 'R',
        'GGA': 'G',
        'UGG': 'W',
        'CGG': 'R',
        'AGG': 'R',
        'GGG': 'G',
}

ps = ''
for i in range(int(len(s)/3)):
    codon = s[i*3:i*3+3]
    aa = rna_codons[codon]
    if aa != 'Stop':
        ps += aa
    else:
        break

print(ps)
