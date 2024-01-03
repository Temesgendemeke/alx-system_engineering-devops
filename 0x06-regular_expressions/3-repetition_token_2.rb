#!/usr/bin/env ruby
reg = ARGV[0].scan(/hb[t]{1,}n/)

for i in reg
    print i
end
print "\n"