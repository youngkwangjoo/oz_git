from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

user = {
"User-Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

#브라우저 자동종료 방지
options = Options()
options.add_experimental_option("detach", True)


Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)
url = "https://google.com"
driver.get(url)


