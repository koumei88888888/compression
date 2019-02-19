#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import sys

def sxor(s1,s2):    
    return ''.join(str(format(int(a, 16) ^ int(b, 16), '04b')) for a,b in zip(s1,s2))

filename = r'corolla_fielder_10min_xor_dump.csv'
host = '192.168.11.4'

MovingData = ""
MovingDataLog = [[]]
OutputData = ""
OutputDataLog = [[]]
#s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_sock.connect((host, 37562))
flag = False
watch = 0

IDs = ["0AA" ,"020" ,"025" ,"024" ,"127" ,"260" ,"1C4" ,"247" ,"245" ,"224" ,"0B4" ,"230"]

huffman = {}
for line in open("huffman_list.csv", 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  huffman[line[0]] = line[1]

path = "type_num\\xor\\for_huffman\\huffman\\{}_huffman.csv"
DATA_0AA_1 = {}
for line in open(path.format("0AA_1"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_0AA_1[line[0]] = line[1]
DATA_0AA_3 = {}
for line in open(path.format("0AA_3"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_0AA_3[line[0]] = line[1]
DATA_0AA_5 = {}
for line in open(path.format("0AA_5"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_0AA_5[line[0]] = line[1]
DATA_0AA_7 = {}
for line in open(path.format("0AA_7"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_0AA_7[line[0]] = line[1]
DATA_0B4_5 = {}
for line in open(path.format("0B4_5"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_0B4_5[line[0]] = line[1]
DATA_0B4_6 = {}
for line in open(path.format("0B4_6"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_0B4_6[line[0]] = line[1]
DATA_1C4_1 = {}
for line in open(path.format("1C4_1"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_1C4_1[line[0]] = line[1]
DATA_024_2 = {}
for line in open(path.format("024_2"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_024_2[line[0]] = line[1]
DATA_025_1 = {}
for line in open(path.format("025_1"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_025_1[line[0]] = line[1]
DATA_025_5 = {}
for line in open(path.format("025_5"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_025_5[line[0]] = line[1]
DATA_127_4 = {}
for line in open(path.format("127_4"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_127_4[line[0]] = line[1]
DATA_127_6 = {}
for line in open(path.format("127_6"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_127_6[line[0]] = line[1]
DATA_245_4 = {}
for line in open(path.format("245_4"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_245_4[line[0]] = line[1]
DATA_247_1 = {}
for line in open(path.format("247_1"), 'r'):
  line = line.replace('\n', '')
  line = line.split(" ")
  DATA_247_1[line[0]] = line[1]

Nr = 1
for line in open(filename, 'r'):
  MovingData = line[:-1].split(' ')
  MovingDataLog.append(MovingData)
  Nr += 1

FlagALLCANID = [0]*2048 #New:0, Pre:1
for i in range(0, len(FlagALLCANID)):
  FlagALLCANID[i] = 0

AbsoluteCANData = dict() # key:=CAN ID
Nr = 1
TotalRawDatabit = 0
TotalComDatabit = 0
TotalRawIDbit = 0
TotalComIDbit = 0
RawDLC = 0
ComDLC = 0
other_DLC = 0
OutputData_RunLength = ""

CDATAbit = 0
ZERO = 0

f = open(filename, "r")
for line in f:
  buff = 0
  line = line.replace("\n", "")
  line = line.split(" ")
  if line[0] == "0AA":
      buff += len(DATA_0AA_1[str(int(line[1][0:2], 16))])
      buff += len(DATA_0AA_3[str(int(line[1][4:6], 16))])
      buff += len(DATA_0AA_5[str(int(line[1][8:10], 16))])
      buff += len(DATA_0AA_7[str(int(line[1][12:14], 16))])
      buff += 8*4
  elif line[0] == "0B4":
      buff += 1
      buff += 1
      buff += 1
      buff += 1
      buff += len(DATA_0B4_5[str(int(line[1][8:10], 16))])
      buff += len(DATA_0B4_6[str(int(line[1][10:12], 16))])
      buff += 8*2
  elif line[0] == "1C4":
      ZERO += 1
      if line[1] == "0000000000000000":
          pass
      else:
          buff += len(DATA_1C4_1[str(int(line[1][0:2], 16))])
          buff += 8
          buff += 1
          buff += 1
          buff += 1
          buff += 1
          buff += 1
          buff += 8
  elif line[0] == "020":
      pass
  elif line[0] == "024":
      buff += 1
      buff += len(DATA_024_2[str(int(line[1][2:4], 16))])
      buff += 1
      buff += 1
      buff += 1
      buff += 1
      buff += 1
      buff += 8
  elif line[0] == "025":
      buff += len(DATA_025_1[str(int(line[1][0:2], 16))])
      if line[1][2:4] == "00":
          buff += 1
      else:
          buff += 8
      buff += 1
      buff += 1
      buff += len(DATA_025_5[str(int(line[1][8:10], 16))])
      buff += 8
      buff += 1
      buff += 8
  elif line[0] == "127":
      buff += 1
      buff += 1
      buff += 1
      buff += len(DATA_127_4[str(int(line[1][6:8], 16))])
      if line[1][8:10] == "00":
          buff += 1
      else:
          buff += 8
      buff += len(DATA_127_6[str(int(line[1][10:12], 16))])
      buff += 8
      buff += 8
  elif line[0] == "224":
      buff += 1
      buff += 1
      buff += 1
      buff += 1
      buff += 1
      if line[1][10:12] == "00":
          buff += 1
      else:
          buff += 8
      buff += 1
      buff += 1
  elif line[0] == "230":
      buff += 1
  elif line[0] == "245":
      ZERO += 1
      if line[1] == "0000000000":
          pass
      else:
          buff += 1
          buff += 1
          if line[1][4:6] == "00":
              buff += 1
          else:
              buff += 8
          buff += len(DATA_245_4[str(int(line[1][6:8], 16))])
          if line[1][8:10] == "00":
              buff += 1
          else:
              buff += 8
  elif line[0] == "247":
      ZERO += 1
      if line[1] == "0000000000":
          pass
      else:
          buff += len(DATA_247_1[str(int(line[1][0:2], 16))])
          if line[1][2:4] == "00":
              buff += 1
          else:
              buff += 8
          buff += 1
          buff += 1
          buff += 1
  elif line[0] == "260":
      pass
  else:
      pass
      #buff = 8*8
  CDATAbit += buff
f.close()

for i in range(0, len(MovingDataLog)-1):
  AbsoluteCANData.setdefault(MovingDataLog[Nr][0], MovingDataLog[Nr][1])
  RunLength_Sum = 0
  OutputData_RunLength = ""
  AbstData = AbsoluteCANData[MovingDataLog[Nr][0]]
  AbsoluteCANData[MovingDataLog[Nr][0]] = MovingDataLog[Nr][1]
  DiffData = MovingDataLog[Nr][1]
  OutputData = sxor(AbstData, DiffData)

  for j in range(0, len(OutputData)):
    if OutputData[j] == '0':
      RunLength_Sum += 1
    else :
      OutputData_RunLength += str(format(RunLength_Sum, '06b'))
      RunLength_Sum = 0
  if RunLength_Sum != 0:
    OutputData_RunLength += str(format(RunLength_Sum, '06b'))
  
  TotalRawIDbit += 24
  TotalComIDbit += len(huffman[MovingDataLog[Nr][0]])
  TotalRawDatabit += len(MovingDataLog[Nr][1])/2*8
  RawDLC += 4
  
  ######   send data   ######
  ID = huffman[MovingDataLog[Nr][0]]
  if OutputData_RunLength == "1000000":
    DLC = '000000'
    OutputData_RunLength = ''
  else: 
    #print(bin(len(OutputData_RunLength)//6).replace('0b', ''))
    DLC = bin(len(OutputData_RunLength)//6).replace('0b', '')
    DLC = DLC.zfill(6)
    TotalComDatabit += len(OutputData_RunLength)
  if MovingDataLog[Nr][0] not in IDs:
    CDATAbit += len(OutputData_RunLength)
    other_DLC += 6
  ComDLC += 6
  line = ID + DLC + OutputData_RunLength

  """
  x = 0
  while(True):
    if flag == True:
      line = tmp + line
      flag = False
    if (len(line)-x*8)/8 < 1:
      last = (len(line)%8) * (-1)
      tmp = line[last:]
      flag = True
      break
    i_data = int(line[8*x:8*(x+1)], 2)
    b_data = i_data.to_bytes(1, 'big')
  """

  OutputDataLog.append(OutputData)
  Nr += 1
  #print(Nr)

Raw = TotalRawDatabit + TotalRawIDbit + RawDLC
Compression = TotalComDatabit + TotalComIDbit + ComDLC
print("TotalRawIDbit:%d[bit]"%TotalRawIDbit)
print("TotalComIDbit:%d[bit]"%TotalComIDbit)
print("RawDLC:%d[bit]"%RawDLC)
print("ComDLC:%d[bit]"%ComDLC)
print("TotalRawDatabit:%d[bit]"%TotalRawDatabit)
print("TotalComDatabit:%d[bit]"%TotalComDatabit)
print("Data Compression Rate:%f"%(TotalComDatabit*100 / TotalRawDatabit))
print("Raw:%d[bit]" % Raw, "Compression:%d[bit]" % Compression)
print("data can be compressed from %d bits into %d bits (%f%%)" % \
  (Raw, Compression, float(Compression) / Raw * 100))
  
print("")
print("Total Com bit True:%d[bit]"%CDATAbit)
print("Data Compression Rate:%f"%(CDATAbit*100 / TotalRawDatabit))
print("Total ZERO_flag:%d[bit]"%ZERO)
print("Total DLC:%d[bit]"%other_DLC)
Compression = TotalComIDbit + CDATAbit + ZERO + other_DLC
print("data can be compressed from %d bits into %d bits (%f%%)" % \
  (Raw, Compression, float(Compression) / Raw * 100))
#s_sock.close()