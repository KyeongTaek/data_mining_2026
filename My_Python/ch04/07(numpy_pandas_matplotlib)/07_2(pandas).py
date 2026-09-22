"""
07. numpy, pandas, matplotlib
2) pandas

- 데이터 조작 및 분석을 위한 python용으로 작성된 소프트웨어 라이브러리.
- 숫자 테이블과 시계열을 조작하기 위한 데이터 구조와 연산을 제공.

"""

import pandas as pd
print(pd.__version__)

# 1. series
data1 = [10, 20, 30, 40, 50]
print(data1)

data2 = ['1반', '2반', '3반', '4반', '5반']
print(data2)

sr1 = pd.Series(data1) # series 객체 생성
print(sr1) # int64: 정수

sr2 = pd.Series(data2)
print(sr2) # object: 문자, 숫자 섞여서

sr3 = pd.Series([101, 102, 103, 104, 105])
print(sr3)

sr4 = pd.Series(['월', '화', '수', '목', '금'])
print(sr4)

sr5 = pd.Series(data1, index = [1000, 1001, 1002, 1003, 1004]) # 인덱스 변경
print(sr5)

sr6 = pd.Series(data1, index = data2) # 문자열도 인덱스로 가능
print(sr6)

sr7 = pd.Series(data2, index = data1)
print(sr7)

sr8 = pd.Series(data2, index = sr4)
print(sr8)

# print(sr8[2]) # error: 인덱스로 접근하는 방식은 deprecated 됨(pandas 버전 높아지며)
# print(sr8[-1])
print(sr8['수'])
print(sr8[0:4])

print(sr8.index)
print(sr8.values)

print(sr1 + sr3) # series끼리 연산 가능. int+int->int
print(sr4 + sr2) # obj+obj->obj(concat)

# 2. dataframe
data_dict = {
    'year': [2018, 2019, 2020],
    'sales': [340, 480, 1099]
}

print(data_dict)

df1 = pd.DataFrame(data_dict)
print(df1)

df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]], index = ['중간고사', '기말고사'], columns = data2[0:3])
print(df2)

data_df = [['20201101', 'Hong', '90', '95'], ['20201102', 'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']] # 3x4
df3 = pd.DataFrame(data_df)
print(df3) # index, columns 지정 안하면 0부터 순차적으로 1씩 증가

df3.columns = ['학번', '이름', '중간고사', '기말고사'] # 생성한 이후에 수정 가능
print(df3)

print(df3.head(2)) # 위에서부터 2개
print(df3.tail(2)) # 뒤에서부터 2개

print(df3['이름']) # 마치 DB의 프로젝션 연산

df3.to_csv('c:/temp/score.csv', header='False') # 전처리 결과를 저장. 인코딩 방식은 생략. csv: 구분자가 세미콜론 or 컴마
df4 = pd.read_csv('c:/temp/score.csv', encoding='utf-8', index_col=0, engine='python') # 전처리 결과 읽. index_col=0: 0번 컬럼을 인덱스로.

# +ms office: 한글 인코딩이 cp949. -> 엑셀로 utf-8(기본인코딩)을 열면 깨짐

df4 = pd.read_csv('c:/temp/score.csv', encoding='utf-8', index_col=1, engine='python') # 학번이 인덱스 됨
