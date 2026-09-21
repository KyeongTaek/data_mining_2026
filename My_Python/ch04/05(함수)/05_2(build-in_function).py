"""
05. 함수
2) 내장 함수
"""

print(abs(-3.5)) # 절댓값
print(all([1, 2, 3, 4])) # 모두 True(0 아닌 값)면 True
print(any([4, -2, 0.0, 4])) # 하나라도 True(0 아닌 값)면 True

print(chr(97)) # ascii -> str. 97 -> 'a'. 48 -> '0'.
print(ord('a')) # str -> ascii. 'a' -> 97. '0' -> 48.

print(dir([1, 2, 3])) # 전달된 객체가 사용할 수 있는 속성과 메서드 목록을 오름차순 정렬해 반환
print(dir()) # 현재 네임스페이스에 정의된 변수, 모듈, 함수 등의 이름 목록 반환

print(divmod(7, 3)) # 몫, 나머지를 묶은 튜플 반환
print(type(divmod(7, 3)))

print(oct(8)) # 10진수 -> 8진수. 0o10
print(hex(16)) # 10진수 -> 16진수. 0x10

a = 3
print(id(a)) # 객체 고유값을 얻을 수 있음

print(int('3')) # str -> int
print(str(3)) # int -> str

print(list("Python")) # str -> list
print(list((1, 2, 3))) # tuple -> list

print(tuple("Python")) # str -> tuple
print(tuple([1, 2, 3])) # list -> tuple

print(type("abc")) # 타입 출력


def sum1(a: int, b: int) -> int:
    return a + b

sum2 = lambda a,b: a+b # 이름 없이 일회성으로 쓰기 좋은 익명 함수
print(sum1) # function sum1
print(type(sum1)) # type: function
print(sum2) # function lambda
print(type(sum2)) # type: function

print(sum1(3, 5))
print(sum2(3, 5))

print(max([1, 4, 2, 8, 6]))
print(min([1, 4, 2, 8, 6]))

print(pow(2, 4))

c = input("정수를 입력하세요: ")
print(type(c))
try:
    print("your input is %d" %int(c))
except ValueError:
    print("정수를 입력하지 않았습니다")

print(range(5))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))
print(len('Python'))
print(sorted([3, 0, 2, 1])) # 정렬된 새로운 리스트 반환

