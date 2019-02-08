#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import array
import sys

#memo
#raw_data = b'Hello, World!'
    #msg = struct.pack('!16s', raw_data)
    #s_sock.send(msg)
    
    #data = [['100010101000101010010101010010101000101010'],['00101001001010100100101010'],['00001000000'],['10000110001001001010100100101001010'],['01001010100101010101010010101010100101001000101'],['11111110000000001111111000000010110']]

host = '192.168.11.43'

if __name__ == '__main__':
    s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_sock.connect((host, 37562))

    data = ['100010101000101010010101010010101000101010','11101001001010100100101010','00001000000','10000110001001001010100100101001010','01001010100101010101010010101010100101001000101','11111110000000001111111000000010110']
    i = 0
    for _ in data:
        x = 0
        while(True):
            if (len(data[i])-x*8)/8 < 1:
                last = (len(data[i]) % 8) * (-1)
                if i+1 != len(data):
                    data[i+1] = data[i][last:] + data[i+1]
                else:
                    print("last char:",last)
                    sys.exit()
                i = i + 1
                break
            print(data[i][8*x:8*(x+1)])
            i_data = int(data[i][8*x:8*(x+1)], 2)
            b_data = i_data.to_bytes(1, 'big')
            print(b_data)
            print("")
            s_sock.send(b_data)
            x = x + 1
    #msg = array.array('B', [data])
    #data = s_sock.recv(1)
    #print(data)
    
    s_sock.close()