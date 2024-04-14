global _start

section .text
_start:
    mov rax, 2
    mov rcx, 5
loopRAX:
    imul rax, rax
    loop loopRAX
