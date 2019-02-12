# -*- coding: utf-8 -*-
a = b'@'
print(a)
a = int.from_bytes(a, 'big')
print(a)
a = bin(a)
print(a)
a = a.replace('0b', '')
print(a)