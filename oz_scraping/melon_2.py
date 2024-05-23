import requests
from bs4 import BeautifulSoup

header_user = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "https://www.melon.com/chart/index.htm"
req = requests.get(base_url, headers=header_user)


html = req.text
soup = BeautifulSoup(html, "html.parser")

#print(soup.title)
#title은 하나다. h1은 한페이지에 한개다. 
#print(soup.h1)#태그안에 텍스트는 뽑을 수 없다. 
#find 방식
# h1 = soup.find("h1")
# print(h1)

# logo = soup.find(class_="page_header")
# logo2 = soup.select_one(".page_header")
# print(logo)
# print(logo2)

# nav = soup.find(class_="button_rbox", text="담기")
# print(nav)

#find는 하나의 값만 출력한다. 

navs = soup.find_all(class_="button_rbox")
print(len(navs))
#데이터 타입을 모두 찾는다는건 list타입이라는것. 그래서list에서 쓰는 모든 메소드를 사용가능
for i in navs:
    print(i.text)