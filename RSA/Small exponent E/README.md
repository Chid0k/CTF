# What is RSA ???



# RSA - Small public exponent e

Trong trường hợp số mũ công khai [n, e] có n lớn và số mũ e nhỏ: 1, 2, 3, 5, ...
## [+] Nếu e = 1:
```shell c = m ^ 1 % n```

Điều kiện cần: m < n

Solve: m = c
## [+] Nếu e = 2, 3, 5, ...
``` c = m ^ e % n ```

Điều kiện cần: m ^ e > n

(Trong trường hợp m ^ e < n ---> Đưa về giải c = m ^ e)

## Idea ##

Do số mũ e nhỏ và có thể lấy nhiều bộ [N, c] từ challenge. Ta sử dụng tính chất cuả đồng dư Trung hoa (Chinese Remainder Theorem) để tìm m ^ e.

Đồng dư Trung hoa có gì:

Giả sử ta có hệ phương trình như sau:
* x ≡ a1 [m1]
* x ≡ a2 [m2]
* 
* x ≡ ak [mk]

Và:
    ```Ciphertext = mess ^ e % N```

Trong đó '**mi**' có vai trò như '**N**' trong khóa công khai, '**ai**' có vai trò như '**(C) Ciphertext**'

_==> Công việc chúng ta là đi tìm '**X**' hay là '**mess ^ e**'_

***Điều kiện cần có***: Các cặp số '**mi**' phải đôi một nguyên tố cùng nhau: ```gcd(m[i], m[j]) == 1```

## Solve ##

Tính toán các hằng số cần thiết để giải hệ phương trình Đồng dư
* M = m1 * m2 * m3 * ... 
* Mi = M // mi (i = 1, 2, 3, ...)
* Hằng số '**yi**' là nghịch đảo modulo của '**Mi**' trong modulo '**mi**'.
```Mi * yi ≡ 1 [mi]```
* Tính toán giá trị của ```X = sum(ai * Mi * yi) % M```
**_Giá trị của X tìm được là giá trị của mess ^ e_**

# Simple challenge

**BKSEC training 2024**
## Preview 

* nc 128.199.219.160 7011
* Output:
```
Welcome to Hanxin's Military Camp. Would you like to enroll? (y/n) 
y
{"requirement": "A2DFA420C1F5BB78B0C9E2DEAB213E8545A3084C0594E3AD5CEB4A4EBE4896390C83FD614A68CAFB00B46BEC1A970CBE76032E36188E2828FE1BEE0C5F0FDCBE410A80D720CDF856B8756493B120B5AC7A886DACA71012D44086A75FCC1393880186F2B00C3F520447199328E74D6DDB6760E5302B0AD0AEE84A4A5553FE3713", "key": ["D343959DAF0365ABA5A275B47BE34F319FFD93C3FDA4B6C25D11DE745CA19FA27A6BB906C2EFD7A998C48F1FF41E6A1DC57808818D4556897D92BE85F4F6791A2AFADA334753AF02D2B44BA769E8945593AD00A902F1F5EB0FCD46DA2A33003C9EAD82094664314796CB4035821EF72DE7A58D997E7E5BE5583D54AB4157C4F7", "5"]}
```
## Code solve 
```
from Crypto.Util.number import bytes_to_long, long_to_bytes
from gmpy2 import iroot
from pwn import *
import time
from math import gcd
import json


io = remote("128.199.219.160", 7011) # mở kết nối tới server chall
accept = b"y"
io.recv()

e = 5
X = 1
M = 1
a = [] # cipher
m = [] # module
C = 1
while len(a) < e:
    kt = 1
    io.sendline(accept)
    kt = io.recvline()
    try:
        data = json.loads(kt)

        # Lấy các cặp khóa công khai, và cipher text [N, c]
        cip = int(data['requirement'], 16)
        n = int(data['key'][0], 16)
        check = 1
        for i in a:
            if (gcd(i, n) != 1): # Kiểm tra các bộ (mi, mj) nguyên tố cùng nhau
                check = 0
                break
        if check == 1:
            a.append(cip)
            m.append(n)
            X = X * n   # tính toán M
            C = C * cip
    except json.JSONDecodeError as e:
        continue
M = [] 
y = []
for i in range(len(m)):
    M.append(X // m[i]) # M[i] là các giá trị riêng của M
for i in range(len(M)):
    y.append(pow(M[i], -1, m[i]))   # Mảng y[] gồm các giá trị y[i]

Mess = 0
for i in range(len(M)):
    Mess = (Mess + a[i] * y[i] * M[i]) % X

e = 5
m = int(iroot(Mess, e)[0]) # lấy căn bậc e của Mess
print(long_to_bytes(m))
```
*Chú ý:*

* **Hàm iroot(a, k) trả về [Phần nguyên căn bậc k của a, True-False]**

* **True: tồn tại căn bậc k của a False ngược lại**
## Flag ##
**_GOOD LUCK_**
