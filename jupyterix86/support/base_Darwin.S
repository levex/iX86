.section __TEXT,__text
.globl _main
_main:
  pushq %rbp
  movq %rsp, %rbp
  movq $1337, %rax

  ##__CODE__HERE__##

  movq str@GOTPCREL(%rip), %rdi
  movq %rax, %rsi
  movb $0, %al
  callq _printf

  movq $42, %rdi
  callq _exit

.section __DATA,__data
str:
  .asciz "The result is: %d!\n"

