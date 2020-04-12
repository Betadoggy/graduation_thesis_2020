import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/')
source = req.text
soup = BeautifulSoup(source, 'html.parser')

top_list = soup.select("#news_cast > div.area_newstop > div > div > ol > li > a")

for top in top_list:
    print(top.text)