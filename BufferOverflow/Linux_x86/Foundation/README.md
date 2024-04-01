# The memory
---
## Buffer
![Buffer](https://academy.hackthebox.com/storage/modules/31/buffer_overflow_1.png)

- <span style="color:blue">.text</span> : Chứa chỉ dẫn hợp ngữ của chương trình. Khu vuẹc này chỉ đọc, ghi vào khu vực này sẽ dẫn đến lỗi <span style="color:red">segmentation fault </span>

- <span style="color:blue">.data</span> : Chứa các biến toàn cục và biến tĩnh được chương trình khởi tạo rõ ràng.

- <span style="color:blue">.bss</span> : Một số trình biên dịch sử dụng .bss như 1 phần của phân đoạn dữ liệu. Chứa các biến phân bố tĩnh được biểu thị bằng 0 bit.

## Heap
![Heap](https://academy.hackthebox.com/storage/modules/31/buffer_overflow_1.png)

- <span style="color:blue">Heap memory</span> : Vùng này nằm sau phân đoạn .bss và được ghi tới địa chỉ cao hơn.

## Stack
![Stack](https://academy.hackthebox.com/storage/modules/31/buffer_overflow_1.png)

<span style="color:blue">Stack memory</span> là cấu trúc dữ liệu <span style="color:blue">LIFO</span> có địa chỉ trả về, tham số, tùy chọn trình biên dịch, khung con trỏ được lưu trữ.

Biến cục bộ trong C/C++ được lưu trữ tại Stack.

Stack là vùng bộ nhớ được xác định trong RAM. Nằm ở vùng bộ nhớ thấp hơn, trên biến toàn cục và biến tĩnh. Trong quá trình thực thi _phần mở rộng_ sẽ giảm từ địa chỉ cao xuống địa chỉ thấp.
```
| RAM | ... | Stack | Global and static variables | ...  |
|-----|-----|-------|-----------------------------|------|
|     | Low |    <- |                             | High |
```

Các biện pháp ngăn ngừa tràn bộ nhớ đệm như <span style="color:green">DEP/ASLR</span> 
- DEP (Data Execution Prevention) : Ngăn chặn thực thi dữ liệu, cho vùng bộ nhớ "read only".
- Vùng bộ nhớ chỉ đọc là nơi lưu trữ một số thông tin đầu vào của người dùng (Ví dụ: Stack), vì vậy ý ​​tưởng đằng sau DEP là ngăn người dùng tải shellcode lên bộ nhớ và sau đó đặt con trỏ lệnh tới shellcode.
- ASLR (Address Space Layout Randomization) để ngẫu nhiên hóa nơi mọi thứ được lưu trữ khiến ROP trở nên khó khăn hơn.

# Vulnerable Program

Vulnerable function called <span style="color:green">strcpy().</span> 

```shell: bow.c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int bowfunc(char *string) 
{
	char buffer[1024];
	strcpy(buffer, string);
	return 1;
}

int main(int argc, char *argv[]) 
{

	bowfunc(argv[1]);
	printf("Done.\n");
	return 1;
}
```
Complie: ``gcc bow.c -o bow32 -fno-stack-protector -z execstack -m32``

Some checking:
```
└─$ file bow32 | tr "," "\n"
bow32: ELF 32-bit LSB pie executable <--- file thực thi 32 bit (_x86)
 Intel 80386
 version 1 (SYSV)
 dynamically linked
 interpreter /lib/ld-linux.so.2
 BuildID[sha1]=bfb830a7aea40ef4fe650d91c866b8ed5abbd882
 for GNU/Linux 3.2.0
 not stripped
```

## Vulnerable C Functions
Một số hàm dễ bị tấn công trong C:
- strcpy
- gets
- sprintf
- scanf
- strcat
- ...

## GDB - PWNDBG

GDB, hay GNU Debugger, là trình gỡ lỗi tiêu chuẩn của các hệ thống Linux do Dự án GNU phát triển. Nó đã được chuyển sang nhiều hệ thống và hỗ trợ các ngôn ngữ lập trình C, C++, Objective-C, FORTRAN, Java và nhiều ngôn ngữ khác.

GDB cung cấp cho chúng tôi các tính năng truy xuất nguồn gốc thông thường như điểm dừng hoặc đầu ra theo dõi ngăn xếp và cho phép chúng tôi can thiệp vào việc thực thi các chương trình

## GDB - Syntax
```
pwndbg> disassemble main
Dump of assembler code for function main:
   0x000011d2 <+0>:     lea    ecx,[esp+0x4]
   0x000011d6 <+4>:     and    esp,0xfffffff0
   0x000011d9 <+7>:     push   DWORD PTR [ecx-0x4]
   0x000011dc <+10>:    push   ebp
   0x000011dd <+11>:    mov    ebp,esp
   0x000011df <+13>:    push   ebx
   0x000011e0 <+14>:    push   ecx
   0x000011e1 <+15>:    call   0x10a0 <__x86.get_pc_thunk.bx>
   0x000011e6 <+20>:    add    ebx,0x2e0e
   0x000011ec <+26>:    mov    eax,ecx
   0x000011ee <+28>:    mov    eax,DWORD PTR [eax+0x4]
   0x000011f1 <+31>:    add    eax,0x4
   0x000011f4 <+34>:    mov    eax,DWORD PTR [eax]
   0x000011f6 <+36>:    sub    esp,0xc
   0x000011f9 <+39>:    push   eax
   0x000011fa <+40>:    call   0x119d <bowfunc>
   0x000011ff <+45>:    add    esp,0x10
   0x00001202 <+48>:    sub    esp,0xc
   0x00001205 <+51>:    lea    eax,[ebx-0x1fec]
   0x0000120b <+57>:    push   eax
   0x0000120c <+58>:    call   0x1050 <puts@plt>
   0x00001211 <+63>:    add    esp,0x10
   0x00001214 <+66>:    mov    eax,0x1
   0x00001219 <+71>:    lea    esp,[ebp-0x8]
   0x0000121c <+74>:    pop    ecx
   0x0000121d <+75>:    pop    ebx
   0x0000121e <+76>:    pop    ebp
   0x0000121f <+77>:    lea    esp,[ecx-0x4]
   0x00001222 <+80>:    ret
End of assembler dump.
pwndbg>
```

Sự khác biệt giữa cú pháp AT&T và Intel không chỉ ở cách trình bày các lệnh bằng ký hiệu của chúng mà còn ở thứ tự và hướng thực hiện và đọc các lệnh.

**EXAMPLE :** 
```
0x0000058d <+11>:	mov    ebp,esp      <--- Intel
0x0000058d <+11>:	mov    %esp,%ebp    <--- AT&T
```

| Intel Syntax |             |             |
|--------------|-------------|-------------|
| Instruction  | Destination | Source      |
| mov          | ebp         | esp         |

| AT&T Syntax  |             |             |
|--------------|-------------|-------------|
| Instruction  | Source      | Destination |
| mov          | %esp        | %ebp        |






