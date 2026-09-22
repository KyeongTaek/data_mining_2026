# Naver 검색 API 예제 코드(https://api.ncloud-docs.com/docs/naver-api-hub-search-examples#python)

import urllib.request
import urllib.parse

import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

enc_text = urllib.parse.quote("커피") # utf-8로 인코딩(기본)
url = "https://naverapihub.apigw.ntruss.com/search/v1/blog?query=" + enc_text + "&display=2"

request = urllib.request.Request(url) # request 객체 생성
request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
request.add_header("X-NCP-APIGW-API-KEY", client_secret)

response = urllib.request.urlopen(request) # 전송 및 응답 받음
rescode = response.getcode()
if rescode == 200:
    response_body = response.read() # body를 읽어옴(json)
    print(response_body.decode("utf-8"))
else:
    print("Error Code:" + str(rescode))

def main():
 node = 'news' #크롤링할 대상
 srcText = input('검색어를 입력하세요: ')
 cnt = 0
 jsonResult = []

 jsonResponse = getNaverSearch(node, srcText, 1, 100) #[CODE 2]
 total = jsonResponse['total']

 while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
   for post in jsonResponse['items']:
     cnt += 1
     getPostData(post, jsonResult, cnt) #[CODE 3]

   start = jsonResponse['start'] + jsonResponse['display']
   jsonResponse = getNaverSearch(node, srcText, start, 100) #[CODE 2]

 print('전체 검색 : %d 건' %total)

 with open('%s_naver_%s.json' % (srcText, node), 'w', encoding = 'utf8') as outfile:
   jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True,
ensure_ascii = False)

   outfile.write(jsonFile)

 print("가져온 데이터 : %d 건" %(cnt))
 print('%s_naver_%s.json SAVED' % (srcText, node))
