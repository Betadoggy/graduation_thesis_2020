""" 
텍스트 전처리
특수문자, 영어 제거
"""

import re

# 입출력 파일명
INPUT_FILE_NAME = 'output.txt'
OUTPUT_FILE_NAME = 'output_prp.txt'


# 텍스트 전처리(Preprocess text 함수)
def prp_text(text):
    prped_text = re.sub('[a-zA-Z]', '', text) # 영어
    prped_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', prped_text) # 특수문자

    return prped_text


# 메인 함수
def main():
    read_file = open(INPUT_FILE_NAME, 'r', encoding= 'UTF-8') # UTP-8 인코딩
    write_file = open(OUTPUT_FILE_NAME, 'w', encoding= 'UTF-8')
    text = read_file.read()
    text = prp_text(text)
    write_file.write(text)
    read_file.close()
    write_file.close()


# 인터프리터에서 직접 실행할 경우
if __name__ == "__main__":
    main()