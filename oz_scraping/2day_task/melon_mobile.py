from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".img-logo").click()#광고 제거
time.sleep(2)

driver.find_element(By.LINK_TEXT,"멜론차트").click() #멜론차트 클릭

for i in range(5):# 스크롤 5번
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5) 

### 더보기 버튼 누르기
button_selector = "#moreBtn"
driver.execute_script("hasMore2();")
time.sleep(1)
### 5번 더 내리기
for i in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

#스크래핑
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

###
ele = driver.find_element(By.ID, '_chartList').find_elements(By.CLASS_NAME,'list_item')
for i in ele:
    x = "".join(i.find_element(By.CLASS_NAME, "ranking_num").text.split())
    print("순위 :", x)
    print(i.find_element(By.CLASS_NAME, "content").text)
    print(sep="/")


driver.quit
#find_elements는 왜 .text가 안되는것인가...


