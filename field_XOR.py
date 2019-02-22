#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

path_data = 'revorg_moving_log_5min_2.csv'
output = 'revorg_moving_log_5min_xor.csv'
canid = []
list = [["" for i in range(9)] for j in range(100)]
cnt = 0
num = 0

w = open(output, mode='w')
with open(path_data, mode='r', newline="") as f:
	for line in f:
		line = line.replace("\r\n", '')
		line = line.split(sep=',')
		data = []
		data.append(line[0])
		for i in range(1, len(line)):
			if(line[i] != ""):
				data.append(int(line[i], 16))
		#print(data)
		if data[0] in canid:
			print(data[0], end = ',', file = w)
			for i in range(len(data)-2):
				print(data[i+1] ^ list[canid.index(data[0])][i+1], end = ',', file = w)
			print(data[len(data)-1] ^ list[canid.index(data[0])][len(data)-1], file = w)
			list[canid.index(data[0])] = data
		else:
			canid.append(data[0])
			for x in range(len(data)):
				list[num][x] = data[x]
			for x in range(len(data)-1):
				print(list[num][x], end = ',', file = w)
			print(list[num][len(data)-1], file = w)
			num = num + 1
w.close