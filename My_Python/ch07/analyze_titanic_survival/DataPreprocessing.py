import pandas as pd
import seaborn as sns

def collect_data():
    import seaborn as sns
    
    titanic = sns.load_dataset("titanic") # dataframe 형태
    titanic.to_csv('./titanic.csv', index = False) # csv로 저장

def prepare_data():
    titanic = pd.read_csv('./titanic.csv', header = 0, engine = 'python')

    # 결측치를 체크합니다.
    print(titanic.isnull().sum()) # 피처마다 null 개수 카운팅. isnull은 각 데이터가 null이면 1을 반환하는데, sum은 열 방향으로 1의 합계를 더하니 각 열의 결측치 총합이 구해지는 것.

    # 결측치가 많네요. 결측치를 채워봅니다.    
    titanic['age'] = titanic['age'].fillna(titanic['age'].median()) # age의 중앙값(median)으로 빈칸을 채움(fillna)

    print(titanic['embark_town'].value_counts()) # embark_town의 각 속성값마다의 개수 파악(여기선 최빈값 파악 위함)
    titanic['embark_town'] = titanic['embark_town'].fillna('Southampton') # embark_town의 최빈값인 Southampton으로 빈칸을 채움

    print(titanic['deck'].value_counts()) # deck의 각 속성값마다 개수 파악(여기선 최빈값 파악 위함)
    titanic['deck'] = titanic['deck'].fillna('C') # deck의 최빈값으로 빈칸 채움

    print(titanic['embarked'].value_counts()) # embarked의 각 속성값마다의 개수 파악(여기선 최빈값 파악 위함)
    titanic['embarked'] = titanic['embarked'].fillna('S') # embarked의 최빈값으로 빈칸 채움
    
    # 결측치를 채운 후, 결측치를 다시 체크합니다.
    print(titanic.isnull().sum()) # 결측치가 없음

    titanic.to_csv('./titanic2.csv', index = False)
    
def exploratory_data_analysis():
    import matplotlib.pyplot as plt

    titanic = pd.read_csv('./titanic2.csv', header = 0, engine = 'python')

    # 1. 기본 정보 탐색하기
    print(titanic.info()) # 기본 정보 출력
    print(titanic['survived'].value_counts()) # survived 속성값 빈도 확인

    # 2. 차트를 그려 데이터를 시각적으로 탐색하기
    f, ax = plt.subplots(1, 2, figsize = (10, 5)) # 행렬의 크기는 1x2.

    # sol1. 연속인덱싱(임시 생존자 series를 만들고, 성별 조건 데이터를 대조하며 필터링) -> 연산 낭비, 수정 시 모호함으로 인한 에러
    # titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0, 0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)

    # sol2. loc을 이용함. 행을 먼저 필터링하고 원하는 열을 가져오기
    titanic.loc[titanic['sex'] == 'male', 'survived'].value_counts().plot.pie(explode = [0, 0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True) # 남성 중에서, survived 열 가져옴. 이에 대해 value_counts()로 각 속성값마다의 개수를 파악해 dataframe 반환.
    # dataframe에 대해 plot.pie로 파이차트 그림. explode로 생존자 파이를 살짝 돌출시키고, autopct로 소수점 아래 첫째자리까지 표현하면서 % 붙이고(ex. 63.7%) ax로 왼쪽에 배치하고 shadow로 그림자 효과를 줌.

    titanic.loc[titanic['sex'] == 'female', 'survived'].value_counts().plot.pie(explode = [0.1, 0], autopct = '%1.1f%%', ax = ax[1], shadow = False)

    ax[0].set_title('Survived (Male)')
    ax[1].set_title('Survived (Female)')

    plt.show()

    # 3. 등급별 생존자 수를 차트로 나타내기
    sns.countplot(x = 'pclass', hue = 'survived', data = titanic) # 히스토그램 형태. pclass의 유형을 x축으로. 종속 변수(hue)는 survived=0과 survived=1의 개수.
    plt.title('PClass vs Survived')
    plt.show() # pclass가 클수록 사망 높아짐(survived 작아짐) -> 음의 상관관계

if __name__ == '__main__':
    collect_data()
    prepare_data()
    exploratory_data_analysis()
