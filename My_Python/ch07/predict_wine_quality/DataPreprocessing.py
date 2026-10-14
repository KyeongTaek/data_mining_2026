import pandas as pd

# 1. 데이터 준비
red_df = pd.read_csv('./winequality-red.csv', sep = ';', header = 0, engine = 'python') # 열 구분자가 세미콜론으로 되어 있으므로, 이를 기준으로 읽음
white_df = pd.read_csv('./winequality-white.csv', sep = ';', header = 0, engine = 'python')

red_df.to_csv('./winequality-red2.csv', index = False) # 열 구분자를 컴마로 바꿔서 저장
white_df.to_csv('./winequality-white2.csv', index = False)

# 2. 데이터 통합(Data Integration)
print(red_df.head())
red_df.insert(0, column = 'type_int', value = 0)
red_df.insert(0, column = 'type', value = 'red') # 구분 변수 추가
print(red_df.head())
print(red_df.shape)

print(white_df.head())
white_df.insert(0, column = 'type_int', value = 1)
white_df.insert(0, column = 'type', value = 'white') # 구분 변수 추가
print(white_df.head())
print(white_df.shape)

## 서로 컬럼의 종류와 개수가 같으니, 그대로 이어붙일 수 있음을 확인.
wine = pd.concat([red_df, white_df]) # 수직 형태로 연결(행 방향 결합)
print(wine.shape)

# 3. 데이터 탐색(Exploratory Data Analysis, EDA)
# 3-1. 기본 정보 확인
print(wine.info()) # 기본 정보 확인. non-null count로 누락치가 얼마나 되는지 확인할 수 있음. 각 컬럼의 타입을 확인할 수 있음.
## 누락치는 없으니 채우지 않고 바로 데이터를 사용할 수 있음을 확인.

wine.columns = wine.columns.str.replace(' ', '_') # 컬럼의 공백을 언더바로 바꿈. .str은 문자열화.
print(wine.head())

wine.to_csv('./wine.csv', index = False)

wine.describe() # 기술통계값 볼 수 있음.

print(sorted(wine['quality'].unique())) # 중복 제외한 고유값(품질) 추출. sorted()를 거치면서, 정렬되어 실제 타입 출력.
## 품질 등급은 3, 4, 5, 6, 7, 8, 9로 7개 등급이 있음을 확인.

print(wine['quality'].value_counts()) # quality값마다 데이터 몇 개 있는지 빈도수 출력.
## 6등급인 샘플이 2826개로 가장 많고, 9등급인 샘플이 5개로 가장 적은 것을 확인. 등급 순서대로 나열할 때 정규분포와 비슷한 형태를 보임을 확인.

wine_split_group = wine.groupby('type') # type을 기준으로 데이터를 쪼개 계산할 준비를 마침
print(type(wine_split_group)) # DataFrameGroupBy 객체. 이후 집계함수(.mean(), .sum(), .describe())를 붙일 때 DataFrame(혹은 Series)가 됨.

print(wine_split_group['quality'].describe()) # type별로 품질에 대한 기술 통계.
print(wine_split_group['quality'].std()) # type별로 품질에 대한 표준편차만 따로 구함.
print(wine_split_group['quality'].agg(['mean', 'std'])) # type별로 품질에 대해 mean, std만 따로 구함.
print(wine_split_group['quality'].agg(['median', 'prod', 'sum', 'var'])) # type별로 품질에 대해 중앙값, 모든값의 곱, 모든값의 합, 분산만 따로 구함(값 중 inf는 오버플로우)

# 3-2. t-검정
# type이 품질에 영향을 미치는 요인인지 확인하려면, 통계적으로 유의미한 차이가 있는지 확인해야 함.
# 차이가 명확하다면 type별로 개별 모델을 만들거나, 통합 모델 만들더라도 독립 변수에 포함시킬 수 있음.
# 차이가 없다면, 전체를 합쳐서 학습해 성능을 높임.
# 3-1만으로는 통계적으로 유의미한 차이 있다고 볼 수 없음(두 범주형 집단 간 수치형 평균 차이를 비교하는 t-검정 필요).
# 참고로, 나머지 연속형 변수들이 품질에 미치는 영향은 OLS 내의 t-검정 및 회귀계수를 통해 유의성을 한꺼번에 검정함.

# t-검정을 위해서는 scipy 패키지가 필요함.
# scipy 패키지 설치 시, 파이썬 버전을 지정하는 방식은
# sol1) py -3.12 -m pip install scipy
# sol2) native python이 설치된 경로에서 pip install scipy

from scipy import stats

red_wine_quality = wine.loc[wine['type'] == 'red', 'quality'] # red의 품질을 뽑음(조건에 맞는 행에서 특정 컬럼 선택)
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality'] # white의 품질을 뽑음

print(stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)) # 두 독립된 표본 집단(red와 white)의 평균에 대한 독립표본 t-검정 수행.
## statistic의 값이 t-value. 이때 수식에서 X2 평균이 더 크면 음수도 가능(X1과 X2를 바꾸면 부호 바뀜). 여기서 중요한 건 값의 크기.
## pvalue의 값이 t-value를 기반으로 산정한 p-value. 이때 0.05보다 작으므로, 두 집단(red, white) 간에 유의미한 차이가 있음을 확인.
