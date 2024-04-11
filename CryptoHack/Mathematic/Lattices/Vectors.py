import numpy as np
_v = [2, 6, 3]
v = np.array(_v)
_w = [1, 0, 0] 
w = np.array(_w)
_u = [7, 7, 2]
u = np.array(_u)
# calculate 3*(2*v - w) ∙ 2*u

print(np.dot((3*(2*v - w)) , (2 * u)))