"""
04. 조건문과 반복문
1) 조건문
"""
x = 3
y = 2
print(x == y)
print(x != y)
print(x >= y)

money = 1300
if money >= 1200 and money < 3500:
    print("버스를 탈 수 있습니다.")

print(1 in [1, 2, 3])
print(x in [1, 2, 3])
print(x not in [1, 2, 3])
print('a' in ('a', 'b', 'c', 'd'))
print('i' not in 'Python')

if money < 10:
    pass
else:
    print("저금하자!")
