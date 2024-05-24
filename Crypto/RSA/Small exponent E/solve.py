from Crypto.Util.number import bytes_to_long, long_to_bytes
from gmpy2 import iroot
from pwn import *
import time
from math import gcd
import json


e = 5
flag = b'BKSEC'
io = remote("128.199.219.160", 7011)
accept = b"y"
io.recv()

X = 1
M = 1


a = [] # cipher
m = [] # module
C = 1
while len(a) < 5:
    kt = 1
    io.sendline(accept)
    kt = io.recvline()
    try:
        data = json.loads(kt)
        cip = int(data['requirement'], 16)
        n = int(data['key'][0], 16)
        check = 1
        for i in a:
            if (gcd(i, n) != 1):
                check = 0
                break
        if check == 1:
            a.append(cip)
            m.append(n)
            X = X * n
            C = C * cip
    except json.JSONDecodeError as e:
        continue
M = []
y = []
for i in range(len(m)):
    M.append(X // m[i])
for i in range(len(M)):
    y.append(pow(M[i], -1, m[i]))

Mess = 0
for i in range(len(M)):
    Mess = (Mess + a[i] * y[i] * M[i]) % X

m = int(iroot(Mess, 5)[0])
print(long_to_bytes(m))
    


    


    
    




