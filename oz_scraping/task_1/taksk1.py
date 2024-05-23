import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요: ")

url = base_url + keyword
#print(url)
req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html, "html.parser")

# blog_users = soup.select(".user_box")
blog_users = soup.select(".user_box")
blog_names = soup.select(".title_link")
blog_name = soup.select(".name")

for user, names, name in zip(blog_users, blog_names, blog_name):
    if user.find(class_="spblog ico_ad"):
        continue
    else:
        print(f" 저자 : {name.text}")
        print(f" 제목 : {names.text}")
        print(sep="/")
#users 와 names를 합쳐보려 했으나 애초에 코드 작동방식이 user에 광고 클래스가 있으면 스킵하는 코드이기 때문에 그냥 따로했음

#     #유저박스를 가져올때 class spblog 가 포함되어있다면 false 아니라면 그아래 제목을 가져온다?


# import requests
# from bs4 import BeautifulSoup

# header_user = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
# keyword = input("검색어를 하나만 입력해주세요: ")

# url = base_url + keyword
# #print(url)
# req = requests.get(url, headers=header_user)
# html = req.text
# soup = BeautifulSoup(html, "html.parser")

# blog = soup.select(".user_box, .title_link")


# for i in blog:
#     if i.find(class_="spblog ico_ad"):
#         continue
#     else:
#         print(i.text)
       
