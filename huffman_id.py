#!/usr/bin/env python
#coding:utf-8
class Huffman:
    def __init__(self):
        self.tree = None
        self.pattern = None
        self.encode_dict = {}
        self.decode_dict = {}

    def encode(self, data):
        unique_data = set(data)
        nodes = []

        for v in unique_data:
            node_obj = Node(value=v, count=data.count(v))
            nodes.append(node_obj)
        temp = []
        while len(nodes) >= 2:
            for v in range(2):
                elem = min(nodes, key=lambda x: x.count)
                temp.append(elem)
                nodes.remove(elem)
            n = Node(value=None, count=temp[0].count+temp[1].count, left=temp[0], right=temp[1])
            temp = []
            nodes.append(n)
        self.tree = nodes[0]
        self.recursive_code(self.tree, "")
        s = ""
        for v in data:
            s += self.encode_dict[v]
        return s

    def recursive_code(self, node, s): #圧縮結果を取得する
        if not isinstance(node, Node):
            return
        if node.value:
            id = node.value
            id = id.replace("\n", "")
            id = id.replace("\r", "")
            id = id.replace("\r\n", "")
            id_bin = s
            #if id_bin[0] == "0":
            #    id_bin = "1" + id_bin
            print("{} {}".format(id,id_bin), file=w)
            self.encode_dict[node.value] = s
            self.decode_dict[s] = node.value
            return
        self.recursive_code(node.right, s+"1")
        self.recursive_code(node.left, s+"0")
    def decode(self, data):
        assert(self.decode_dict)
        result = ""
        s = ""
        for bit in data:
            s += bit
            if s in self.decode_dict:
                result += self.decode_dict[s]
                s = ""
        return result


class Node: #葉を表すクラス
    def __init__(self, value=None, count=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.count = count

input = "yuki_1230s_id.csv"
output = "huffman_id.csv"
f = open(input)
w = open(output, mode="w")
data = f.readlines()
h = Huffman()
x = h.encode(data)
#print(x)
d = h.decode(x)
#print("decoded:", d)
f.close()
w.close()