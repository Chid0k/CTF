# Topic: Stack
---

- Stack là đoạn bộ nhớ được phân bổ cho việc lưu trữ dữ liệu chương trình tạm thời. Đỉnh của stack được chỉ tới bởi *Top Stack Pointer* (SP) và đáy stack được chỉ bởi *Base Pointer* (BP)

- Dữ liệu được *Push* sẽ nằm trên đỉnh stack và *Pop* sẽ được lấy từ đỉnh stack ra.

- Chúng ta sẽ đẩy dữ liệu các thanh ghi vào stack trước khi gọi một **func** hoặc **syscall** và khôi phục sau khi kết thúc hàm.

# Topic: Syscall
---
**Linux syscall**
- Hàm có sẵn được viết bằng C cung cấp bởi OS Kernel. Syscall lấy các đối số cần thiết trong thanh ghi và thực thi hàm với đối số được cung cấp.

- Tìm các tập lệnh *syscall* thông qua **syscall number** hoặc đọc file **unistd_64.h** trong hệ thống
```shell
$ cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h
#ifndef _ASM_X86_UNISTD_64_H
#define _ASM_X86_UNISTD_64_H 1

#define __NR_read 0
#define __NR_write 1
#define __NR_open 2
#define __NR_close 3
#define __NR_stat 4
#define __NR_fstat 5
```

> Note: With 32-bit x86 processors, the syscall numbers are in the unistd_32.h file.

- Để sử dụng syscall ghi, trước tiên chúng ta phải biết nó chấp nhận những đối số nào. Để tìm các đối số được syscall chấp nhận, chúng ta có thể sử dụng lệnh man -s 2 với tên syscall từ danh sách trên:

```shell
$ man -s 2 write
...SNIP...
       ssize_t write(int fd, const void *buf, size_t count);
>>>>       
1.  File Descriptor fd to be printed to (usually 1 for stdout)
2.  The address pointer to the string to be printed
3.  The length we want to print
```
[Syscall Table](https://filippo.io/linux-syscall-table/)
[More](https://github.com/torvalds/linux/blob/master/arch/x86/entry/syscalls/syscall_64.tbl)

**Syscall calling convention**
Để gọi một syscall :
- Lưu thanh ghi vào stack
- rax lưu syscall number
- Set các đối số vào các thanh ghi
- sử dụng syscall để gọi hàm. 

**Syscall Argument**
|         Description         | 64-bit Register | 8-bit Register |
|:---------------------------:|:---------------:|:--------------:|
| Syscall Number/Return value | rax             | al             |
| Callee Saved                | rbx             | bl             |
| 1st arg                     | rdi             | dil            |
| 2nd arg                     | rsi             | sil            |
| 3rd arg                     | rdx             | cl             |
| 4th arg                     | rcx             | bpl            |
| 5th arg                     | r8              | r8b            |
| 6th arg                     | r9              | r9b            |

Như chúng ta có thể thấy, chúng ta có một thanh ghi cho mỗi đối số trong số 6 đối số đầu tiên. Bất kỳ đối số bổ sung nào cũng có thể được lưu trữ trong ngăn xếp.

* Example: `` write(int fd, const void *buf, size_t count);``
```shell
    mov rax, 1          ; rax: syscall number 1
    mov rdi, 1          ; rdi: fd 1 for stdout
    mov rsi,message     ; rsi: pointer to message
    mov rdx, 20         ; rdx: print length of 20 bytes
```

> Nếu chúng ta cần tạo một con trỏ tới một giá trị được lưu trong một thanh ghi, chúng ta chỉ cần đẩy nó vào ngăn xếp, sau đó sử dụng con trỏ rsp để trỏ tới nó.

MORE:

>Bây giờ chúng ta hãy xem các đối số được truyền từ caller đến callee như thế nào.

![Calling convention](https://www.ired.team/~gitbook/image?url=https:%2F%2F386337598-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LFEMnER3fywgFHoroYn%252F-M_kPdFv-dvxpx8KxFzD%252F-M_kPmfxo1wKpMfYNvkM%252Fimage.png%3Falt=media%26token=6507484d-b6b9-43b8-b9aa-64167c14aba1&width=768&dpr=1&quality=100&sign=787ba9af101145c8f8da23a2820dbda737fa8242932ed07fc6e5f0a118f9fc79)

| Argument # | Location   | Variable | Value | Colour |
|------------|------------|----------|-------|--------|
| 1          | RDI        | a        | 0x1   | Red    |
| 2          | RSI        | b        | 0x2   | Red    |
| 3          | RDX        | c        | 0x3   | Red    |
| 4          | RCX        | d        | 0x4   | Red    |
| 5          | R8         | e        | 0x5   | Orange |
| 6          | R9         | f        | 0x6   | Orange |
| 7          | RSP + 0x10 | g        | 0x7   | Lime   |
| 8          | RSP + 0x18 | h        | 0x8   | Lime   |
| 9          | RSP + 0x20 | i        | 0x9   | Lime   |


**Exit syscall**
- Nếu không kết thúc syscall chương trình sẽ dẫn đến lỗi phân đoạn (segment fault).

- Vì vậy, hãy thêm phần này vào cuối mã của chúng ta. Đầu tiên chúng ta cần tìm *Exit syscall number* như sau

```shell
$ grep exit /usr/include/x86_64-linux-gnu/asm/unistd_64.h

#define __NR_exit 60
#define __NR_exit_group 231

>>>
$ man -s 2 exit
void _exit(int status);
```
- _Exit() cần 1 đối số truyền vào. Trong Linux, bất cứ khi nào một chương trình thoát ra mà không gặp bất kỳ lỗi nào, nó sẽ chuyển mã thoát là 0.

```shell
    mov rax, 60     ;   exit syscall number
    mov rdi, 0      ;   startus argument
    syscall         ;   calling
```
# Topic: Call / ret
---

- Khi cần thực thi một hàm, ta cần 1 lời gọi hàm: call func.
- Lệnh **call** sẽ lưu IP của lệnh tiếp theo vào Stack và nhảy tới hàm chỉ định.
- Sau khi thủ tục được thực thi, chúng ta nên kết thúc nó bằng lệnh **ret** để quay lại điểm trước khi chuyển sang thủ tục.
- Lệnh **ret** chuyển địa chỉ ở đầu ngăn xếp thành **rip**, do đó lệnh tiếp theo của chương trình được khôi phục về địa chỉ trước khi chuyển sang quy trình.

| Instruction |                                        Description                                        |
|:-----------:|:-----------------------------------------------------------------------------------------:|
| call        | push the next instruction pointer rip to the stack, then jumps to the specified procedure |
| ret         | pop the address at rsp into rip, then jump to it                                          |

```
+---------------+----+--+---------+     +----------+----+--+---------+------------+
|      CALL     |    |  | Stack   |     | RET      |    |  | Stack   |            |
+---------------+----+--+---------+     +----------+----+--+---------+------------+
| instruction 1 |    |  | ...     |     | ins func |    |  | ...     |            |
+---------------+----+--+---------+     +----------+----+--+---------+------------+
| call func     | <- |  | func    |     | ret      | <- |  | func    | <- pop     |
+---------------+----+--+---------+     +----------+----+--+---------+------------+
| instruction 2 |    |  | func    |     |          |    |  | func    | <- pop     |
+---------------+----+--+---------+     +----------+----+--+---------+------------+
|               |    |  | IP ins2 |     |          |    |  | IP ins2 | <- SP = IP |
+---------------+----+--+---------+     +----------+----+--+---------+------------+
```

> Update: 14/04/2024



