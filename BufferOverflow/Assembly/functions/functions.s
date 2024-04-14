global  _start
extern  printf

section .data
    outFormat db  "It's %s", 0x0a, 0x00
    message db "Aligned!", 0x0a

section .text
_start:
    sub rsp, 0x8
    call print          ; print string
    add rsp, 0x8
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