with open("./enc",encoding = 'utf-8') as f:
	s = f.read()
for i in range(0, len(s), 1):
	print(chr(ord(s[i]) >> 8), chr(ord(s[i]) - ((ord(s[i]) >> 8) << 8 )), end = '', sep = "")

print()
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# test
flag = "ab"
en = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
# (ord(flag[i]) << 8) + ord(flag[i + 1]) = ord (en)
print(chr(ord(en) >> 8))
print(ord(en) - ((ord(en) >> 8) << 8))
print((97 << 8) + 98) 