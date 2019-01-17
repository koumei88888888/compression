#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input = "yuki_1230s_id.csv"
output = "yuki_1230s_id.bin"
f = open(input, "r")
w = open(output, "wb")

bary = bytearray()
for line in f:
	line = line.replace("\n", "")
	line = line.replace("\r", "")
	line = line.replace("\r\n", "")
	
	id = list(line)
	#print(id)
	for data in id:
		data = int(data, 16)
		#print(data, end="")
		bary.append(data)
	#print("")
w.write(bary)
f.close
w.close()
