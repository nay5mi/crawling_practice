#pip install openpyxl


import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

keyword = input("검색어를 입력하세요")
pagenum = 1


list = []
for i in range(1,100,10)   : 
    response= requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}", headers = header)
    html = response.text

    soup = BeautifulSoup(html,'html.parser')
    words = soup.select(".news_tit")

    for word in words:
        list.append(word.text.strip())
        
df = pd.DataFrame(list)
df.to_csv(f"{keyword}기사제목.csv", index=False,encoding="UTF-16")

