#! /usr/local/bin/python3

import sys

problem = "FIB"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: Positive integers n≤40 and k≤5.")
print(f"> **Return**: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).")

data = sys.stdin.readline()

print(f"{data}")
n, k = [int(i) for i in data.strip().split(' ')]

print(f"n: {n}")
print(f"k: {k}")

fib = [1, 1]

for x in range(2,n):
    new_rab = fib[-1]
    ra_rab = fib[-2]
    pop_rab = new_rab + ra_rab*k
    print(f"After {x + 1} months there are population pairs of {pop_rab}")
    fib.append(pop_rab)

print(f"{fib[-1]}")

