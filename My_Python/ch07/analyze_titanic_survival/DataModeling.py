import pandas as pd


def calc_corr():
    titanic = pd.read_csv('./titanic2.csv', header = 0, engine = 'python')

    titanic_new = titanic[['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare', 'adult_male', 'alone']]
    titanic_corr = titanic_new.corr(method = 'pearson') # corr: 상관계수 분석하는 dataframe 자체 메서드.
    # pearson 상관계수 분석: 숫자(int64, float64, boolean 등)만 분석 가능

    print(titanic_corr) # 전체 상관 계수 확인하기

    print(titanic['survived'].corr(titanic['adult_male'])) # 특정 변수 사이의 단순 상관 계수 구하기

    titanic_corr.to_csv('./titanic2_corr.csv', index = True) # 저장

def category_age(x):
    if x < 10:
        return 0
    elif x < 20:
        return 1
    elif x < 30:
        return 2
    elif x < 40:
        return 3
    elif x < 50:
        return 4
    elif x < 60:
        return 5
    elif x < 70:
        return 6
    else:
        return 7

def feature_engineering(titanic):
    titanic['family'] = titanic['sibsp'] + titanic['parch'] + 1 # sibsp와 parch는 상관관계가 높았기에, 다중공선성 문제 방지를 위해 'family' 변수로 만듦.
    titanic['age2'] = titanic['age'].apply(category_age) # 'age'에 category_age 적용해 'age2'에 넣음
    titanic['sex'] = titanic['sex'].map({'male':1, 'female':0}) # str -> int

    titanic.to_csv('./titanic3.csv', index = False)
    
    
def visualize():
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    titanic = pd.read_csv('./titanic2.csv', header = 0, engine = 'python')

    # 1. 산점도로 상관 분석 시각화
    sns.pairplot(titanic, hue = 'survived') # 모든 변수쌍 간의 산점도로 상관 분석 시각화. hue에 종속변수 survived를 지정해 그룹별 데이터 분포 패턴도 시각적으로 확인 가능.
    plt.show()

    # 2. 두 변수의 상관관계 시각화
    sns.catplot(x = 'pclass', y = 'survived', hue = 'sex', data = titanic, kind = 'point') # categorical plot. 범주형 데이터에 적합. hue 인자를 독립변수 sex로 지정하여, 성별에 따라 집단을 구분한 것.
    plt.show()

    # 3. 시각화를 통해 얻은 분석 내용 반영
    feature_engineering(titanic)

    # 3. 히트맵으로 상관 계수 시각화
    ## 변수의 독립, 종속 역할은 분석 목적에 따라 결정됨(y에 넣었다고 항상 종속변수가 되거나, hue에 넣었다고 항상 독립변수가 되는 건 아니라는 의미
    titanic = pd.read_csv('./titanic3.csv', header = 0, engine = 'python')
    
    heatmap_data = titanic[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]
    colormap = plt.cm.RdBu # colormap에서 빨강-파랑 선택
    sns.heatmap(heatmap_data.astype(float).corr(), linewidths = 0.1, vmax = 1.0, square = True, cmap = colormap, linecolor = 'white', annot = True, annot_kws = {"size": 10}) # heatmap_data를 float으로 바꾸고, 상관계수 구함(6x6 행렬)
    plt.show()
    
    
    
if __name__ == '__main__':
    calc_corr()
    visualize()
    
    
