# crawling test on coffeebeankorea.com

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions as EC
import time
import pandas as pd

def CoffeeBean_store(result):
    url = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome() # 크롬 webdriver 객체 생성

    for i in range(1, 600): # 매장 수만큼 반복
        start_time = time.time()
        wd.get(url) # 브라우저 연결(브라우저가 웹사이트 서버에 접속하여 html 문서 받아오기 시작) 후 페이지 로딩까지.
        # 페이지 로딩: html 본문, 이미지, css, js 파일 등 리소스를 브라우저가 다운로드하고 화면에 그리는(렌더링) 전체 과정
        page_load_time = time.time()
        try:
            wd.execute_script("storePop2(%d)" % i) # 자바스크립트 함수 호출해 매장 정보 페이지 엶(비동기 처리)
            try: # 팝업창 다 그린 후 소스를 가져오도록 명시적 대기 적용. store_table 클래스를 가진 테이블이 DOM(html 코드가 자바스크립트가 조작할 수 있도록 변환된 객체)에 나타날 때까지 최대 5초 대기
                element = ui.WebDriverWait(wd, 3).until( # 무조건 5초를 기다리는 time.sleep(5)와 달리, 테이블이 나타나면 바로 다음 코드 실행.
                    EC.presence_of_element_located((By.CSS_SELECTOR, "table.store_table"))
                )
            except Exception as e:
                # print("요소를 찾는 데 실패했습니다:", e)
                continue
            script_load_time = time.time()

            html = wd.page_source # 로딩이 완료된 후 안전하게 소스(html 문서) 가져옴
            soupCB = BeautifulSoup(html, 'html.parser')

            # print(f'page load time: {page_load_time - start_time}s') # 페이지 로딩에 걸린 시간
            # print(f'script load time: {script_load_time - page_load_time}s') # 팝업창 로딩에 걸린 시간

            # print(soupCB1.prettify()) # html 문서 시각화

            store_name_h2 = soupCB.select("div.store_txt > h2")
            # print(list(store_name_h2))
            store_name = store_name_h2[0].string
            print(f'%d: {store_name}' % i)

            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            # print(list(store_info))
            store_address_list = list(store_info[2])
            # print(store_address_list) # 주석도 별개의 객체로 취급하기에, 텍스트(주소)와 더불어 리스트의 자식 요소로 함께 포함
            store_address = store_address_list[0].strip()
            # print(store_address)

            store_phone = store_info[3].string
            # print(store_phone)

            result.append([i]+[store_name]+[store_address]+[store_phone])
        except:
            continue # 매장X 시 건너뜀
    return

def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)

    CB_tbl = pd.DataFrame(result, columns=('num', 'store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding = 'cp949', mode='w', index=True)

if __name__ == '__main__':
    main()

