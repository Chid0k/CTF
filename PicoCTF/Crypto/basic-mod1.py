a = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137 ,205 ,87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
b = [0] * 1000
for i in range(ord('A'),ord('Z') + 1):
      b[i-65] = i

for  x in a:
      i = x % 37
      if (i == 36):
            print('_', end = '')
      elif i in range(0,26):
            print(chr(b[i]), end = '')
      else:
            print(i-26, end = '')