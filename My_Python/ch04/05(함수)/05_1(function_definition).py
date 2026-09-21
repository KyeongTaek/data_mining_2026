"""
05. 함수
1) 사용자 정의 함수
"""

def sum1(a, b):
    x = a + b
    return x

def sum2(*args): # 인자가 리스트(가변인자)
    x = 0
    for i in args:
        x += i
    return x

a = 5
b = 3
print(sum1(a, b))
print(sum1(3, 5))
print(sum2(1, 2, 3, 4, 5))
print(sum2(2, 3.5, 10))
