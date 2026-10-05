# crawling test on hollys.co.kr

from bs4 import BeautifulSoup # 파싱
import urllib.request
import pandas as pd
import time

def hollys_store(result):
    for page in range(1, 58):
        hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' % page
        print(hollys_url)

        html = urllib.request.urlopen(hollys_url) # http 요청 보내고(보통 get) httpresponse 받
        time.sleep(0.5) # 요청 간 0.5초의 sleep을 넣어서 혹시 모를 ip ban을 회피
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody') # tbody 1개 가져옴
        for store in tag_tbody.find_all('tr'): # tr 모두 가져옴
            if len(store) <= 3: # 파싱 정보 없으면
                break
            store_td = store.find_all('td') # td는 6개
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name] + [store_sido] + [store_address] + [store_phone])

    print(f'length: {len(result)}')
    print(result[0])

    print(result[563])
    print(list(store_td))
    print(store_td[1].string)
    print(store_td[0].string)
    print(store_td[3].string)
    print(store_td[5].string)

    return

def main():
    result = [] # 결과를 저장할 리스트
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    hollys_store(result)
    
    hollys_tbl = pd.DataFrame(result, columns = ('store', 'sido-gu', 'address', 'phone'))
    hollys_tbl.to_csv("C:/Users/HP/Desktop/data_mining_2026/My_Python/ch06/hollys.csv", encoding="cp949", mode="w", index=False) # index=True의 경우 가장 왼쪽에 인덱스 열 추가    

    del result[:]

if __name__ == '__main__':
    main()
