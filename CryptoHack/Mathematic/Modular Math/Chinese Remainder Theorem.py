"""
      x ≡ 2 mod 5
      x ≡ 3 mod 11
      x ≡ 5 mod 17
"""
m = [5, 11, 17]
M = 935
a = [2, 3, 5]
x = 0
for i in range(3):
      x += a[i] * pow((M // m[i]),-1,m[i]) * (M // m[i])
print(x % M)

