# 138 .

f = open('stockcode.txt', 'r') # 'r' 읽기 모드로 열기
line_num = 1 # 줄 번호
line = f.readline() # 한 줄 읽고, 'line'에 넣기
while line: # line이 빈 칸일 때까지, while 루프 반복
    print('%d %s' % (line_num, line), end='') # %d와 %s에 line_num 넣고, 출력하는 루프
    line = f.readline() # 한 줄씩 읽기
    line_num += 1 # 줄 번호를 1씩 올리기
f.close()