p = 29
ints = [14, 6, 11]
Fp = []
Fp = set(Fp)
for a in range(1,29):
      x = pow(a,2,p)
      print(x,a)
      
      

      


for x in range(29):
      t = pow(x,2,p)
      if t in ints:
            print(x)