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
host = '192.168.11.43'

MovingData = ""
MovingDataLog = [[]]
OutputData = ""
OutputDataLog = [[]]
#s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_sock.connect((host, 37562))
flag = False
watch = 0

huffman = {}
c_huffman = {}
for line in open("huffman_list.csv", 'r'):
	line = line.replace('\n', '')
	line = line.split(" ")
	huffman[line[0]] = line[1]
	c_huffman[line[0]] = 0


Nr = 1
for line in open(filename, 'r'):
  MovingData = line[:-1].split(' ')
  MovingDataLog.append(MovingData)
  #print MovingDataLog[Nr][0]
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
OutputData_RunLength = ""
Abst_ALLCANID_bit = [0]*2048
Diff_ALLCANID_bit = [0]*2048

for i in range(0, len(MovingDataLog)-1):
  if FlagALLCANID[int(MovingDataLog[Nr][0], 16)] == 0:
    FlagALLCANID[int(MovingDataLog[Nr][0], 16)] = 1
    AbsoluteCANData.setdefault(MovingDataLog[Nr][0], MovingDataLog[Nr][1])
    OutputData = MovingDataLog[Nr][1]
    OutputData_RunLength = OutputData
  else :
    RunLength_Sum = 0
    OutputData_RunLength = ""
    AbstData = AbsoluteCANData[MovingDataLog[Nr][0]]
    AbsoluteCANData[MovingDataLog[Nr][0]] = MovingDataLog[Nr][1]
    DiffData = MovingDataLog[Nr][1]
    OutputData = sxor(AbstData, DiffData)
    """
    print MovingDataLog[Nr][0], list(map(hex, map(ord, OutputData)))
    print(MovingDataLog[Nr][0], OutputData, len(OutputData))
    print("")
    """
    for j in range(0, len(OutputData)):
      if OutputData[j] == '0':
        RunLength_Sum += 1
      else :
        #print RunLength_Sum
        #print OutputData_RunLength, str(format(RunLength_Sum, '06b'))
        OutputData_RunLength += str(format(RunLength_Sum, '06b'))
        #print OutputData_RunLength, RunLength_Sum
        RunLength_Sum = 0
    if RunLength_Sum != 0:
      OutputData_RunLength += str(format(RunLength_Sum, '06b'))
    #print(MovingDataLog[Nr][0], OutputData_RunLength, AbstData, DiffData, len(OutputData_RunLength))
  #print len(MovingDataLog[Nr][1])/2*8, len(OutputData_RunLength)
  #print(MovingDataLog[Nr][1], len(MovingDataLog[Nr][1]) ,OutputData_RunLength, len(OutputData_RunLength))
  TotalRawDatabit += len(MovingDataLog[Nr][1])/2*8
  TotalRawIDbit += 24
  #if len(OutputData_RunLength) != 7:
  TotalComDatabit += len(OutputData_RunLength)
  
  """
  #if len(OutputData_RunLength) % 6 != 0:
    #print(MovingDataLog[Nr][1])
  #print(OutputData_RunLength.to_bytes())
  #print("")
  """
  TotalComIDbit += len(huffman[MovingDataLog[Nr][0]])
  RawDLC += 4
  ComDLC += 6
  
  ######   send data   ######
  if c_huffman[MovingDataLog[Nr][0]] == 0:
    OutputData_RunLength = bin(int(OutputData_RunLength, 16)).replace('0b', '')
    c_huffman[MovingDataLog[Nr][0]] = 1
  #print("ID: " + huffman[MovingDataLog[Nr][0]]) #str
  #print("DLC: %d"%len(OutputData_RunLength))
  if len(OutputData_RunLength) % 6 != 0 and OutputData_RunLength != "1000000":
    print("Data: " + OutputData_RunLength) #str
  #print(bin(len(OutputData_RunLength)).replace("0b", ""))
  line = huffman[MovingDataLog[Nr][0]] + bin(len(OutputData_RunLength)).replace("0b", "") + OutputData_RunLength
  #if watch < 100:
  #  print("line: " + line)
  #  watch = watch + 1
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
    #s_sock.send(b_data)
    x = x + 1
  ##########################

  OutputDataLog.append(OutputData)
  Nr += 1

Raw = TotalRawDatabit + TotalRawIDbit + RawDLC
Compression = TotalComDatabit + TotalComIDbit + ComDLC
print("TotalRawDatabit:%d[bit]"%TotalRawDatabit)
print("TotalComDatabit:%d[bit]"%TotalComDatabit)
print("TotalRawIDbit:%d[bit]"%TotalRawIDbit)
print("TotalComIDbit:%d[bit]"%TotalComIDbit)
print("RawDLC:%d[bit]"%RawDLC)
print("ComDLC:%d[bit]"%ComDLC)
print("Raw:%d[bit]" % Raw, "Compression:%d[bit]" % Compression)
print("data can be compressed from %d bits into %d bits (%f%%)" % \
  (Raw, Compression, float(Compression) / Raw * 100))
#for Nr in range(0, len(OutputDataLog)):
  #print OutputDataLog[Nr]
#s_sock.close()