import pandas as pd
import os

"""
current_path = os.getcwd()
print(current_path)

os.chdir("C:\\Users\\Moon Gyuseong\\Documents\\github\\graduation_thesis_2020\\stats")

current_path = os.getcwd()
print(current_path)
"""

# csv 파일로 변환할 csv 폴더 만들기
if not(os.path.isdir('csv')):
	os.mkdir('csv')


# stats 파일 내 txt파일 리스트
path = "stats"
file_list = os.listdir(path)
file_list_txt = [file for file in file_list if file.endswith(".txt")]


# 입출력 파일명
INPUT_FILE_NAME = 'stats/'
OUTPUT_FILE_NAME = 'csv/csv'

# stats 내부의 전체 파일 읽기 
# 파일명 읽고 변수로, 그 외는 동일하게 구분자 \t


# 메인 함수
def main():
    for file in file_list_txt:
        raw_data = pd.read_csv(INPUT_FILE_NAME + file, names=["어휘", "빈도수"])