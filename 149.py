# 149 파일을 다른 디렉터리로 이동하기 os.rename
# rename() - 특정 파일을 다른 디렉터리로 이동하려면 rename()의 인자로 대상 파일이름을 포함하여 이동할 절대 경로를 입력함.
# stockcode.txt 사용자가 입력한 코드를 디렉터리로 이동하는 코드


from os import rename # os 모듈: rename() 임포트

target_file = 'stockcode.txt' # # 이동할 파일 지정
newpath = input('[%s]를 이동할 디렉터리의 절대경로를 입력하세요.:' % target_file) # input()을 이용해 사용자로부터 이동할 디렉터리의 절대경로를 입력받음. newpath로 둔다.

if newpath[-1] == '/':
    newname = newpath + target_file
else:
    newname = newpath +'/' + target_file

try:
    rename(target_file, newname)
    print('[%s] -> [%s]로 이동되었습니다.' %(target_file, newname))
except FileNotFoundError as e:
    print(e)