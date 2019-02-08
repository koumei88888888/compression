#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import sys

def sxor(s1,s2):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(str(format(int(a, 16) ^ int(b, 16), '04b')) for a,b in zip(s1,s2))

filename = r'corolla_fielder_10min_xor_dump.csv'
host = '192.168.11.4'

MovingData = ""
MovingDataLog = [[]]
OutputData = ""
OutputDataLog = [[]]
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.connect((host, 37562))
flag = False
watch = 0

huffman = {}
for line in open("huffman_list.csv", 'r'):
	line = line.replace('\n', '')
	line = line.split(" ")
	huffman[line[0]] = line[1]


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
ZERObit = 0
RawDLC = 0
ComDLC = 0
OutputData_RunLength = ""

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
  
  """
  #if len(OutputData_RunLength) % 6 != 0:
    #print(MovingDataLog[Nr][1])
  #print(OutputData_RunLength.to_bytes())
  #print("")
  """
  TotalRawIDbit += 24
  TotalComIDbit += len(huffman[MovingDataLog[Nr][0]])
  TotalRawDatabit += len(MovingDataLog[Nr][1])/2*8
  ZERObit += 1
  RawDLC += 4
  
  ######   send data   ######
  ID = huffman[MovingDataLog[Nr][0]]
  if len(OutputData_RunLength)%6 != 0:
  	zero = '1'
  	DLC = ''
  	OutputData_RunLength = ''
  else: 
    zero = '0'
    DLC = bin(len(OutputData_RunLength)//6).replace('0b', '')
    DLC = DLC.zfill(6)
    ComDLC += 6
    TotalComDatabit += len(OutputData_RunLength)
  line = ID + zero + DLC + OutputData_RunLength
  """
  print("ID: " + ID) #str
  print("zero: " + zero)
  print("DLC: " + DLC)
  print("Payload: " + OutputData_RunLength)
  print("line: " + line)
  print("")
  """

  """
  if len(OutputData_RunLength) % 6 != 0 and OutputData_RunLength != "1000000":
    print("Data: " + OutputData_RunLength) #str
  """
  
  """
  if watch < 100:
    print("line: " + line)
    watch = watch + 1
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
    s_sock.send(b_data)
    x = x + 1
  ##########################

  OutputDataLog.append(OutputData)
  Nr += 1

Raw = TotalRawDatabit + TotalRawIDbit + RawDLC
Compression = TotalComDatabit + ZERObit + TotalComIDbit + ComDLC
print("TotalRawIDbit:%d[bit]"%TotalRawIDbit)
print("TotalComIDbit:%d[bit]"%TotalComIDbit)
print("TotalZERObit:%d[bit]"%ZERObit)
print("RawDLC:%d[bit]"%RawDLC)
print("ComDLC:%d[bit]"%ComDLC)
print("TotalRawDatabit:%d[bit]"%TotalRawDatabit)
print("TotalComDatabit:%d[bit]"%TotalComDatabit)
print("Raw:%d[bit]" % Raw, "Compression:%d[bit]" % Compression)
print("data can be compressed from %d bits into %d bits (%f%%)" % \
  (Raw, Compression, float(Compression) / Raw * 100))

s_sock.close()