a = 97
b = 22

c = [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]

text_key = "trudeau"

p = 97
g = 31

# u = g ^ a % p
# v = g ^ b % p

# key = v ^ a % p
# b_key = u ^ b % p

share_key = pow(g, a * b, p)

# semi_cipher = {palin_text, text_key}
cipher = ""
for x in c:
    cipher = cipher + chr((x // 311) // share_key)
    
# dy_e {plaintext, text_key} string;string
# key_len = 7
# key_char = char in t_k
# en_cry  = 

s = ""
for i in range(len(cipher)):
    key = text_key[i % 7]
    char = chr(ord(cipher[i]) ^ ord(key))
    s = char + s
print(s)
    

