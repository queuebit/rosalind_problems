#!/usr/bin/env ruby

input = ARGV[0];
seq1, seq2 = File.open(input, "r").readlines;

hamming_dist = 0;

seq1.length.times {|i| hamming_dist+=1 unless (seq1[i] == seq2[i])}

puts hamming_dist;
