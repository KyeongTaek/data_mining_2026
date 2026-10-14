import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# 5. 결과 시각화

# 5-1. 와인 유형에 따른 품질 등급 히스토그램
wine = pd.read_csv('./wine.csv', header = 0, engine = 'python')
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']

sns.set_style('ticks') # 배경 없고, 눈금만 있음.
sns.histplot(red_wine_quality, kde = True, color = "red", label = 'red wine') # kde: 확률밀도함수. 각 값이 몇 퍼센트 차지하는지(sum은 1)
sns.histplot(white_wine_quality, kde = True, label = 'white wine')

plt.title("Quality of Wine Type")
plt.legend() # 범례

plt.show()

# 5-2. 부분 회귀 플롯으로 시각화
import statsmodels.api as sm
wine.drop(columns = ['type_int', 'type'], inplace = True) # type_int 컬럼 임시 제거
others = list(set(wine.columns).difference(set(["quality", "fixed_acidity"]))) # 컬럼 집합에서 quality, fixed_acidity 제거한 것들을 others로 지정

p, resids = sm.graphics.plot_partregress("quality", "fixed_acidity", others, data = wine, ret_coords = True) # quality, fixed_acidity에 대해 부분회귀 플롯 그림(others는 고정해서 영향 배제).
plt.show() # fixed_acidity가 quality에 미치는 영향력 시각화

# 5-3. 각 독립 변수가 quality에 미치는 영향력 시각화
from statsmodels.formula.api import ols
Rformula_origin = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'

origin_result = ols(Rformula_origin, data = wine).fit()

fig = plt.figure(figsize = (8, 13)) # 차트 크기 지정
sm.graphics.plot_partregress_grid(origin_result, fig = fig) # 내부: 잔차 y*(종속), 잔차 xk*(독립)를 구해 선형 회귀분석(y* = bkxk* + u)해서 플로팅
plt.show()
