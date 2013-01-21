#!/usr/bin/env ruby

input = ARGV[0];

seqs = File.open(input,"r").readlines;

# Possibly change this to a class so I can reuse and to a better to_s
pro_a = Array.new(seqs[0].length-1) { |i| 0 };
pro_c = Array.new(seqs[0].length-1) { |i| 0 };
pro_g = Array.new(seqs[0].length-1) { |i| 0 };
pro_t = Array.new(seqs[0].length-1) { |i| 0 };

# Counts the bases within the sequences
seqs.map do |s|
	s = s.to_s;
	s.chomp! # removes \n char
	s = s.chars.to_a; # required in Ruby 1.8.7 not in Ruby 1.9
	(s.length).times  do |i|
		case s[i]
		when /A/ then pro_a[i]+=1;
		when /C/ then pro_c[i]+=1;
		when /G/ then pro_g[i]+=1;
		when /T/ then pro_t[i]+=1;
		end
	end
end


# Consensus string (might redo this within class with comparison)
c = "";
pro_a.length.times do |i|
	if pro_a[i] >= [pro_c[i], pro_g[i], pro_t[i]].max then
		c << "A"
	elsif pro_c[i] >= [pro_g[i], pro_t[i]].max then
		c << "C"
	elsif pro_g[i] >= pro_t[i] then
		c << "G"
	else
		c << "T"
	end
end

# Pretty print results
puts c;
print "A: "
print pro_a.map {|base| print base, " "}
puts
print "C: "
print pro_c.map {|base| print base, " "}
puts
print "G: "
print pro_g.map {|base| print base, " "}
puts
print "T: "
print pro_t.map {|base| print base, " "}
puts