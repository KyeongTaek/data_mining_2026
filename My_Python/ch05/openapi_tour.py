import urllib.request
import sys
import pandas as pd
import datetime
import time
import json

# 주피터노트북의 파이썬 경로와, dotenv가 설치된 파이썬 경로가 달라서 생기는 import 에러를 잡기 위함.
# import sys
# !{sys.executable} -m pip install python-dotenv

import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

service_key = os.getenv("SERVICE_KEY")
alt_service_key = os.getenv("ALT_SERVICE_KEY")

# url 접속을 요청하고 응답을 받아서 반환

def getPublicRequestUrl(url):
    req = urllib.request.Request(url) # request 객체 생성
    try:
        resp = urllib.request.urlopen(req) # request 객체를 인자로 받아 서버에 요청을 보내고, 성공하면 응답을 담은 HttpResponse 객체를 반환
        if resp.getcode() == 200: # 네트워크 통신이 정상적으로 이루어지기만 하면 200 반환.
            print("[%s] Url Request Success" % datetime.datetime.now())
            return resp.read().decode('utf-8') # body에 대한 utf-8 디코딩
        else:
            print("[%s] Url Request Not Successful: %d" % (datetime.datetime.now(), resp.getcode()))
            return None
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

            # 데이터 요청 URL을 만들고, getRequestUrl()를 호출해서 받은 응답 데이터를 반환

def getTourismStatsItem(yyyymm, nat_cd, ed_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    # 헤더가 아닌, 파라미터처럼 들어감
    parameters = "?_type=json&serviceKey=" + alt_service_key # 26/9/30 - 작동하지 않아 alt_service_key를 이용
    parameters += "&YM=" + yyyymm # 연월(ex. 201201)
    parameters += "&NAT_CD=" + nat_cd # 국가 코드
    parameters += "&ED_CD=" + ed_cd # 출/입국 구분코드(D or E)

    url = service_url + parameters

    retData = getPublicRequestUrl(url) # body만. utf-8 디코딩됨.

    if (retData == None):
        return None
    else:
        return json.loads(retData) # dict 리턴

    # 수집 기간 동안 월 단위로 getTourismStatsItem()을 호출해 받은 데이터를 리스트로 묶어 반환

def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = []
    result = []
    natName = ''
    ed = ''
    dataEND = "{0}{1:0>2}".format(str(nEndYear), str(12)) # ex. 202612
    isDataEnd = 0 # 데이터 끝 확인용 flag 초기화
    
    for year in range(nStartYear, nEndYear+1): # startYear부터 endYear까지 반복
        for month in range(1, 13):
            if(isDataEnd == 1): break # 데이터 끝 flag 설정되어 있으면 작업 중지
            yyyymm = "{0}{1:0>2}".format(str(year), str(month)) # ex. 202601
            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd) # 응답을 dict 형태로 가져옴

            if "response" in jsonData and "header" in jsonData["response"]:
                result_code = jsonData["response"]["header"].get("resultCode") # 응답의 결과 코드 확인

                if result_code != 0 and result_code != "0000": # 정상("0000")이 아닌 경우
                    error_msg = jsonData["response"]["header"].get("resultMsg")
                    print(f"API 에러 발생: {error_msg}") # 에러 메시지 출력
                    break
            
            if jsonData['response']['body']['items'] == '': # 정보 없을 시
                isDataEnd = 1 # 데이터 끝 flag 설정
                dataEND = "{0}{1:0>2}".format(str(year), str(month-1)) # 이번달 전까지 성공했으니까
                print("데이터 없음... \n 제공되는 통계 데이터는 %s년 %s월까지입니다." %(str(year), str(month-1)))
                break
            print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False)) # 시각화
            natName = jsonData['response']['body']['items']['item']['natKorNm']
            natName = natName.replace(' ', '') # 공백 제거
            num = jsonData['response']['body']['items']['item']['num']
            ed = jsonData['response']['body']['items']['item']['ed']
            print('[ %s_%s : %s ]' % (natName, yyyymm, num))
            print('--------------------')
            jsonResult.append({ # 딕셔너리 리스트가 필요함(이후 json 파일로 만들기 위해)
                'nat_name': natName,
                'nat_cd': nat_cd,
                'yyyymm': yyyymm,
                'visit_cnt': num
            })
            result.append([natName, nat_cd, yyyymm, num]) # 리스트의 리스트가 필요함(이후 dataframe으로 만들기 위해)
    return (jsonResult, result, natName, ed, dataEND)

def main():
    jsonResult = []
    result = []

    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) :') # str.
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? :'))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? :'))
    ed_cd = "E" # E: 방한외래관광객(입국), D: 해외 출국

    jsonResult, result, natName, ed, dataEND = getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)

    if jsonResult == []: # api 에러나 연도 범위 오류의 경우
        return # 파일을 만들지 않고 종료

    # 파일저장 1: json 파일
    with open('./%s_%s_%d_%s.json' % (natName, ed, nStartYear, dataEND), 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False) # json(문자열)으로 만듦. 4칸 띄워 표현. 여러 개면 오름차순.
        outfile.write(jsonFile)

    # 파일저장 2: csv 파일
    columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
    result_df = pd.DataFrame(result, columns = columns)
    result_df.to_csv('./%s_%s_%d_%s.csv' % (natName, ed, nStartYear, dataEND), index = False, encoding = 'cp949')

if __name__ == "__main__":
    main()
