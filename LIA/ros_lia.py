#! /usr/local/bin/python3

import sys

problem = "LIA"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.") 
print(f"> **Return**: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.")

data = sys.stdin.readline()

print(f"{data}")
k, n = [int(i) for i in data.strip().split(' ')]

print(f"k = {k}")
print(f"N = {n}")

print(f"")

#  |  A |  a
#---------
# A| AA | Aa
#---------
# a| aA | aa 

#  |  B |  b
#---------
# B| BB | Bb
#---------
# b| bB | bb 

p = 2

pAA = 1 / 4
pAa = 2 / 4
paa = 1 / 4

pBB = 1 / 4
pBb = 2 / 4
pbb = 1 / 4

pAABB = pAA * pBB
pAABb = pAA * pBb
pAAbb = pAA * pbb

pAaBB = pAa * pBB
pAaBb = pAa * pBb
pAabb = pAa * pbb

paaBB = paa * pBB
paaBb = paa * pBb
paabb = paa * pbb

pPop = [pAABB, pAABb, pAAbb, pAaBB, pAaBb, pAabb, paaBB, paaBb, paabb]
print(pPop)
print(sum(pPop))

#  |  A |  a
#---------
# A| AA | Aa
#---------
# A| AA | Aa 

#  |  A |  a
#---------
# a| aA | aa
#---------
# a| aA | aa 

#  |  B |  b
#---------
# B| BB | Bb
#---------
# B| BB | Bb 

#  |  B |  b
#---------
# b| bB | bb
#---------
# b| bB | bb 

g2AA_pAa = 1 / 4
g2aa_pAa = 2 / 4

g2BB_pBb = 1 / 4
g2bb_pBb = 2 / 4

g2_AABB_pHetero = g2AA_pAa * g2BB_pBb
g2_AABb_pHetero = g2AA_pAa * pBb
g2_AAbb_pHetero = g2AA_pAa * g2bb_pBb

g2_AaBB_pHetero = pAa * g2BB_pBb
g2_AaBb_pHetero = pAa * pBb
g2_Aabb_pHetero = pAa * g2bb_pBb

g2_aaBB_pHetero = g2aa_pAa * g2BB_pBb
g2_aaBb_pHetero = g2aa_pAa * pBb
g2_aabb_pHetero = g2aa_pAa * g2bb_pBb

g2_pPopHetero = [g2_AABB_pHetero, g2_AABb_pHetero, g2_AAbb_pHetero,
        g2_AaBB_pHetero, g2_AaBb_pHetero, g2_Aabb_pHetero,
        g2_aaBB_pHetero, g2_aaBb_pHetero, g2_aabb_pHetero]

#a = [1, 2, 3]
#b = [2, 3, 4]
#print(a, b, list(map(lambda x,y:x*y,a,b)), a * p, b * p)
