"""
04. 조건문과 반복문
2) 반복문
"""

# for문
test_list = ['one', 'two', 'three']
for i in test_list:
    x = i + '!'
    print(x)

number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# while문
i = 0
while i < 5:
    i += 1
    print('*' * i)

