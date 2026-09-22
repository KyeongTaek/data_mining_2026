"""
06. 파일 처리
1) 쓰기 모드
"""

# 쓰기 모드
f = open("c:/temp/새파일.txt", 'w')
print(f)

for i in range(1, 6):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

