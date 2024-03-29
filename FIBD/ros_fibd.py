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
#pop = [[0], [1], [0, 2]]
last_pop = [0,2]
pop_crit = [[1,0,0], [0,1,0], [1,1,0]]
print(pop_crit)

for x in range(3,n):
    ### A
    # rab_a = fib[-3]
    # rab_b = fib[-2]
    # pop_rab = rab_a + rab_b
    # print(f"After {x + 1} months there are population pairs of {pop_rab}")
    # fib.append(pop_rab)

    ### B
    # ret_rab = 0
    # rab_a = fib[-2]
    # rab_b = fib[-1]
    # if len(fib) > m:
    #    for i in range(1,m):
    #        print(i, -i, -(i+1))
    #        ret_rab += fib[-i] - fib[-(i+1)]

    #prev_month = pop[-1]
    this_month = []

    #for r in last_pop:
    #    if r == 0:
    #        this_month.append(1)
    #    elif r == m - 1:
    #        this_month.append(0)
    #    else:
    #        this_month.append(0)
    #        this_month.append(r+1)
    ln, lm, lr = pop_crit[-1]
    math = ln + lm*2 - lr
    tn = lm
    tm = ln + lm - lr
    tr = pop_crit[-(m-1)][0] if len(pop_crit) >= (m - 1) else 0
    pop_crit.append([tn, tm, tr])

    #pop.append(this_month)
    last_pop = this_month

    #print(f"prev month MON:{x} rabbits: {len(prev_month)} -- {prev_month}")
    #print(f"MON:{x+1} | NEW: {this_month.count(0)} | MATURE: {len(this_month) - this_month.count(0)} | RETIRING: {this_month.count(m - 1)} [rabbits]: {len(this_month)} -- {this_month}")
    #fib.append(len(this_month))
    #print(f"MATH: {math} crit: {pop_crit[-1]}")
    fib.append(math)

    #pop_rab = rab_a + rab_b - ret_rab
    #print(m, rab_a, rab_b, ret_rab)
    #print(f"After {x+1} months there are population pairs of {pop_rab}")
    #fib.append(pop_rab)

print(f"{fib[-1]}")
