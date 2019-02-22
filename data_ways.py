#Output the type and num of byte values of the file with the specified ID.
#usage: python data_ways.py [ID1] [ID2] [IDn](n is Natural number)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import collections

#Remove LF in line.
def remove_LF(line):
	line = line.replace('\r', '')
	line = line.replace('\n', '')
	return line
	
#Input byte position of target ID. 
def input_byte(file_name):
	print("\nFile name is %s"%file_name)
	print("Which byte do you chose?[Usage:byte1 byte2 byten(n is Natural number)]")
	line = input()
	line = remove_LF(line)
	byte_position = line.split(' ')
	return byte_position, len(byte_position)
	
args = sys.argv
file_num = len(args)-1
if file_num == 0:
	print("Error!: Please type the target ID.")
	exit()
file_name = []
for i in range(file_num):
	#file_name.append("log\\xor\\" + args[i+1] + "_log.csv")
	file_name.append("revorg\\xor\\" + args[i+1] + "_log.csv")
	try:
		f = open(file_name[i], 'r')
	except:
		print("cannot open %s"%file_name[i])
		exit()
		
	#Pick up 1line and calcurate DLC.
	line = f.readline()
	line = remove_LF(line)
	line = line.split(',')
	minus = 1
	for s in line:
		if s == '':
			minus += 1
	while(True):
		byte_position,byte_num = input_byte(file_name[i])
		eflag = False
		#Too many bytes inputed.
		if len(line)-minus < byte_num:
			eflag = True
		for x in range(byte_num):
			byte_position[x] = int(byte_position[x])
		#The value of the inputed bytes is too large or too small.
		if min(byte_position) < 1 or len(line)-1 < max(byte_position):
			eflag = True
		if eflag:
			print("Error!: byte field is incorrect")
			continue
		else:
			f.close()
			break
			
	output = args[i+1] + "_type_num.csv"
	a = open(output, "a")
	df = pd.read_csv(file_name[i], sep=',', header=None)
	#Calcurate the type and num of bytes.
	for x in range(byte_num):
		type_num = collections.Counter(df.iloc[:,byte_position[x]])
		a.write(str(byte_position[x]) + "\n")
		for key,value in sorted(type_num.items(), key=lambda z: -z[1]):
			a.write("{} {}\n".format(key, value))
		#a.write("type_num: %d\n"%len(type_num))
		a.write("\n")
	a.close()
