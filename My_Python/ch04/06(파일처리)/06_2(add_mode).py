"""
06. 파일 처리
2) 추가 모드
"""

# 추가 모드
f = open("c:/temp/새파일.txt", 'a')

for i in range(6, 11):
    data = "%d번째 줄 추가입니다. \n" % i
    f.write(data)
f.close()
