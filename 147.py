# 147

from os import remove

target_file = 'stococode_copy.txt'
k = input('[%s] 파일을 삭제하시겠습니까? (y/n)' % target_file)
if k == 'y':
    remove(target_file)
    print('[%s]를 삭제했습니다.' % target_file)