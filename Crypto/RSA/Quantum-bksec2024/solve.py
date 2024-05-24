# nc 128.199.219.160 7031

def quantum(square):
    io.recvuntil(b"Enter your options: ")
    io.sendline(b"2")
    s = io.recvuntil(b"Make a guess, must be a square number:")
    io.sendline(str(square).encode('utf-8'))
    io.recvline()
    s = io.recvline().decode('utf-8')
    return int(s[:len(s) - 1])

from pwn import *
from Crypto.Util.number import *

io = process("python3", "server.py")
io.recvuntil(b"\n")
s = io.recvuntil(b")\n").decode('utf-8')

n = int(s[26:s.find("', '0x10001'")], 16)
e = 65537

io.recvuntil(b"Enter your options: ")
io.sendline(b"1")
s = io.recvline().decode('utf-8')
cipher = int(s[28:len(s) - 1], 16)

print(f"cipher = {cipher}")
print(f"n = {n}")
print()
print(quantum(0))

io.interactive()







