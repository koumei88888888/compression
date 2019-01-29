#import pandas as pd
#df = pd.read_csv("corolla_fielder_10min.csv", sep=',', names=('Time', 'Ch', 'Protocol', 'Dir', 'Label', 'State', 'Type', 'Format', 'ID', 'DLC', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'Sum'))
#df = df[['ID', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']]
#df.to_csv("corolla_fielder_10min_2.csv", index=False)

input = "corolla_fielder_10min_xor.csv"
output = "corolla_fielder_10min_xor_dump.csv"
w = open(output, "w")
with open(input, "r") as f:
	for line in f:
#		line = line.replace("\n", "")
#		line = line.replace("\r", "")
#		line = line.replace("\r\n", "")
#		line = f.readline()
		line = line.split(",")
		data = line[0] + " "
		for i in range(1,len(line)):
			num = hex(int(line[i]))
			if len(num) == 3:
				num = '0' + num
			data = data + num
		data = data.replace(',', '')
		data = data.replace('0x', '')
		data = data + '\n'
		w.write(data)
w.close()