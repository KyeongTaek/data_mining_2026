"""
03. 자료형과 연산자
2) 그룹 자료형 - 문자열
"""
## 그룹 자료형: 문자열, 리스트, 튜플, 딕셔너리, 집합

# 1) 문자열: 한 개 이상의 문자로 구성된 문제 집합. 작은따옴표나 큰 따옴표 사용해 나타냄(페어는 맞춰야겠지)
# 인덱스 사용 가능. 원소값 변경은 불가능(immutable)

s1 = 'Hello Python'
print(s1)
s2 = "Hello Python"
print(s2)
s3 = '''Hello Python'''
print(s3)
s4 = """Hello Python"""
print(s4)

# 1-2) 사용 가능 연산자
head = "Python"
tail = " is fun"
print(head + tail) # 오버로딩
print(head * 2)
print("=" * 5)

a = 'Now is better than never'
print(a[0]) # 인덱스를 이용하여 지정 가능
print(a[-1]) # 맨 뒤
print(a[3:6]) # 범위를 이용하여 내부 문자열 지정(슬라이싱). 이때 open 방식의 인덱스 표기를 사용하기에, [3], [4], [5]까지 해당.

b = a[0] + a[1] + a[2]
print(b)
print(a[0:3])
print(a[4:6])
print(a[19:]) # 19부터 끝
print(a[:3])
print(a[:]) # 전체
print(a[7:-11])

a = "Python" # 문자열 객체
print(a.count('p')) # 대소문자 구별 -> 없으므로 0
print(a.find('y'))
print(a.find('p'))
print(a.index('y'))
# print(a.index('p')) # error. 없는 문자이기 때문

b = ","
c = b.join('Abcd') # 리스트의 각 요소 사이에 지정한 구분자를 넣어 연결
print(c)

b = ",."
c = b.join('Abcd')
print(c)

a.upper()
a.lower()

d = " py"
print(d.lstrip()) # 왼쪽 공백 제거
print(d.rstrip()) # 오른쪽 공백 제거
print(d.strip()) # 양쪽 공백 제거

a = "pithon"
# a[1] = 'y' # error. c언어는 가능할지 몰라도, 여기는 immutable(변경불가) 에러

a = "Python is difficult."
print(a.replace("difficult", "funny")) # 대체
print(a.split()) # 공백 기준으로 분리

b = "a, b, c, d"
print(b)
print(b.split(',')) # 컴마 기준으로 분리
