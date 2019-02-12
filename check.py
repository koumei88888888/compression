if __name__ == '__main__':
    w = open("memo.txt", "w")
    flag = 0
    for line in data:
        if flag == 0:
            ch = line
        else:
            ch += line
        flag = 1
    x = 0
    print(len(ch), file=w)
    while(True):
        if (len(ch)-8*x)/8 > 1:
            cch = ch[8*x:8*(x+1)]
            print(cch, file=w)
        else:
            print(len(ch)%8, file=w)
            break
        x = x + 1
    w.close()