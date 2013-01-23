# !/usr/bin/env ruby

input = ARGV[0];

dna_strings = File.open(input,"r").readlines.map {|s| s.chomp!}

# http://en.wikibooks.org/wiki/Algorithm_implementation/Strings/Longest_common_substring#Ruby
# TODO: I need to modify this function to return an array of substrings instead
def find_longest_common_substring(s1, s2)
    if (s1 == "" || s2 == "")
      return ""
    end
    m = Array.new(s1.length){ [0] * s2.length }
    n = []
    longest_length, longest_end_pos = 0,0
    (0 .. s1.length - 1).each do |x|
      (0 .. s2.length - 1).each do |y|
        if s1[x] == s2[y]
          m[x][y] = 1
          if (x > 0 && y > 0)
            m[x][y] += m[x-1][y-1]
          end
          if m[x][y] > longest_length
            n << s1[longest_end_pos - longest_length + 1 .. longest_end_pos]
            longest_length = m[x][y]
            longest_end_pos = x
          elsif m[x][y] == longest_length
            n << s1[longest_end_pos - longest_length + 1 .. longest_end_pos]
          end
        end
      end
    end
    puts n
    return s1[longest_end_pos - longest_length + 1 .. longest_end_pos]
end

(dna_strings.length-1).times do |i|
	 find_longest_common_substring(dna_strings[i], dna_strings[i+1])
end