import numpy as np

v = [np.zeros((1, 4))] * 5
v[1] = np.array([4,1,3,-1])
v[2] = np.array([2,1,-3,4])
v[3] = np.array([1,0,-2,7])
v[4] = np.array([6,2,9,-5])

u = [np.zeros((1, 4))] * 5 
u[1] = v[1]
print(v[2] - v[1] * 2.5)
for i in range(2,5):
    print(i)
    u[i] = v[i]
    for j in range(1,i):
        print(j, end = ' ')
        k = (float((np.dot(v[i], u[j]))) / (np.linalg.norm(u[j]) * np.linalg.norm(u[j])))
        u[i] = u[i] -  k * u[j]
    print(u[i])
    print()




