#!/usr/bin/env python
#coding:utf-8

input = "xor_time.csv"

f = open(input, "r")
Raw_size = 0
Run_size = 0
for line in f:
	line = line.replace("\n", "")
	line = line.replace("\r", "")
	line = line.split(":")
	Hour = bin(int(line[0])).replace("0b", "")
	Hour = Hour.zfill(5)
	Minites = bin(int(line[1])).replace("0b", "")
	Minites = Minites.zfill(6)
	line[2] = line[2].split(".")
	Second = bin(int(line[2][0])).replace("0b", "")
	Second = Second.zfill(6)
	Micro = bin(int(line[2][1])).replace("0b", "")
	Micro = Micro.zfill(19)
	Time = Hour + Minites + Second + Micro
	Run_Sum = 0
	for word in Time:
		if word == "0":
			Run_Sum += 1
		elif word == "1":
			Runlength = bin(Run_Sum).replace("0b", "")
			Runlength = Runlength.zfill(6)
			Run_Time = Runlength + Time[Run_Sum:]
			break
	Raw_size += len(Time)
	Run_size += len(Run_Time)
	"""
	print("Hour:%s"%Hour)
	print("Minites:%s"%Minites)
	print("Second:%s"%Second)
	print("Micro:%s"%Micro)
	print("Raw Time:%s"%Time)
	print("Run TIme:%s"%Run_Time)
	print("Run_Sum:%d Raw:%d Run:%d"%(Run_Sum, len(Time), len(Run_Time)))
	print("")
	"""
print("Raw data size:%d ,Run data size:%d ,Compression Rate:%f"%(Raw_size, Run_size, Run_size*100/Raw_size))
f.close()