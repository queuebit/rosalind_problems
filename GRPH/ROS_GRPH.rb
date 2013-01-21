# !/usr/bin/env ruby

input = ARGV[0];

class FASTA 
	attr_accessor :pref, :suff, :fasta_id

	def initialize (fasta_id, sequence)
		@fasta_id = fasta_id;
		@sequence = sequence.to_s.split(/\s/).join;
		@pref = @sequence[0..2];
		@suff = @sequence[-3,3];
	end

	def to_s 
		puts "Rosalind_#{@fasta_id}"	
	end

	def edge_match (seq2)
		@suff === seq2.pref
	end

end

fc = File.open(input, "r").read;
raw_seq = fc.split('>');
raw_seq.shift;

fasta_seqs = raw_seq.map { |fasta_pair| FASTA.new(/[0-9]{4}/.match(fasta_pair), /[ACTG\s]+/.match(fasta_pair))};

num_fas = fasta_seqs.length

num_fas.times do |i|
	num_fas.times do |j|
		s1 = fasta_seqs[i]
		s2 = fasta_seqs[j]
		if ((not i == j) and s1.edge_match(s2)) then
			print "Rosalind_", s1.fasta_id,  " Rosalind_", s2.fasta_id, "\n"
		end
	end
end