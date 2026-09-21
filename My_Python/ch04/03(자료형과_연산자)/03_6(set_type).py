"""
03. 자료형과 연산자
6) 그룹 자료형 - 집합
"""
## 그룹 자료형: 문자열, 리스트, 튜플, 딕셔너리, 집합

# 5) 집합(set): 중복 없이 유일해야 함. 인덱스 사용 불가능
# 인덱스 사용 불가능(unordered). 원소값 변경 가능(mutable)
s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2)
s3 = set([4, 5, 6, 7, 8, 9])
print(s3)

print(s2 & s3) # 교집합
print(s2.intersection(s3)) # 교집합

print(s2 | s3) # 합집합(기존 set 바꾸지 않고, 합친 새 set 반환)
print(s2.union(s3)) # 합집합

print(s2 - s3) # 차집합
print(s2.difference(s3)) # 차집합
print(s3.difference(s2)) # 차집합(A-B랑 B-A는 다르다)

s2.add(7) # 기존 set에 값 1개 추가
# s2.add([6, 7]) # error. 변경 가능한(mutable) 리스트는 set에 담을 수 없음(unhashable type 에러)
print(s2)

s2.update([6, 7, 8, 9, 10]) # 기존 set에 여러 개의 값(반복 가능한 객체)을 언패킹해서 한 번에 추가
print(s2)

s2.remove(7) # 기존 set에서 값 1개 제거
print(s2)
