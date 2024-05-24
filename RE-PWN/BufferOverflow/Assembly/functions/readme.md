**Code :**
```shell
global  _start
extern  printf

section .data
    outFormat db  "It's %s", 0x0a, 0x00
    message db "Aligned!", 0x0a

section .text
_start:
    call print          ; print string
    call Exit           ; Exit the program

print:
    mov rdi, outFormat  ; set 1st argument (Print Format)
    mov rsi, message    ; set 2nd argument (message)
    call printf         ; printf(outFormat, message)
    ret

Exit:
    mov rax, 60
    mov rdi, 0
    syscall
```

Compile: ``nasm -f elf64 functions.s &&  ld functions.o -o functions -lc --dynamic-linker /lib64/ld-linux-x86-64.so.2``

**Debug**

Stack when call print:
```shell
00:0000│ rsp 0x7fffffffdf18 —▸ 0x401025 (_start+5) ◂— call 0x401044     <--- print
01:0008│ r13 0x7fffffffdf20 ◂— 0x1
```
- Call <=> push 8 bytes to stack
- We need 16x bytes in stack then we extended stack with 8 bytes.

**Modife**
```shell
_start:
    sub rsp, 0x8        ; Extended stack with 8 bytes
    call print          ; print string
    add rsp, 0x8        ; Return befor call print func
    call Exit           ; Exit the program
```

```shell
└─$ nasm -f elf64 functions.s &&  ld functions.o -o functions -lc --dynamic-linker /lib64/ld-linux-x86-64.so.2 && ./functions
It's Aligned!
```

