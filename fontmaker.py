#!/usr/bin/env python

# generated font image with:
# ttf2png -s18 -c32 -r0,127 -l128 -v -t pixel\ font-7.ttf

import sys
import png

file = sys.argv[1]

parser = png.Reader(file)

data = parser.read()
pxls = list(data[2])

print "/* #### FONT0 #### */"
print "reg [11:0] font0 [1709:0];"
print "\ninitial begin"
k = 0
for i in xrange(32,127):
    for y in xrange(18):
        sys.stdout.write("font0[" + str(k) + "] = 12'b")
        k=k+1
        for x0 in xrange(10,22):
            x = (i<<6) + (x0<<1) + 1 
            sys.stdout.write('0' if (pxls[y][x] < 16) else '1')
        print(";")
print "end"
print "/* #### END FONT0 #### */"
