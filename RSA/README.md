# [-]   WHAT IS RSA ?

Trong mật mã học, RSA là một thuật toán mật mã hóa khóa công khai. Đây là thuật toán đầu tiên phù hợp với việc tạo ra chữ ký điện tử đồng thời với việc mã hóa. Nó đánh dấu một sự tiến bộ vượt bậc của lĩnh vực mật mã học trong việc sử dụng khóa công cộng. RSA đang được sử dụng phổ biến trong thương mại điện tử và được cho là đảm bảo an toàn với điều kiện độ dài khóa đủ lớn.
# [-]   How does it work ?
***
## [+] Cách thức hoạt động chung

Mã hóa RSA là dạng mã hóa sử dụng Khóa bất đối xứng (asymmetric encryption) gồm 2 khóa: **Khóa công khai (Public Key)** và **Khóa bí mật (Private Key)**

Mỗi khóa gồm những số cố định dùng trong cả mã hóa và giải mã.
## [+] Tạo bộ mã hóa

Giả sử Bob và Alice trao đổi thông tin với nhau. Bob và Alice cùng thống nhất để tạo ra được Khóa công khai và Khóa bí mật
* N được tạo ra bằng tích hai số nguyên tố p và q ```N = p * q```
* Tính giá trị hàm số phi Euler ```phi(n) = (p - 1) * (q - 1)```
* Chọn số e < phi(n) sao cho gcd(e, phi(n)) = 1
* Tính d sao cho d*e ≡ 1 [phi(n)]

**_Khóa công khai bao gồm:_** N, e
**_Khóa bí mật gồm:_** N, e, d

Alice gửi bộ khóa công khai [N, e] cho Bob để Bob mã hóa tin nhắn và gửi lại cho Alice. Alice dùng khóa bí mật cá nhân của mình là [N, e, d] để giải mã thông tin Bob gửi.
## [+] Truyền thông tin

Tin nhắn Bob gửi cho Alice sẽ được mã hóa. M (Mess) là nội dung trước khi Bob gửi đi, C (cipher) là nội dung sau khi Bob mã hóa để gửi cho Alice.

Bob gửi cho Alice: ```C = M ^ e % N```
Alice dùng khóa cá nhân để giải mã ```M = C ^ d % N```

# [-]   Some problem 
**_Check_**