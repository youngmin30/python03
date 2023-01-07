# 142

f = open('stockcode.txt', 'r')
h = open('stockcode_copy.txt', 'w') # 복사본 만드는 것

data = f.read()
h.write(data)

f.close()
h.close()