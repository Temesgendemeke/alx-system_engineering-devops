#!/usr/bin/env ruby
reg = ARGV[0].scan(/h[b]{0,1}tn/)

for i in reg
    print i
end
print "\n"