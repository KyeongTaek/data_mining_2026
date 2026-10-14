import pandas as pd
from statsmodels.formula.api import ols, glm # ols: 다중 선형 회귀 분석

# 4. 데이터 모델링

# 4-1. 회귀 분석
wine = pd.read_csv('./wine.csv', header = 0, engine = 'python')

Rformula_origin = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol' # 11개의 독립변수를 선형결합(각 weight와 곱해짐)하여 종속변수 예측하는 회귀식
origin_result = ols(Rformula_origin, data = wine).fit() # 다중 선형 회귀 분석 방식으로 학습 시켜라

print(origin_result.summary()) # 학습된 정보 출력

Rformula_type = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol + type_int' # type을 포함해 12개의 독립변수를 선형결합하여 종속변수 예측하는 회귀식
type_result = ols(Rformula_type, data = wine).fit()

print(type_result.summary())

# 4-2. 학습에 썼던 데이터에 대해 예측(의미X)
sample1 = wine[wine.columns.difference(['quality', 'type', 'type_int'])] # 품질, 타입(숫자 형태 포함) 제외
sample1 = sample1.iloc[0:5] # 5x11
sample1_predict = origin_result.predict(sample1) # 예측(5x1)
print(sample1_predict) # y-hat
print(wine[0:5]['quality']) # y

# 4-3. 새 데이터에 대해 예측
data = {
    "fixed_acidity": [8.5, 8.1],
    "volatile_acidity": [0.8, 0.5],
    "citric_acid": [0.3, 0.4],
    "residual_sugar": [6.1, 5.8],
    "chlorides": [0.055, 0.04],
    "free_sulfur_dioxide": [30.0, 31.0],
    "total_sulfur_dioxide": [98.0, 99],
    "density": [0.996, 0.91],
    "pH": [3.25, 3.01],
    "sulphates": [0.4, 0.35],
    "alcohol": [9.0, 0.88]
}
sample2 = pd.DataFrame(data, columns = sample1.columns)
print(sample2)
sample2_predict = origin_result.predict(sample2)
print(sample2_predict) # y-hat(정답은 없음)

