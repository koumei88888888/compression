w = open("huffman_hex_id.csv", "w")
flag = 0
with open("huffman_id.csv", "r") as f:
	for line in f:
		if flag == 0:
			flag = 1
		else:
			line = line.replace('\r','')
			line = line.replace('\n','')
			line = line.replace('\r\n','')
			line = line.split(' ')
			llen = len(line[1])
			if llen <= 8:
				line[1] = line[1].zfill(8)
				#print(int(line[1][:4], 2), int(line[1][4:8], 2))
				#print(hex(int(line[1][:4], 2)), hex(int(line[1][4:8], 2)))
				line[1] = hex(int(line[1][:4], 2)) +  hex(int(line[1][4:8], 2))
			elif llen > 8 and llen <= 16:
				line[1] = line[1].zfill(16)
				line[1] = hex(int(line[1][:4], 2)) +  hex(int(line[1][4:8], 2)) + " " + hex(int(line[1][8:12], 2)) +  hex(int(line[1][12:16], 2))
			line[1] = line[1].replace("0x", "")
			print("{} {}".format(line[0], line[1]), file=w)
w.close()