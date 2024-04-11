from Crypto.Util.number import *

p = 28151

for g in range(p):
      a = {}
      a = set(a)
      print(g,end=' ')
      for n in range(0,p + 1):
            a.add(pow(g,n,p))
      if len(a) == p or len(a) == p - 1 :
            print(g)
            print(len(a))
            break

