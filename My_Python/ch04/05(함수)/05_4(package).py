"""
05. 함수
3) 모듈과 패키지
"""

# 패키지: 여러 모듈을 디렉토리 구조로 조직화한 것. 모듈을 포함하는 디렉토리이며, 해당 디렉토리를 패키지로 인식하도록 하기 위해 __init__.py라는 파일이 필요함(python 3.3 이후로는 없어도 인식이 되나, 명시적으로 사용하는 게 일반적)

from mypackage import module1, some_function # __init__.py 덕분에, some_function은 하위 모듈 경로를 생략하고 바로 함수 임포트 가능

print(module1.greet("Tianhong"))
print(some_function())
