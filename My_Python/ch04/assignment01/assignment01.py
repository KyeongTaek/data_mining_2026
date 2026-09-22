"""
Assignment01
작성자: 2021040032 임경택
"""

import matplotlib.pyplot as plt

## 과제1-2: Bar 차트에서 3개의 데이터를 누적해서 표현하는 방법
# 1. 데이터 준비
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]

x = ['first', 'second', 'third', 'fourth'] # 라벨 미리 설정

# 2. x축과 y축 데이터를 지정하여 바차트 생성
plt.bar(x, y1, width=0.7, color="blue")
plt.bar(x, y2, width=0.7, color="red", bottom=y1)
plt.bar(x, y3, width=0.7, color="green", bottom=[y1[i]+y2[i] for i in range(0,4)])

# 3. 차트 제목 설정
plt.title('Quarterly sales')

# 4. x축 레이블 설정
plt.xlabel('Quarters')

# 5. y축 레이블 설정
plt.ylabel('sales')

# 6. 범례 설정
plt.legend(['chairs', 'desks', 'goods'])

# 7. 바 차트 표시
plt.show()

## 과제1-3: matplotlib.org을 참고하여 추가적 데이터 가시화
# Scatter plot with histograms 예제 코드

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data source: https://www.kaggle.com/datasets/raphaelmanayon/temperature-and-ice-cream-sales?resource=download
df = pd.read_csv('../07(numpy_pandas_matplotlib)/temp_sales.csv', encoding='utf-8', engine='python')

x = df['Temperature']
y = df['Ice Cream Profits']

# 중첩 리스트를 받아, 각 영역의 이름을 배치. {레이블이름: Axes 객체} 반환.
fig, axs = plt.subplot_mosaic([['histx', '.'], # histx 요소는 위쪽을 넓게 씀
                               ['scatter', 'histy']], # scatter 요소와 histy 요소는 아래쪽 전체를 씀. 왼쪽엔 scatter 요소, 오른쪽엔 histy요소가 배치됨.
                              figsize=(6, 6),
                              width_ratios=(4, 1), height_ratios=(1, 4), # 가로는 scatter가 4, histy가 1의 비율. 높이는 histx가 1, scatter가 4의 비율.
                              layout='constrained') # 그래프 요소가 서로 겹치지 않도록 크기 자동 조절

axs['scatter'].scatter(x, y) # scatter 요소에 scatter plot 그림.

bins_x = np.linspace(x.min(), x.max(), 11) # 온도의 최소값부터 최대값까지 11개의 균등한 간격의 숫자를 생성해 1차원 배열 반환.
bins_y = np.linspace(y.min(), y.max(), 11) # 이윤의 최소값부터 최대값까지 11개의 균등한 간격의 숫자를 생성해 1차원 배열 반환.
                                                    
axs['histx'].hist(x, bins=bins_x) # histx 요소에 온도 히스토그램 그림.
axs['histy'].hist(y, bins=bins_y, orientation='horizontal') # histy 요소에 이윤 히스토그램 그림(막대가 수평).

plt.show()


