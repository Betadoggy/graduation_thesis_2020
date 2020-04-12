""" 
웹 크롤링 
"""

from bs4 import BeautifulSoup
import urllib.request
 
# 출력 파일 명
OUTPUT_FILE_NAME = 'output.txt'

# 긁어 올 URL(우리역사넷)
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