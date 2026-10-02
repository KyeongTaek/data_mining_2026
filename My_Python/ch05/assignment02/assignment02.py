import openapi_tour as tour
import matplotlib.pyplot as plt
import sys

# 폰트 설정
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

def getTourStatResult():
    jsonResult = []
    result = []

    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) :') # str.
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? :'))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? :'))
    ed_cd = "E" # E: 방한외래관광객(입국), D: 해외 출국

    jsonResult, results, natName, ed, dataEND = tour.getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)

    if jsonResult == []: # api 에러나 연도 범위 오류의 경우
        return None, None, None # None을 반환

    return nStartYear, natName, results


# Figure: 전체 캔버스. Axes: 그래프가 그려지는 하나의  구역. Axis: x축과 y축
# 명시적이고, 객체지향 기반인 Axes 방식을 사용

fig, ax = plt.subplots() # Figure(전체 캔버스)와 Axes(그래프 영역 1개) 반환.

start_year, natName, results = getTourStatResult()

if results is not None:
    numbers = [result[3] for result in results] # 관광객수(index=3)만 모음
else:
    print('데이터가 비어 있습니다.')
    sys.exit()

length = len(results)
month = 1
columns = []
while length > 0:
    columns.append("{0}{1:0>2}".format(str(start_year), str(month))) # '202601'식의 월 정보를 담아, x축 라벨로 만듦
    length -= 1
    month += 1
    if month == 13: # 12월에서 다음으로 넘어갈 때
        month = 1 # 1월로 설정하고
        start_year += 1 # 해를 다음해로 설정함

# columns(라벨)를 x축으로 하고, numbers(관광객수)를 y축으로 하는 라인차트를 그림.
ax.plot(columns, numbers, 'ro-', label=natName) # 빨간색(r) 원형마커(o) 실선(-). legend는 국가 이름으로 설정(라벨만 달아둘 뿐, 아직 화면에 그리지 X)

# 다양한 속성을 한번에 설정함.
ax.set(xlabel='입국연월', ylabel='입국자수', title='입국연월별 국가별 입국자 수') # x축, y축, 그래프 제목

ax.tick_params(axis='x', labelrotation=90) # xtick(x축 눈금) 라벨을 반시계로 90도 돌림(수직)

ax.grid() # 가시성을 위해, 그래프 내부에 격자 추가
ax.legend() # 라벨(legend)이 달린 그래프 선을 찾아 범례 상자를 그래프 위에 띄움

plt.show() # 모든 Figure를 표시한다.
