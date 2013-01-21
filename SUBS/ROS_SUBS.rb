#!usr/bin/env ruby

input = ARGV[0];

s, t = File.open(input, "r").readlines;

s.chomp!;
t.chomp!;

match_loc = 0;

while s.index(t,match_loc)
	match_loc = s.index(t,match_loc) + 1;
	print match_loc;
	print ' ';
end

puts '';