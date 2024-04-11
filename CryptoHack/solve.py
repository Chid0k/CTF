from Crypto.Util.number import *

flag = long_to_bytes(int("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104", 16))
key = "myXORkey"
s = ""
for i in range(len(flag)):
	print(chr(flag[i] ^ ord(key[i % 8])), end = '' )
print(s)



