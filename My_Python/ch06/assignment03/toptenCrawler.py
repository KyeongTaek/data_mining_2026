# crawling test on topten

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

def topten_store(result):
    topten_url = 'https://display-topten10.goodwearmall.com/ranking/SSMA42'
    print(topten_url)

    html = urllib.request.urlopen(topten_url) # http 요청 보내고(보통 get) httpresponse 받음
    
    soupTopten = BeautifulSoup(html, 'html.parser')
    tag_divs = soupTopten.find_all('div', attrs={'class': 'catalog-item st-tile'}) # find_all이나 find의 경우, class 속성은 attrs로 지정(key-value)
    # print(tag_divs)

    for elem in tag_divs: # 각각의 상품에 대해서
        body = elem.select('div.tile-body')[0] # 브랜드, 상품명, 가격이 위치한 파트
        # print(body)

        brand = body.select('strong.tile-brand')[0].string
        # print(brand)
        
        product = body.select('p.tile-goods-label > span.tile-goods-label-inner')[0].string # p 태그 안의 span 태그에 텍스트가 위치
        print(product)
        
        price = body.select('div.tile-price-box > strong.tile-price.st-current')[0].string # div 태그 안의 strong 태그에 텍스트가 위치
        # print(price)
        
        footer = elem.select('div.tile-footer')[0] # 평점과 리뷰 개수가 위치한 파트

        stats = footer.select('div.tile-affinity')[0].find_all('p') # div 태그 내에서 p 태그 검색
        if len(stats) == 1: # 찜하기만 있는 경우
            result.append([brand] + [product] + [price] + [None] + [0])
            continue
        
        stats = stats[1] # 평점과 리뷰 개수가 위치한 p 태그
        
        review = stats.text.split() # 요소가 텍스트 뿐 아니라 i태그도 있기에, string이 아닌 text로 가져와야 함.
        # print(review)
        
        review_rate = review[0] # 평점
        # print(review_rate)
        review_cnt = review[1][1:-1] # 리뷰 개수(앞뒤의 소괄호 제거)
        # print(review_cnt)
        
        result.append([brand] + [product] + [price] + [review_rate] + [review_cnt])

def main():
    result = [] # 결과를 저장할 리스트
    print('Topten crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    topten_store(result)

    topten_tbl = pd.DataFrame(result, columns = ('brand', 'product', 'price', 'review_rate', 'review_cnt'))
    topten_tbl.to_csv("./topten_best.csv", encoding="cp949", mode="w", index=True) # 인덱스 지정

if __name__ == '__main__':
    main()
