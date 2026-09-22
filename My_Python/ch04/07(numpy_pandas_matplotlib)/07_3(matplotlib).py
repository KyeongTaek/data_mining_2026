"""
07. numpy, pandas, matplotlib
3) matplotlib

- 파이썬 및 numpy 라이브러리를 활용한 시각화 라이브러리.
- lines, bars, markers, images, contours, fields 등 제공.

"""
import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt

## 라인플롯 차트 그리기
# 1. 데이터 준비
x = [2016, 2017, 2018, 2019, 2020]
y = [350, 410, 520, 695, 543]

# 2. x축과 y축 데이터를 지정하여 라인플롯 생성
print(plt.plot(x, y))

# 3. 차트 제목 설정
print(plt.title('Annual sales'))

# 4. x축 레이블 설정(x축 이름)
print(plt.xlabel('years'))

# 5. y축 레이블 설정(y축 이름)
print(plt.ylabel('sales'))

# 6. 라인플롯 표
plt.show()

## 바차트 차트 그리기
# 1. 데이터 준비
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]

x = range(len(y1))

# 2. x축과 y축 데이터를 지정하여 바차트 생성
plt.bar(x, y1, width=0.7, color="blue") # bottom 없으니 바닥부터. width=0.7: 꽉 차지 않게.
plt.bar(x, y2, width=0.7, color="red", bottom=y1) # bottom(y1)부터.

# 3. 차트 제목 설정
plt.title('Quarterly sales')

# 4. x축 레이블 설정
plt.xlabel('Quarters')

# 5. y축 레이블 설정
plt.ylabel('Sales')

# 6. 눈금 이름 리스트 생성
xLabel = ['first', 'second', 'third', 'fourth']

# 7. 바 차트의 x축 눈금 이름 설정
plt.xticks(x, xLabel, fontsize=10)

# 8. 범례 설정
plt.legend(['chairs', 'desks'])

# 9. 바 차트 표시
plt.show()
