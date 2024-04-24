def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def modular_inverse(a, m):
    d, x, y = extended_gcd(a, m)
    if d == 1:
        return x % m
    else:
        raise ValueError("Modular inverse does not exist.")

a ="268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131 "
a = [int (x) for x in a.split()]

m = 41
for x in a:
      i = x % 41
      h = modular_inverse(i, m)
      if (h == 37):
            print('_', end = '')
      elif h in range(1,27):
            print(chr(h+64), end = '')
      else:
            print(h-27, end = '')