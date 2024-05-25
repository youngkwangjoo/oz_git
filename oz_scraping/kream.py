from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests



#브라우저 자동종료 방지
options = Options()
options.add_experimental_option("detach", True)

user = {
"User-Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

options.add_argument(f"User-Agent={user}")

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

driver = webdriver.Chrome(options=options)
url = "https://kream.co.kr/"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".nav-search.icon.sprite-icons").click()#띄어쓰기는 .으로 대체
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(3)

for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


items = soup.select(".item_inner") #find_all로 찾으면 리스트로 들어감. 

for i in items:
    product_name = i.select_one(".translated_name")
    if "후드" in product_name.text:
        price = i.select_one(".amount").text
        print(product_name.text)
        print(price)


driver.quit()
