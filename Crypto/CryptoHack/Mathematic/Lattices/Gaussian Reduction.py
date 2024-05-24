import math
import numpy as np

v = np.array([846835985, 9834798552])
u = np.array([87502093, 123094980])

def det(k):
      return np.linalg.norm(k)


while True:
      if det(v) < det(u):
            h = u
            u = v
            v = h
      else:
            m = round(np.dot(u,v) / np.dot(u,u))
            if m == 0:
                  print(u, v)
                  break
            v = v - m * u
print(np.dot(u,v))
            

      