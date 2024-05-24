# p*u + q*v = gcd(u,v) = x
# p*u = x + (-v)*q
# p*u = x [q]


from math import gcd
p = 26513
q = 32321
# gcd(p, q) == 1
# u = x * pow(p, - 1) % q
u = pow(p, -1, q)
v = pow(q, -1, p)
v = (1 - p * u) / q
print(v)


