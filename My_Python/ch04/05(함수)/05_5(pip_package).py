"""
05. 함수
3) 모듈과 패키지
"""
# pip으로 설치된 파이썬 패키지는 네이티브(아나콘다/venv 안한 경우) 기준으로 윈도우에서는 appdata 폴더 하위에 Lib\site-packages에 있다.

# Request('http://www.hanb.co.kr') # error. 임포트를 아직 안했기 때문.

import urllib.request # 패키지: urllib. 모듈: request --> urllib/request.py
print(urllib.request.Request('http://www.hanb.co.kr'))

import pandas as pd
print(pd.DataFrame())

from datetime import datetime
print(datetime.now())
