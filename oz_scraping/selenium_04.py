from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword

driver.get(url)
time.sleep(3)

# #스크롤 코드
# driver.execute_script("window.scrollTo(0, 10000)")
# time.sleep(2)

# #스크롤 페이지 끝까지 내리는 코드
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(2)
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    blog_users = soup.select(".user_box")# 큰상자
    blog_names = soup.select(".title_link")# 블로그제목
    blog_name = soup.select(".name")# 작성자
    for i in zip(blog_users,blog_names,blog_name):
        print(i[0].text)
        print(i[1].text)





