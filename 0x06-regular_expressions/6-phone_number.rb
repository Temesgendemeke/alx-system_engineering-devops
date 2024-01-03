#!/usr/bin/env ruby
reg = ARGV[0].scan(/^\d{10}$/)

for i in reg
    print i
end
print "\n"