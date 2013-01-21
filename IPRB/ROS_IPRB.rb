# !/usr/bin/env ruby

k, m, n = ARGV[0..2];

pos_outcomes = 0;
total_outcomes = 0;

k = k.to_f;
m = m.to_f;
n = n.to_f;

pop = k+m+n

prob_AA_Aa = 
	# k chosen first 
	(k / pop * 
	((k-1)/(pop-1)*1 + m/(pop-1)*1 + n/(pop-1)*1) +
	# m chosen first
	m / pop *
	(k/(pop-1)*1 + (m-1)/(pop-1)*0.75 + n/(pop-1)*0.5) +
	# n chosen first
	n / pop *
	(k/(pop-1)*1 + m/(pop-1)*0.5 + (n-1)/(pop-1)*0));

puts (prob_AA_Aa*100000).floor/100000.0