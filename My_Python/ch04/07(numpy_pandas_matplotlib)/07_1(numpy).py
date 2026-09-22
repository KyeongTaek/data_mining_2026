"""
07. numpy, pandas, matplotlib
1) numpy

- 행렬이나 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 파이썬의 라이브러리.
- 데이터 구조 외에도, 수치 계산을 위해 효율적으로 구현된 기능을 제공함.

"""
import numpy as np # np로 축약해 쓰는 게 de facto(사실상 표준)
print(np.__version__)

ar1 = np.array([1, 2, 3, 4, 5]) # 1차원 np array
print(f'ar1: {ar1}, type: {type(ar1)}')

ar2 = np.array([[10, 20, 30], [40, 50, 60]]) # 2차원(2행 3열. 2x3)
print(ar2)

ar3 = np.arange(1, 11, 2) # open 방식이라, 11 포함x. 2씩 증가
print(ar3)

ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2)) # 1x6(1행 6열)을 3x2(3행 2열로)
print(ar4)

ar5 = np.zeros((2, 3)) # 2x3 크기만큼을 0으로 채움
print(ar5)

ar6 = ar2[0:2, 0:2] # 행은 0부터 1까지. 열은 0부터 1까지.
print(ar6)

ar7 = ar2[0, :] # 행은 0번 행만. 열은 열 전체.
print(ar7)

ar8 = ar1 + 10 # 각 원소에 10씩 더함
print(ar8)

print(ar1 + ar8)
print(ar1 - ar8)
print(ar1 * 2)
print(ar1 / 2)

ar9 = np.dot(ar2, ar4) # 곱함. (2x3)와 (3x2)를 곱해서 2x2가 됨.
print(ar9)
