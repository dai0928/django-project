import requests
from bs4 import BeautifulSoup

word = "python"

pages = 5+1

result1 = "Search_word:" + word


url = "https://www.google.co.jp/search?hl=ja&num={pages}&q=" + word
request = requests.get(url)

soup = BeautifulSoup(request.text, "html.parser")
search_list = soup.select("div.kCrYT > a")

for rank, site in zip(range(1, pages), search_list):
    try:
        site_title = site.select('h3.zBAuLc')[0].text
    except IndexError:
        site_title = site.select("img")[0]['alt']
    site_url = site['href'].replace("/url?q=", "")
    result2 = str(rank) + "位:" + site_title + ":"
    result3 = site_url
