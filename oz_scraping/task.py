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
    print(i[0].text)
    print(i[1].text) 
    print(i[2].text)
    print(i[3].text)
