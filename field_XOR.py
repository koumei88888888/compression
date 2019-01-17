#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

path_data = 'yuki_1230s_field.csv'
output = 'yuki_1230s_xor.csv'
canid = []
#list = np.empty((100, 9))
list = [["" for i in range(9)] for j in range(100)]
cnt = 0
num = 0

w = open(output, mode='w')
with open(path_data, mode='r', newline="") as f:
	for line in f:
		line = line.split(sep=',')
		for i in range(len(line)-1):
			line[i+1] = int(line[i+1])
		#line = np.array(line)
		if line[0] in canid:
			#print("line : {}".format(line))
			#int_line = []
			#int_line.insert(0, line[0])
			#int_line[1:] = map(int, line[1:])
			#print("int_line : {}".format(int_line))
			#print("int_line[0] : {}".format(int_line[0]))
			#print("int_line[1] : {}".format(int_line[1]))
			#list[canid.index(int_line[0])][1:] = int(list[canid.index(int_line[0])][1:])
			#print(int_line[1:] ^ int_list[1:])
			print(line[0], end = ',', file = w)
			for i in range(len(line)-2):
				print(line[i+1] ^ list[canid.index(line[0])][i+1], end = ',', file = w)
			print(line[len(line)-1] ^ list[canid.index(line[0])][len(line)-1], file = w)
			list[canid.index(line[0])] = line
		else:
			canid.append(line[0])
			#x = 0
			for x in range(len(line)):
				list[num][x] = line[x]
				#x = x + 1
			for x in range(len(line)-2):
				print(list[num][x], end = ',', file = w)
			print(list[num][len(line)-1], file = w)
			#np.insert(list[num], 0, float(line[0]))
			num = num + 1
w.close()