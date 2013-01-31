# !/usr/bin/env ruby

x = ARGV[0].to_i;

def factorial (n) 
	(1..n).inject {|s, n| s*n}
end

# Also see http://flori.github.com/permutation/
def perm_sets (n)
  ps = (1..n).to_a.permutation.to_a
  ps.each {|a| print a.join(' '); puts;};
end

puts factorial x
perm_sets x