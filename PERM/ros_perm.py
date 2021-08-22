#! /usr/local/bin/python3

from itertools import permutations
import sys

problem = "PERM"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: A positive integer n≤7.")
print(f"> **Return**: The total number of permutations of length n, followed by a list of all such permutations (in any order).")

data = sys.stdin.readline()
n = int(data.strip())
print(f"{n}")

alpha = [str(i) for i in range(1,n+1)]
print(alpha)
alphabet = ''.join(alpha)
print(alphabet)

ps = list(permutations(alphabet, n))

print(len(ps))
for p in ps:
    print(' '.join(p))
