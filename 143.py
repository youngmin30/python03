# 143

bufsize = 1024
f = open('img_sample.jpg', 'rb')
h = open('img_sample_copy.jpg', 'wb') # 이미지 복사

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)

f.close()
h.close()