#! /usr/local/bin/python3

from itertools import product
import sys

problem = "LEXP"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).")
print(f"> **Return**: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)")

data = sys.stdin.readlines()
print(f"")

strings = {}
label = None
string = None

bet, n = [d.strip() for d in data]
n = int(n)
print(bet, n)

chars = bet.replace(' ','')
#chars = bet.split(' ')

a_set = []
for x in range(1, n + 1):
    for s in product(chars, repeat=x):
        a_set.append(''.join(s))

def lex_val(a):
    lv=0
    az = str(a).ljust(n, '0')
    an = 0
    for i,c in enumerate(az):
        if c != "0":
            lv = (chars.index(c) + 1)*10**(n-i)
            an += lv
    return an

#print(a_set)
a_sort = sorted(a_set, key=lex_val)
for si in a_sort:
    print(si)
