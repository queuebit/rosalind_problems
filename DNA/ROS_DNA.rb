#!/usr/bin/env ruby

input = ARGV[0];

a = input.count('A');
c = input.count('C');
g = input.count('G');
t = input.count('T');

puts "#{a} #{c} #{g} #{t}";