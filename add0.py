#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

input = "yuki_1230s_field.csv"
output = "yuki_1230s_id_0.csv"
w = open(output, "w")
writer = csv.writer(w, lineterminator='\n')
with open(input, "r") as f:
	for line in f:
		line = line.replace("\n", "")
		line = line.replace("\r", "")
		line = line.replace("\r\n", "")
		line = line.split(",")
		if len(line[0]) == 2:
			line[0] = "0" + line[0]
		writer.writerow(line)
w.close()