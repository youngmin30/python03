# 148 파일 이름 바꾸기 os.rename

from os import rename

target_file = 'stockcode.txt'
newname = input('[%s]에 대한 새로운 파일이름을 입력하세요.' % target_file)
rename(target_file, newname)
print('[%s]로 파일이름이 변경되었습니다.' %(target_file, newname))

# os 모듈이 rename() 파일 이름을 변경함.
# rename()은 이름을 변경하고자 하는 대상 파일의 상대 경로나 절대 경로를 인자로 받음.
# os 모듈의 rename()을 임포트함.
# 이름을 변경할 대상 파일을 저장함.
# imput()을 이용해 사용자로부터 새로운 파일이름을 입력 받음
# rename()으로 대상 파일의 이름을 변경함. 이미 존재하는 파일이름으로 변경하려고 하면 다음과 같이 FileExistsError가 발생함.

# FileExistsError:[WinError 183] 파일이 이미 있으므로 만들 수 없습니다.
# 오류없이 제대로 수행되었따면 대상 파일의 이름이 변경되었는지 확인함.

