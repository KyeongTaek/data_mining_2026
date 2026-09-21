"""
03. 자료형과 연산자
"""


## 기본 자료형
# 1) 숫자형
a = 123
a = 12.34
a = 1 + 2j
print(a.real) # 실수부(멤버변수)
print(a.imag) # 허수부(멤버변수)
print(a.conjugate()) # 켤레복소수(멤버함수)
print(abs(a)) # 절대값 반환(복소수의 경우, 그 크기)

a = 0o12
print(a)
a = 0x12A
print(a)

# 2) 논리형
b = True
print(b)

# 3) 사용 가능 연산자
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(2 ** 3)
print(a % b) # 나머지
print(7 % 3)
print(a // b) # 몫
print(7 // 3)
