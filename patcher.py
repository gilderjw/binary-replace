import os
import binascii

file = open('whitelist', 'r')
whitelist = file.read().split()
hexList = []

file.close()

for s in whitelist:
	hexList.append(s)

file = open('challenge1', 'rb')
binary = binascii.hexlify(file.read())
file.close()

file = open('patched', 'w')


repl = 0
for old in hexList: 
	if old in binary:
		repl = repl+1
		binary = binary.replace(old, '909090CD80')

file.write(binary.decode("hex"))
file.close()
print repl