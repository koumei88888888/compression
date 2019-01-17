#usage: python id_probability.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open('yuki_1230s_id.csv')
output = 'id_probability.txt'
w = open(output, mode='w')
pro = {}

#Count number of messages
num_lines = sum(1 for line in f)
f.close()

#Calculate the probability for each ID
f = open('id_num.txt')
cnt = 0
#sum = 0
for line in f:
	line = line.split(' ')
	pro[cnt] = int(line[1]) / num_lines * 100
	pro[cnt] = round(pro[cnt], 2)
	print('{},{}%'.format(line[0], pro[cnt]), file = w)
#	sum += pro[cnt]
	cnt = cnt + 1
#print(sum)

#File close
f.close()
w.close()