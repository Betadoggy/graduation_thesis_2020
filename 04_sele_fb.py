from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = "mgs4786@gmail.com"
pwd = "Mgs_56565656"

path = "C:\\Users\\Moon Gyuseong\\Desktop\\crawling\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title # 예외처리
elem = driver.find_element_by_id("email")
elem.send_keys(usr) # 커서가 위치한 곳에 넣음
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd) # 커서가 위치한 곳에 넣음
elem.send_keys(Keys.RETURN) # 엔터키