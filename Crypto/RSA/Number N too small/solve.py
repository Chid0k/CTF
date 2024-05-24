from Crypto.Util.number import bytes_to_long, long_to_bytes
c = 1094555114006097458981
e = 65537
n = 3367854845750390371489
p = 49450786403
q = 68105182763
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)

print("phi = ", long_to_bytes(m))

a = b"BKSEC{"
b = b"}"
M = (bytes_to_long(a) * pow(256,10) + bytes_to_long(b))
k = M % n
for i in range(1000):
    x = n* i + (m - k)
    if (x % 256 == 0):
        print(i, end = ' ')
        print(long_to_bytes(M + x))
    
