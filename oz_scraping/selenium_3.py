from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests
# Service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=Service)

url = "https://section.cafe.naver.com/ca-fe/home"
#동적페이지는 매번 바뀌기 때문에 페이지 안에 코드는 굉장히 짧다. 

# driver.get(url)
# time.sleep(5)
# html = driver.page_source

#bs4를 이용해서 내용을 가져오면 이렇게 조금가져온다. 
req = requests.get

