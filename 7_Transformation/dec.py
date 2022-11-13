f = open('enc', 'r')

line = f.readline()

for i in range(len(line)):
    n = ord(line[i])
    c1 = chr(n & 0xff)
    c2 = chr(n >> 8)
    print(c2+c1, end='')

f.close()
