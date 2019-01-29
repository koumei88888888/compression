huffman = {}
for line in open("huffman_id.csv", 'r'):
	line = line.replace('\n', '')
	line = line.split(" ")
	huffman[line[0]] = line[1]
	
print(huffman)