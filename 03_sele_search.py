from selenium import webdriver

path = "C:\\Users\\Moon Gyuseong\\Desktop\\crawling\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('http://google.com/')
search_box = driver.find_element_by_name("q")
search_box.send_keys("개발새발 블로그")
search_box.submit()
