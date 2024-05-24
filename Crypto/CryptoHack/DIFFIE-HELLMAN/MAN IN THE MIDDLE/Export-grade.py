p = "0xde26ab651b92a129"
g = "0x2"
A = "0x577a071213351f75"
B = "0xce1d04eb69e83a37"
iv = "32efc33dc0028e2f0422081fbd9c5c9f" 
encrypted_flag = "7107a004906fea9fa19aa0678ac045709bb161467f8bda68eddd9a03577fc980"

p = int(p,16)
g = int(g,16)
A = int(A,16)
B = int(B,16)
b = 722750595082907244 ## link
print(pow(A,b,p))

print(A,B,p,g)