from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)#파이어폭스 같은거도 나옴

url = "http://naver.com"

driver.get(url)
time.sleep(3)
#차이점은?
html =driver.page_source#req.text랑 똑같은것

soup = BeautifulSoup(html, "html.parser")
query = soup.select_one(".serch_input_box")
