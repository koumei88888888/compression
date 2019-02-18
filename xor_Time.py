#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

path_data = 'corolla_fielder_10min_time_2.csv'
output = 'xor_time.csv'
canid = []
pre = "00:00:00.000000"
pre = datetime.datetime.strptime(pre, '%H:%M:%S.%f')
f = open(path_data, "r")

w = open(output, "w")
for line in f:
	line = line.replace("\n", "")
	line = line.replace("\r", "")
	line = line.split(",")
	line[0] = line[0].replace("+0", "")
	line[0] = line[0].split(".")
	Time = line[0][0] + "." + line[0][1] + line[0][2]
	DT = datetime.datetime.strptime(Time, '%H:%M:%S.%f')
	print(DT-pre, file=w)
	pre = DT
f.close()