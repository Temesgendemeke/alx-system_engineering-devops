#!/usr/bin/env ruby
reg = ARGV[0].scan(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/).join(",")
puts reg