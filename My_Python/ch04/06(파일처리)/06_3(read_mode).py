"""
06. 파일 처리
3) 읽기 모드
"""

# 1. readline() 활용 예시
f = open("c:/temp/새파일.txt", 'r')
line= f.readline() # '\n'까지 입력 받음
print(line) # 결과적으로 엔터가 두번 쳐지는 셈

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 1-1. readline()에 rstrip() 함수를 사용해 \n을 제외하고 사용하는 예시
f = open("c:/temp/새파일.txt", 'r')
line = f.readline().rstrip('\n') # '\n'까지 입력 받고, '\n'은 제거
print(line)

while True:
    line = f.readline().rstrip('\n')
    if not line: break
    print(line)
f.close()

# 2. readlines() 활용 예시
f = open("c:/temp/새파일.txt", 'r')
lines = f.readlines() # 파일 전체 입력 받아, 각 라인을 리스트의 원소로 만듦.
print(lines)

for line in lines:
    print(line)
f.close()

# 3. read() 활용 예시
f = open("c:/temp/새파일.txt", 'r')
data = f.read() # 파일 전체 입력 받아, 하나의 문자열로 만듦.
print(f'data의 타입: {type(data)}')
print(data)

f.close()

# 4. with open 활용 예시(단락이 끝나면 자동으로 닫힘)
with open("c:/temp/새파일.txt", 'w') as f:
    f.write("Now is better than never.")

# data = f.read() # error. 파일이 이미 닫혔기 때문
