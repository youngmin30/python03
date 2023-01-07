# 139

f = open('stockcode.txt', 'r')
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('%d %s' % (line_num+1, line), end='') # end=''의 역할? 다음 줄을 입력할 때 빈 공간 제거
f.close()