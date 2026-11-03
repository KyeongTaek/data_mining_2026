#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 0. 라이브러리 임포트

import json
import re
from konlpy.tag import Okt
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud


# In[10]:


# Naver 검색 API 예제 코드 임포트
import urllib.request
import urllib.parse

import os
from dotenv import load_dotenv

import datetime
import json

load_dotenv() # .env 파일 로드

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

import sys
from pathlib import Path
ch05_path = os.path.abspath(os.path.join(Path.cwd(), '../../ch05')) # 경로를 절대 경로로 변환

if ch05_path not in sys.path:
    sys.path.append(ch05_path) # 파이썬 모듈 검색 경로에 추가

from nvCrawler import getRequestUrl, getNaverSearch, getPostData, main


# In[12]:


# 1. 데이터 수집
main() # 키워드에 대한 뉴스 기사를 1000건 가져와 json으로 저장함

inputFileName = '백엔드 개발자_naver_news.json'
data = json.loads(open(inputFileName, 'r', encoding = 'utf8').read())
print(data[0:50])


# In[23]:


# 2. 데이터 준비

# 2-1. 데이터 추출
titles = ''
for item in data:
    if 'title' in item.keys():
      raw = item['title']
      raw = re.sub(r'\[[^\]]+\]', '', raw) # 대괄호 안에 있는 내용 제거. ex. [생생 Job]
      raw = re.sub(r'<[^>]+>', '', raw) # 태그 제거. ex. <b>, </b>
      raw = re.sub(r'&[^;]+;', '', raw) # &quot; 제거.
      titles = titles + re.sub(r'[^\w]', ' ', raw) + '' # 유니코드, 숫자, 밑줄 아닌 거 찾아서 공백으로 대체(공백, 탭, 줄바꿈, 특수문자, 구두점, 하이픈 등이 걸림)
print(titles)


# In[24]:


# 2-2. 명사 단어 추출

nlp = Okt()
titles_N = nlp.nouns(titles) # 명사만 뽑음. 중복 체크는 안함.
print(titles_N)


# In[25]:


count = Counter(titles_N)
print(count)


# In[41]:


word_count = dict()
for tag, counts in count.most_common(50): # 출현 횟수 기준 상위 50개 뽑
    if len(str(tag)) > 1: # 길이가 1보다 큰 것만(50개 중 일부 제거됨!!)
        word_count[tag] = counts
        print("%s : %d" % (tag, counts))


# In[39]:


font_path = "c:/Windows/fonts/malgun.ttf" # 기본적인 폰트 위치
font_name = font_manager.FontProperties(fname = font_path).get_name()
matplotlib.rc('font', family = font_name) # font 속성 지정


# In[42]:


plt.figure(figsize = (12, 5))
plt.xlabel('키워드') # 한굴은 폰트 지정 안되면 꺠짐. 위에서 폰트 지정한 이유
plt.ylabel('빈도수')
plt.grid(True)
sorted_Keys = sorted(word_count, key = word_count.get, reverse = True)
sorted_Values = sorted(word_count.values(), reverse = True)
plt.bar(range(len(word_count)), sorted_Values, align = 'center')
plt.xticks(range(len(word_count)), list(sorted_Keys), rotation = 'vertical')
plt.show()


# In[43]:


wc = WordCloud(font_path, background_color = 'ivory', width = 800, height = 600)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize = (8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

