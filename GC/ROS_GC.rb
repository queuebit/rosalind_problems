# !/usr/bin/env ruby

input = ARGV[0];

class FASTA 
	attr_accessor :gc_content

	def initialize (fasta_id, sequence)
		@fasta_id = fasta_id;
		@sequence = sequence.to_s.split(/\s/).join; 
		@gc_content = (((@sequence.count('C').to_f + @sequence.count('G').to_f) / @sequence.length.to_f * 100) * 1000000).floor / 1000000.0;
	end

	def to_s 
		puts "Rosalind_#{@fasta_id}\n#{@gc_content}%"	
	end
end

fc = File.open(input, "r").read;
raw_seq = fc.split('>');
raw_seq.shift;

fasta_seqs = raw_seq.map { |fasta_pair| FASTA.new(/[0-9]{4}/.match(fasta_pair), /[ACTG\s]+/.match(fasta_pair))};

puts fasta_seqs.max_by { |s1| s1.gc_content};
