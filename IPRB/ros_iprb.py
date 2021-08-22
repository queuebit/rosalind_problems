#! /usr/local/bin/python3

import sys

problem = "IPRB"
print(f"This is the {problem}")
print(f"Detailed instructions can be found here: http://rosalind.info/problems/{problem.lower()}/")

print(f"> **Given**: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.")
print(f"> **Return**: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.")

k, m, n = [int(i) for i in sys.stdin.readline().strip().split(' ')]
print(f"{k} {m} {n}")

pop = k + m + n

prob_AA_Aa = (k / pop * 
	((k-1)/(pop-1)*1 + m/(pop-1)*1 + n/(pop-1)*1) +
	m / pop *
	(k/(pop-1)*1 + (m-1)/(pop-1)*0.75 + n/(pop-1)*0.5) +
	n / pop *
	(k/(pop-1)*1 + m/(pop-1)*0.5 + (n-1)/(pop-1)*0));

print(prob_AA_Aa)

