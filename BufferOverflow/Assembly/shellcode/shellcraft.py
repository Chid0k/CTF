from pwn import *

context.arch = 'amd64'
context.os = 'linux'

shellcode = shellcraft.amd64.linux.cat('/bin/flag.txt')

print(shellcode)