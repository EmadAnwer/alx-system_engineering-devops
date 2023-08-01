#!/usr/bin/env ruby
argument = ARGV[0]
sender = argument.match(/\[from:([^\]]+)\]/)&.captures&.first
receiver = argument.match(/\[to:([^\]]+)\]/)&.captures&.first
flags = argument.match(/\[flags:([^\]]+)\]/)&.captures&.first

puts "#{sender},#{receiver},#{flags}"
