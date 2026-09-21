"""
03. 자료형과 연산자
3) 그룹 자료형 - 리스트
"""
## 그룹 자료형: 문자열, 리스트, 튜플, 딕셔너리, 집합

# 2) 리스트 자료형
# 인덱스 사용 가능. 원소값 변경 가능(mutable)
a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']] # 다른 타입 가능
print(d[0]) # 인덱스 접근 가능.
print(d[2])
print(d[3])
print(d[3][-1])
print(d[0:3])
print(a+b)
print(b[0] + "hi ~ ^^;")
# print(a[0] + "hi ~ ^^;") # error. int-str 간 +연산자 오버로딩 안되어 있음.

print(a * 3) # 오버로딩(정수 크기만큼 얕은 복사해서 이어붙여라)
a[2] = 99 # 수정 가능. list는 mutable(변경가능)이기 때문에.
print(a)

a[1:2] = ['a', 'b', 'c'] # 범위를 주었기 때문에, 언패킹해서 1번째에 'a', 'b', 'c'를 넣음
print(a)
a[-1] = ['d', 'e', 'f'] # 단일 인덱스를 주었기 때문에, 객체 자체를 맨 뒤에 넣음
print(a)

del a[-1] # 삭제 내장 명령어
print(a)

a.append(5)
print(a)

b.sort() # 리스트를 직접 수정(사전 순서. 대문자는 소문자보다 앞섬). 반환값은 None.
print(b)

c = sorted(b, reverse=True) # 원본은 유지하고, 새로운 리스트를 반환(reverse=True로 역순)
print(b)
print(c)

a = [3, 4, 1, 9]
a.reverse()
print(a)

print(a.index(9)) # 지정한 값이 저장된 인덱스 확인

a.insert(0, 99)
print(a)

a.remove(99) # 지정한 값을 삭제
print(a)

b = [1, 2, 3]
print(b.pop()) # 뒤에서 꺼낸다(LIFO/FILO) --> 즉 stack
print(b)

print(b.pop(0)) # 앞에서 꺼낸다 --> 즉 queue
print(b)

a = [65, 1, 0, 65, 3, 65, 4, 65, 'A']
print(a.count(65)) # 지정한 값이 몇 개 있는지 확인(타입까지 확인 --> 'A'(아스키코드 65)는 제외하여 4 출력)
