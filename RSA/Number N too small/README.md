# What is RSA ???

# RSA - Number N is too small

## Preview
Giả sử trong cặp khóa công khai [n, e] có khóa n nhỏ và số mũ e lớn. Mess được mã hóa ```c = Mess ^ e % n```. Khi đó Mess gốc đã bị giản lược bởi phép chia dư cho n.

# [+]  Simple challenge

**BKSEC training 2024**
```shell
Length of message: 16
c = 1094555114006097458981
e = 65537
n = 3367854845750390371489
```
Form flag: BKSEC{fake_flag}

## Do something
Trường hợp tính toán phi(n) và mess như bình thường thì ta thu được kết quả như sau:
* ```phi(n) = 3367854845632834402324```
* ```d = pow(e, -1, phi(n)) = 3009008233992782483081 ```
* ```(m) mess = long_to_byte(pow(c, d, n)) = b'\x1f,-_\xe5h*#\xc0'```

Kết quả mess chúng ta thu được là '**\x1f,-_\xe5h*#\xc0**'. Đây là kết quả không mong muốn. Đúng như dự đoán, Mess gốc đã bị lược giản đi do N quá nhỏ.

Số lượng cặp khóa [N, e] chỉ là 1 nên không thể áp dụng **Đồng dư Trung hoa (CTR)**. Để tìm được flag ta cần tính toán theo một trường hợp khác.

# [+]   Idea

Trước khi tìm kiếm cách giải. Ta tìm hiểu một chút về cách hoạt động của hàm **Bytes_to_long**.
## [Bytes_to_long](https://pythonhosted.org/pycrypto/Crypto.Util.number-module.html)

Hàm trên chuyển đổi từng ký tự trong bảng mã ASCII sang binary rồi gộp các giá trị lại chuyểnsang kiểu số nguyên.

| Char | H        | E        | L        | L        | O        |
|------|----------|----------|----------|----------|----------|
| Bin  | 01001000 | 01000101 | 01001100 | 01001100 | 01001111 |
| Int  | 72       | 69       | 76       | 76       | 79       |


|      |                                                      |
|------|------------------------------------------------------|
|Result|100100001000101010011000100110001001111               |
| Long |310400273487                                          |

*_Long = 72 * pow(256, 4)  + 69 * pow(256, 3) + 76 * pow(256, 2) + 76 * pow(256, 1) + 79 * pow(256, 0)_*

## Ứng dụng bài toán

Mỗi ký tự Char = 256 bytes và chúng ta đã biết được độ dài của Flag là bao nhiêu. Form flag đã có, thứ tự các ký tự flag là bậc trong hệ 256

Nhìn lại Simple Chall trên ta có
|      |                |      |     |              |
|------|----------------|------|-----|--------------|
| FLAG | BKSEC{         | flag | }   | LenFlag = 16 |
| Long | 72891287028603 | x    | 125 |              |

**Từ bảng trên ta có:**
```shell 
C (cipher) = 72891287028603 * pow(256, 10) + x * pow(256, 1) + 125 * pow(256, 0)
```

**_==> Cần tìm x để giải ra được Flag_**

## Solve

Giá trị tại head Flag và end Flag đều đã có giá trị cố định là M. Việc tiếp theo chúng ta cần tìm là nội dung trong Flag.

Đặt M là giá trị đã biết trong Flag, X = x * 256. ```Flag = M + X.```

Ta có C = Flag ^ e % N. Áp dụng tính chất của Modulo ta có:

    m = (M + N) % N = (M % N) + (X % N) với m = pow(c, d, n)
    X % N = m - (M % N)
    X = N * i + (m - (M % N))
Bruit Force các giá trị i của X kết hợp điều kiện X % 256 = 0.
Kết quả của flag là M + X

## Code Solve
```shell
from Crypto.Util.number import bytes_to_long, long_to_bytes
c = 1094555114006097458981
e = 65537
n = 3367854845750390371489
p = 49450786403
q = 68105182763
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)

a = b"BKSEC{"
b = b"}"
M = (bytes_to_long(a) * pow(256,10) + bytes_to_long(b))
k = M % n
for i in range(1000):
    x = n* i + (m - k)
    if (x % 256 == 0):
        print(i, end = ' ')
        print(long_to_bytes(M + x))
```


## Flag
**_GOOD LUCK_**

