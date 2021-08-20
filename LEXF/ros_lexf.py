#! /usr/local/bin/python3

from itertools import product
import sys

problem = "LEXF"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).")
print(f"> **Return**: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).")

data = sys.stdin.readlines()
print(f"")

strings = {}
label = None
string = None

bet, n = [d.strip() for d in data]
print(bet, n)

chars = bet.replace(' ','')

for s in product(chars, repeat=int(n)):
    print(f"{''.join(s)}")
