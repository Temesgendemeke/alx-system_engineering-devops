#!/usr/bin/env ruby
reg = ARGV[0].scan(/School*/i)

for i in reg
    print i
end
print "\n"