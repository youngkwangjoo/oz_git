import requests
from bs4 import BeautifulSoup

keyword = input("검색헐 상품 : ")
url = f"https://www.coupang.com/np/search?component=&q={keyword}"

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36","accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
cookie = {"a":"c"}
req = requests.get(url, timeout=5, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")

for rank, item in enumerate(items, 1):
    name = item.select_one(".name")
    price = item.select_one(".price-value")
    link =item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")
    
    print(f"[{rank}]위")
    print(f"제품명 : {name.text}")
    print(f"{price.text}원")
    roket = item.select_one(".badge.rocket")

    if roket:
        print("🚀로켓 배송 가능")
    else:
        print("🚀로켓 배송 불가")
    
    print(f"링크 : https://www.coupang.com{link}")
    if img_src.get("data-img-src"):
        img_url = f"http:{img_src.get('data-img-src')}"
    else :
        img_url = f"http:{img_src.get('src')}"
    print(f"이미지 URl: {img_url}")
    print()

    img_req = requests.get(img_url)
    with open(f"img/{rank}.jpg", "wb") as f:
        f.write(img_req.content)