# graduation_thesis_2020
graduation thesis 2020, CAU, department of history, Moon Gyuseong

중앙대학교 역사학과 졸업논문, 20171580 문규성

python, beatiful soup, selenium 이용

## 적용 단계
1. web_crawling.py : 우리역사넷 웹 크롤링, 2차원/3차원 배열을 통해 URL 접근 (트리 사용할 줄 몰라서 노가다)
2. text_preprocess.py : 텍스트 전처리 (특수문자, 영어)
3. word_process.py : 처리된 어휘의 빈도수 통계 (maximum 20)

crawled(우리역사넷 텍스트 마이닝) -> processed(HTML 특수문자 전처리) -> stats(어휘수 빈도 통계)



source : http://contents.history.go.kr/front/ta/main.do

reference : https://l0o02.github.io/2018/06/09/python-crawling-1_copy0/