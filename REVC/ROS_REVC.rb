#!/usr/bin/env ruby

input = ARGV[0];

puts input.tr('ACTG','TGAC').reverse;