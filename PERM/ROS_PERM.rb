# !/usr/bin/env ruby

x = ARGV[0].to_i;

def factorial (n) 
	(1..n).inject {|s, n| s*n}
end

# See http://flori.github.com/permutation/

puts factorial x
show_perms x