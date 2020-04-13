# urllib.request 모듈 가져오기 (URL)
import requests
from bs4 import BeautifulSoup

"""
임시로 만든 전체 페이지 분석 반복문
트리를 써볼려 했지만 이진트리로 도저히 구현할 수 없어서 배열로 만듦
"""

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
    print(title[0].text + ' : ' + address)   # HTML 태그 전처리 후 URL출력


# index는 교육과정/대단원 순회
for index, value in enumerate(crs): 

    # 일단 교육과정 번호(h21, h31...)
    URL = URL_src + 'h' + str(crs[index])
    print("\n" + str(index + 2) + "차 교육과정 : " + URL)

    # 대단원 URL 저장
    URL += '_00' + str(lar[index]) + '0'

    # URL 요청, 대단원 제목 전처리
    url_req(URL)

    # 대단원 URL 저장
    URL_set = URL

    # 중단원 순회 
    for m_index, value in enumerate(mid[index]):

        # 중단원 URL 저장
        URL_set = URL + '_00' + str(mid[index][m_index]) + '0'

        # URL 요청, 중단원 제목 전처리
        url_req(URL_set)

        # 소단원 순회
        for s_index, value in enumerate(sml[index][m_index]):

            # 소단원이 비어있는 경우 반복문 탈출
            if sml[index][m_index][s_index]==None:
                break

            # 소단원 URL 저장
            URL_set_set = URL_set + '_00' + str(sml[index][m_index][s_index]) + '0'

            # URL 요청, 소단원 제목 전처리
            url_req(URL_set_set)