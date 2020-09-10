""" 
텍스트 전처리
특수문자, 영어 제거
"""

import os
import re

# 크롤링한 파일을 저장할 processed 폴더 만들기
if not(os.path.isdir('processed')):
	os.mkdir('processed')

# 특정 파일 내 txt파일 리스트
path = "crawled"
file_list = os.listdir(path)
file_list_txt = [file for file in file_list if file.endswith(".txt")]

print ("file_list_txt: {}".format(file_list))


# 입출력 파일명
INPUT_FILE_NAME = 'crawled/'
OUTPUT_FILE_NAME = 'processed/prc'


# 텍스트 전처리(Preprocess text 함수)
def prp_text(text):
    prped_text = re.sub('[a-zA-Z]', '', text) # 영어
    prped_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', prped_text) # 특수문자

    return prped_text

# 메인 함수
def main():
    for file in file_list_txt:
        with open(INPUT_FILE_NAME + file, 'r', encoding = 'UTF-8') as read_file: # UTF-8 인코딩
            text = read_file.read()
            text = prp_text(text)
            with open(OUTPUT_FILE_NAME + file.replace("crw", ""), 'w', encoding = 'UTF-8') as write_file: 
                write_file.write(text)


# 인터프리터에서 직접 실행할 경우
if __name__ == "__main__":
    main()