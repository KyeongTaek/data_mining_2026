"""
03. 자료형과 연산자
5) 그룹 자료형 - 딕셔너리
"""
## 그룹 자료형: 문자열, 리스트, 튜플, 딕셔너리, 집합

# 4) 딕셔너리: 'key:value'처럼 쌍의 형태로 이루어짐(타입은 뭐든지 가능)
# 인덱스 사용 불가능(unordered). 원소값 변경 가능(mutable)
dic = {'name': 'Hong', 'phone': '01012345678', 'birth': '0814'}
dic[1] = 'a' # 이때 1이 key, 'a'가 value.
print(dic)
dic['pet'] = 'dog'
print(dic)
del dic[1] # 특정 key 삭제
print(dic)

print(dic['pet'])
print(dic['name'])
print(dic.keys()) # key들만 출력
print(type(dic.keys())) # 타입은 dict_keys
print(list(dic.keys())) # list화
print(type(list(dic.keys())))

print(dic.values()) # value들만 출력
print(list(dic.values())) # list화

print(dic.items()) # 저장된 거 보여줌
print(type(dic.items())) # 타입은 dict_items

dic.clear() # 모든 key와 value를 지워 빈 상태로 만듦
print(dic)
