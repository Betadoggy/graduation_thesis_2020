""" 
우리 역사넷 고등학교 국사 대한민국 현대사 부분 
웹 크롤링 
"""

# os 라이브러리
import os
# requests 모듈 가져오기
import requests
# bs4 모듈에서 Beautifulsoup 가져오기
from bs4 import BeautifulSoup
# urllib.request 모듈 가져오기 (URL)
import urllib.request

# 크롤링한 파일을 저장할 crawled 폴더 만들기
if not(os.path.isdir('crawled')):
	os.mkdir('crawled')

# 출력 파일 명 및 주소
OUTPUT_FILE_NAME = 'crawled\crw_'

# 긁어 올 URL(우리역사넷)
"""
구조화 (교육과정-대단원-중단원-소단원)

e.g. 
'4-3-2-2'는 
'고등학교 국사 4차(하)-Ⅲ. 현대 사회의 발달-2. 민주주의 발전의 새 전기-(2) 대한 민국의 발전'을 의미

아래 URL 주소는 n차 교육과정 중 대한민국 현대사에 해당되는 내용만 작성

#-----------2차 교육과정(h21_)-----------#
'0070'            # 2-6
    '0070_0040'       # 2-6-4
    '0070_0050'       # 2-6-5
    '0070_0060'       # 2-6-6

#-----------3차 교육과정(h31_)-----------#
'0080'            # 3-5
    '0080_0010'       # 3-5-1
        '0080_0010_0010'  # 3-5-1-1
        '0080_0010_0020'  # 3-5-1-2
    '0080_0020'       # 3-5-2
        '0080_0020_0010'  # 3-5-2-1
        '0080_0020_0020'  # 3-5-2-2
    '0080_0030'       # 3-5-3

#-----------4차 교육과정(h42_)-----------#
'0050'            # 4-3
    '0050_0010'       # 4-3-1
        '0050_0010_0010'  # 4-3-1-1
        '0050_0010_0020'  # 4-3-1-2
    '0050_0020'       # 4-3-2
        '0050_0020_0010'  # 4-3-2-1
        '0050_0020_0020'  # 4-3-2-2
        '0050_0020_0030'  # 4-3-2-3
        '0050_0020_0040'  # 4-3-2-4

#-----------5차 교육과정(h52_)-----------#
'0060'            # 5-4
    '0060_0010'       # 5-4-1
        '0060_0010_0010'  # 5-4-1-1
        '0060_0010_0020'  # 5-4-1-2
        '0060_0010_0030'  # 5-4-1-3
        '0060_0010_0040'  # 5-4-1-4
    '0060_0020'       # 5-4-2
        '0060_0020_0010'  # 5-4-2-1
        '0060_0020_0020'  # 5-4-2-2
    '0060_0030'       # 5-4-3
        '0060_0030_0010'  # 5-4-3-1
        '0060_0030_0020'  # 5-4-3-2
        '0060_0030_0030'  # 5-4-3-3
        '0060_0030_0040'  # 5-4-3-4

#-----------6차 교육과정(h62_)-----------#
'0050'            # 6-4
    '0050_0010'       # 6-4-1
        '0050_0010_0010'  # 6-4-1-1
        '0050_0010_0020'  # 6-4-1-2
    '0050_0020'       # 6-4-2
        '0050_0020_0010'  # 6-4-2-1
        '0050_0020_0020'  # 6-4-2-2
    '0050_0030'       # 6-4-3
        '0050_0030_0010'  # 6-4-3-1
        '0050_0030_0020'  # 6-4-3-2
        '0050_0030_0030'  # 6-4-3-3
        '0050_0030_0040'  # 6-4-3-4
    '0050_0040'       # 6-4-4
        '0050_0040_0010'  # 6-4-4-1
        '0050_0040_0020'  # 6-4-4-2
    '0050_0050'       # 6-4-5
        '0050_0050_0010'  # 6-4-5-1
        '0050_0050_0020'  # 6-4-5-2
        '0050_0050_0030'  # 6-4-5-3
        '0050_0050_0040'  # 6-4-5-4

"""
# URL 기본주소
URL_src = "http://contents.history.go.kr/front/ta/view.do?levelId=ta_"

# 2 ~ 6차 교육과정
crs = [21, 31, 42, 52, 62]

# 대단원 번호
lar = [7, 8, 5, 6, 5]

# 중단원, 2차원 배열
mid = [[4, 5, 6], [1, 2, 3], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]

# 소단원, 3차원 배열
sml = [ [ [  None ], [  None ], [  None ]                   ],          # 3
        [ [1   , 2], [1   , 2], [  None ]                   ],          # 3
        [ [1   , 2], [1,2,3,4]                              ],          # 2
        [ [1,2,3,4], [1   , 2], [1,2,3,4]                   ],          # 3
        [ [1   , 2], [1   , 2], [1,2,3,4], [1,2], [1,2,3,4] ] ]         # 5

# URL 요청 및 제목 전처리
def url_req(address):
    req = requests.get(address)
    source = req.text
    soup = BeautifulSoup(source, 'html.parser')

    title = soup.select("#container > div.contWrap > div.content > h1")
    return title[0].text
    # print(title[0].text + ' : ' + address)   # HTML 태그 전처리 후 URL출력


# 크롤링 함수
def get_text(address):
    source_code_from_URL = urllib.request.urlopen(address)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.select('div.article'): # class가 article인 div태그
        text = text + str(item.find_all(text=True))
    return text


# 파일 입출력 함수
def io_file(address, title):
    open_output_file = open(OUTPUT_FILE_NAME + title + '.txt', 'w', -1, "utf-8")
    result_text = get_text(address)
    open_output_file.write(result_text)
    open_output_file.close()


# 메인 함수
def main():
    # index는 교육과정/대단원 순회
    for index, value in enumerate(crs): 

        # 일단 교육과정 번호(h21, h31...)
        URL = URL_src + 'h' + str(crs[index])
        print("\n" + str(index + 2) + "차 교육과정 : " + URL)

        # 교육과정 제목 변수
        crs_title = str(index + 2) + "차 교육과정_"

        # 대단원 URL 저장
        URL += '_00' + str(lar[index]) + '0'

        # URL 요청, 대단원 제목 전처리
        lar_title = crs_title + url_req(URL)

        # 파일 입출력
        io_file(URL, lar_title)

        # 대단원 URL 저장
        URL_set = URL
        
        # 중단원 순회 
        for m_index, value in enumerate(mid[index]):

            # 중단원 URL 저장
            URL_set = URL + '_00' + str(mid[index][m_index]) + '0'

            # URL 요청, 중단원 제목 전처리
            mid_title = lar_title + url_req(URL_set)

            # 파일 입출력
            io_file(URL_set, mid_title)

            # 소단원 순회
            for s_index, value in enumerate(sml[index][m_index]):

                # 소단원이 비어있는 경우 반복문 탈출
                if sml[index][m_index][s_index]==None:
                    break

                # 소단원 URL 저장
                URL_set_set = URL_set + '_00' + str(sml[index][m_index][s_index]) + '0'

                # URL 요청, 소단원 제목 전처리
                sml_title = mid_title + url_req(URL_set_set)

                # 파일 입출력
                io_file(URL_set, sml_title)

    
# 인터프리터에서 메인 함수 실행
if __name__ == '__main__':
    main()