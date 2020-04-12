""" 
웹 크롤링 
"""

from bs4 import BeautifulSoup
import urllib.request
 
# 출력 파일 명
OUTPUT_FILE_NAME = 'output.txt'

# 긁어 올 URL(우리역사넷)
"""
구조화 (교육과정-대단원-중단원-소단원)

e.g. 
'4-3-2-2'는 
'고등학교 국사 4차(하)-Ⅲ. 현대 사회의 발달-2. 민주주의 발전의 새 전기-(2) 대한 민국의 발전'을 의미

"""
#-----------2차 교육과정-----------#
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h21_0070'            # 2-6

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h21_0070_0040'       # 2-6-4
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h21_0070_0050'       # 2-6-5
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h21_0070_0060'       # 2-6-6

#-----------3차 교육과정-----------#
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080'            # 3-5

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080_0010'       # 3-5-1

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080_0010_0010'  # 3-5-1-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080_0010_0020'  # 3-5-1-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080_0020'       # 3-5-2
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080_0020_0010'  # 3-5-2-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080_0020_0020'  # 3-5-2-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h31_0080_0030'       # 3-5-3

#-----------4차 교육과정-----------#
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050'            # 4-3

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0010'       # 4-3-1

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0010_0010'  # 4-3-1-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0010_0020'  # 4-3-1-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0020'       # 4-3-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0020_0010'  # 4-3-2-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0020_0020'  # 4-3-2-2
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0020_0030'  # 4-3-2-3
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h42_0050_0020_0040'  # 4-3-2-4

#-----------5차 교육과정-----------#
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060'            # 5-4

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0010'       # 5-4-1

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0010_0010'  # 5-4-1-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0010_0020'  # 5-4-1-2
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0010_0030'  # 5-4-1-3
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0010_0040'  # 5-4-1-4

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0020'       # 5-4-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0020_0010'  # 5-4-2-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0020_0020'  # 5-4-2-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0030'       # 5-4-3

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0030_0010'  # 5-4-3-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0030_0020'  # 5-4-3-2
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0030_0030'  # 5-4-3-3
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h52_0060_0030_0040'  # 5-4-3-4

#-----------6차 교육과정-----------#
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050'            # 6-4

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0010'       # 6-4-1

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0010_0010'  # 6-4-1-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0010_0020'  # 6-4-1-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0020'       # 6-4-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0020_0010'  # 6-4-2-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0020_0020'  # 6-4-2-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0030'       # 6-4-3

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0030_0010'  # 6-4-3-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0030_0020'  # 6-4-3-2
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0030_0030'  # 6-4-3-3
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0030_0040'  # 6-4-3-4

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0040'       # 6-4-4

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0040_0010'  # 6-4-4-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0040_0020'  # 6-4-4-2

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0050'       # 6-4-5

'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0050_0010'  # 6-4-5-1
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0050_0020'  # 6-4-5-2
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0050_0030'  # 6-4-5-3
'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h62_0050_0050_0040'  # 6-4-5-4

URL = 'http://contents.history.go.kr/front/ta/view.do?levelId=ta_h21_0070_0040'
 
 
# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.select('div.article'): # class가 article인 div태그
        text = text + str(item.find_all(text=True))
    return text
 
 
# 메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w', -1, "utf-8")
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()
    
 
if __name__ == '__main__':
    main()