import requests
from bs4 import BeautifulSoup

header_user = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "http://www.cgv.co.kr/movies/?lt=1&ft="
req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

movie_rank = soup.select(".rank")
movie_name = soup.select(".title")
movie_rating = soup.select(".percent")
movie_first = soup.select(".txt-info")

for i in zip(movie_rank, movie_name, movie_rating, movie_first):
    print(f"영화 제목 : {i[0].text}")
    print(f"영화 이름 : {i[1].text}") 
    print(f"영화 예매율 : {i[2].text}")
    x = "".join(i[3].text.split())
    print(f"영화 개봉일 : {x}")
    print(sep="/")
# 영화 개봉일만 떨어져 있어서 strip를 썻더니 이번엔 개봉만 떨어져서 나옴
# split은 gpt검색해서 알아낸 방법인데 단어를 글자 단위로 쪼갠뒤 join함수로 공백을 없애니 여백이 아예 없어지는 결과가 나옴