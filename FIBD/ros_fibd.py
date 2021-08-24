#! /usr/local/bin/python3

import sys

problem = "FIBD"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: Positive integers n≤100 and m≤20.")
print(f"> **Return**: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.")

data = sys.stdin.readline()

print(f"{data}")
n, m = [int(i) for i in data.strip().split(' ')]

print(f"n: {n}")
print(f"m: {m}")

fib = [1, 1, 2]

for x in range(3,n):
    # rab_a = fib[-3]
    # rab_b = fib[-2]
    # pop_rab = rab_a + rab_b
    # print(f"After {x + 1} months there are population pairs of {pop_rab}")
    # fib.append(pop_rab)
    ret_rab = 0
    rab_a = fib[-2]
    rab_b = fib[-1]
    if len(fib) > m:
        for i in range(1,m):
            print(i, -i, -(i+1))
            ret_rab += fib[-i] - fib[-(i+1)]

    pop_rab = rab_a + rab_b - ret_rab
    print(m, rab_a, rab_b, ret_rab)
    print(f"After {x+1} months there are population pairs of {pop_rab}")
    fib.append(pop_rab)

print(f"{fib[-1]}")
