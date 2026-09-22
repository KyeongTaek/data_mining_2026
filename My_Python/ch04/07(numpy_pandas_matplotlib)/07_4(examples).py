"""
07. numpy, pandas, matplotlib
4) matplotlib examples
"""
import matplotlib
import matplotlib.pyplot as plt

## 바 바트 예제 코드
# 1. 데이터 준비
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
y3 = [200, 250, 385, 350]

x = range(len(y1))

bottom1 = [x+y for x,y in zip(y1, y2)]

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

# 6. 눈금 이름 리스트 생성
xLabel = ['first', 'second', 'third', 'fourth']

# 7. 바 차트의 x축 눈금 이름 설정
plt.xticks(x, xLabel, fontsize=10)

# 8. 범례 설정
plt.legend(['chairs', 'desks', 'goods'])

# 9. 바 차트 표시
plt.show()

## 바코드 예제 코드
import matplotlib.pyplot as plt
import numpy as np

code = np.array([
    1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi = 100

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi = dpi) # code 길이가 늘어나도, 막대 1개당 4픽셀을 유지해줌.
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 상하좌우 폭
ax.set_axis_off() # 축 제거
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto', interpolation='nearest')
plt.show()

## Scatter plot with histograms 예제 코드

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## data source: https://www.kaggle.com/datasets/raphaelmanayon/temperature-and-ice-cream-sales?resource=download
df = pd.read_csv('./temp_sales.csv', encoding='utf-8', engine='python')

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
#def qrcode_generation_wrong():
#    ## qr코드 예제 코드(https://snu-eng.kr/html/2108/s0201.html 참고)
#    import matplotlib.pyplot as plt
#    import numpy as np
#
#    # size는 21x21
#    code = np.zeros((21, 21))
#    restricted = np.zeros((21, 21))
#
#    ## 위치 검출 패턴
#    # 오른쪽 아래를 제외한 귀퉁이는 7x7. 테두리가 검정색이고, 그 안의 5x5 테두리가 하얀색이고, 그 안의 3x3이 검정색.
#    restricted[0:7, 0:7] = 1
#    restricted[0:7, 14:] = 1
#    restricted[14:, 0:7] = 1

#    code[0:7, 0:7] = 1
#    code[0:7, 14:] = 1
#    code[14:, 0:7] = 1

#    code[1:6, 1:6] = 0
#    code[1:6, 15:20] = 0
#    code[15:20, 1:6] = 0
#
#    code[2:5, 2:5] = 1
#    code[2:5, 16:19] = 1
#    code[16:19, 2:5] = 1
#
#    ## 타이밍 패턴
#    # (8,6)부터 아래로 2칸씩. (6,8)부터 오른쪽으로 2칸씩.
#    restricted[8:13, 6] = 1
#    restricted[6, 8:13] = 1
#
#    code[8:13:2, 6] = 1
#    code[6, 8:13:2] = 1
#
#    ## 빈 공간
#    # 오른쪽 아래를 제외한 귀퉁이를 둘러싸는 부분은 빈 공간.
#    restricted[7, 0:8] = 1 # 1번 빈공간(순서: 왼->오, 위->아래)
#    restricted[0:8, 7] = 1 # 2번 빈공간
#
#    restricted[0:8, 13] = 1 # 3번 빈공간
#    restricted[7, 13:] = 1 # 4번 빈공간
#
#    restricted[13, 0:8] = 1 # 5번 빈공간
#    restricted[13:, 7] = 1 # 6번 빈공간
#
#    code[7, 0:8] = 0 # 1번 빈공간(순서: 왼->오, 위->아래)
#    code[0:8, 7] = 0 # 2번 빈공간
#
#    code[0:8, 13] = 0 # 3번 빈공간
#    code[7, 13:] = 0 # 4번 빈공간
#
#    code[13, 0:8] = 0 # 5번 빈공간
#    code[13:, 7] = 0 # 6번 빈공간
#
#    ## 포맷 정보(마스킹 패턴 가리키는 배열)
#    code[8, 2] = 1
#    code[8, 3] = 0
#    code[8, 4] = 1
#
#    code[16, 8] = 1
#    code[17, 8] = 0
#    code[18, 8] = 1
#
#    ## 인코딩
#    target = "https://github.com/Pachyhead/capstone_design_2026"
#    size = len(target)
#
#    binary_list = format(size, '08b')
#
#    for i in range(0, size-1, 2):
#        binary_list += format(ord(target[i])*45+ord(target[i+1]), '08b')
#
#    code[20][20] = 0
#    code[20][19] = 1
#    code[19][20] = 0
#    code[19][19] = 0
#    idx = 0
#    for i in range(20, , -2):
#        for j in range(20, , -1):
#            if restricted[j][i] == 0:
#                code[j][i] = binary_list[idx++]
#                code[j][i-1] = binary_list[idx++]        
#
#    ## 마스킹 패턴 정의
#    mask = np.zeros((21, 21))
#    mask[::2, ::2] = 1
#
#    mask[0:9, 0:9] = 0
#    mask[0:9, 13:] = 0
#    mask[13:, 0:9] = 0
#
#    mask[:, 6] = 0
#    mask[6, :] = 0
#
#    ## 마스킹 진행
#    for i in range(21):
#        for j in range(21):
#            if restricted[i][j] == 0:
#                if code[i][j] != mask[i][j]:
#                    code[i][j] = 1
#                else:
#                    code[i][j] = 0












