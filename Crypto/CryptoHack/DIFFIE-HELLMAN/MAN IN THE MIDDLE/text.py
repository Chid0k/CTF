import math

def discrete_log(g, S, p):
    m = int(math.ceil(math.sqrt(p-1)))
    baby_steps = {pow(g, i, p): i for i in range(m)}
    
    # Tính tất cả giá trị giant-step g^(-m*j) mod p
    inv_g_m = pow(pow(g, m, p), -1, p)
    giant_step = S
    for j in range(m):
        if giant_step in baby_steps:
            return j*m + baby_steps[giant_step]
        giant_step = (giant_step * inv_g_m) % p
    
    # Nếu không tìm thấy giá trị b, trả về None
    return None

a = 12345  
p = 7919   
g = 2      
S = 617    

# Tính giá trị b của B
a_inv = pow(a, -1, p-1)
b = (a_inv * discrete_log(g, S, p)) % (p-1)

print("Giá trị b của B là:", b)