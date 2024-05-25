#목표 : lst50, lst100, lst_all을 find_all을 이용해 한줄로 작성해주세요
import requests
from bs4 import BeautifulSoup

header_user = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "https://www.melon.com/chart/index.htm"
req = requests.get(base_url, headers=header_user)


html = req.text
soup = BeautifulSoup(html, "html.parser")

lst = soup.select(".lst50, .lst100")

for rank, i in enumerate(lst, 1):
    rank = i.select_one(".rank")
    title = i.select_one(".ellipsis.rank01 a")#el이랑 ran안에 있는 a 태그를 선택함
    singer = i.select_one(".checkEllipsis")#.ellicsis.rank02,#checkEllipsis
    album = i.select_one(".ellipsis.rank03 a")
    print(f"[순위] {rank.text}")
    print(f"제목 : {title.text}") 
    print(f"가수 : {singer.text}")
    print(f"가수 : {album.text}")
    print(sep="/")