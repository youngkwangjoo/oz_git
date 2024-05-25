from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests



#브라우저 자동종료 방지
options = Options()
options.add_experimental_option("detach", True)

user = {
"User-Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
#화면 자동설정 옵션
# options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")
# options.add_argument("window-size=500,500")

#브라우저 최소화
# options.add_argument("--headless")

#브라우저 음소거
# options.add_argument("--mute-audio")

# 시크릿모드
# options.add_argument("incognito")

#상단메시지 없애기
# options.add_experimental_option("excludeSwitches",["enable-automation"])

#브라우저 상단메시지 삭제(web)
# options.add_experimental_option("excludeSwitches",["enable-logging"])

options.add_argument(f"User-Agent={user}")



driver = webdriver.Chrome(options=options)
url = "https://google.com"
driver.get(url)

driver.quit()

