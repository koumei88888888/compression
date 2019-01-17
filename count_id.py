#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open('yuki_1230s_id.csv')
data = f.read()
output = 'id_num.txt'
w = open(output, mode='w')

# counting
words = {}
for word in data.split():
    words[word] = words.get(word, 0) + 1

# sort by count
d = [(v,k) for k,v in words.items()]
d.sort()
d.reverse()
for count, word in d:
    print(word,count, file = w)
f.close()
w.close()