""" 
단어 통계처리 
"""

import os
from konlpy.tag import Twitter
from collections import Counter
 
# 크롤링한 파일을 저장할  폴더 만들기
if not(os.path.isdir('stats')):
	os.mkdir('stats')


# 특정 파일 내 txt파일 리스트
path = "processed"
file_list = os.listdir(path)
file_list_txt = [file for file in file_list if file.endswith(".txt")]


# 입출력 파일명
INPUT_FILE_NAME = 'processed/'
OUTPUT_FILE_NAME = 'stats/'


def get_tags(text, ntags=50):
    spliter = Twitter()
    # konlpy의 Twitter객체
    nouns = spliter.nouns(text)
    # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns)
    # Counter객체를 생성하고 참조변수 nouns할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.
    return return_list


# 메인 함수
def main():

    # 최대 많은 빈도수 부터 20개 명사 추출
    noun_count = 20

    # print ("file_list_txt: {}".format(file_list_txt))

    for file in file_list_txt:
        with open(INPUT_FILE_NAME + file, 'r', encoding = 'UTF-8') as read_file: # UTF-8 인코딩
            text = read_file.read() #파일을 읽습니다.
            tags = get_tags(text, noun_count) # get_tags 함수 실행
            with open(OUTPUT_FILE_NAME + file + ".txt", 'w', encoding = 'UTF-8') as write_file: 
                for tag in tags:
                    noun = tag['tag']
                    count = tag['count']
                    write_file.write('{} {}\n'.format(noun, count))


# 인터프리터에서 직접 실행
if __name__ == '__main__':
    main()