#!/usr/bin/env python
#coding:utf-8
import pandas as pd

df = pd.read_csv("huffman_id.csv", sep=' ', index_col=0)
output = "yuki_1230s_huffman_id.csv"
#w = open(output, "wb")
#print(df)
with open("yuki_1230s_id.csv", "r") as f:
	for line in f:
		line = line.replace('\r','')
		line = line.replace('\n','')
		line = line.replace('\r\n','')
		
		print(df.at[line, "bin_id"])
		df.at[line, 'bin_id'].to_csv(output)
		#w.write(line)
#w.close()