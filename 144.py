# 144

with open('stockcode.txt', 'r') as f:
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1, line), end='')


f = open('stockcode.txt', 'r') # withopen('stockcode.'txt', 'r') as f:
... 파일 처리 코드 ...
f.close()