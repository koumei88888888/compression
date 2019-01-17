#!/usr/bin/env python
# -*- coding:cp932 -*-
with open("data_bin.bin", "wb") as f:
	line = bytearray([0b11111111, 0b10000000])
	f.write(line)
with open("data_bin2.bin", "wb") as f:
	line = bytearray([0b0, 0b000000000000000000000000000])
	f.write(line)
with open("data_bin.bin", "rb") as f:
	data = f.read()
	print(data)
with open("data_bin2.bin", "rb") as f:
	data = f.read()
	print(data)