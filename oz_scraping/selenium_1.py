from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)#파이어폭스 같은거도 나옴

url = "http://naver.com"

driver.get(url)
time.sleep(3)

title = driver.title
# print(title)

html = driver.page_source
print(html)
#차이점은?