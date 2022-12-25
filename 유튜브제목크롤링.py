#pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv




keyword = input("검색어를입력하세요")
url = f"https://www.youtube.com/results?search_query={keyword}"


#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach',True)


#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = chrome_options)


#주소이동
driver.implicitly_wait(5) #웹페이지가 로딩될때까지 5초는 기다림
driver.maximize_window()

driver.get(url)



body = driver.find_element(By.TAG_NAME,'body')
for i in range(1,15):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    
    
f = open(r"C:\Users\user\논병아리\crawling_practice\{0}제목.csv".format(keyword),"w",encoding="CP949",newline="")
csvwriter = csv.writer(f)

items = driver.find_elements(By.CSS_SELECTOR,"#dismissible.style-scope.ytd-video-renderer")

for item in items:
    name = item.find_element(By.CSS_SELECTOR, "#title-wrapper").text
    # view = item.find_element(By.CSS_SELECTOR,"#metadata-line").text
    # time = item.find_element(By.CSS_SELECTOR,"''")
    try:
        view = item.find_element(By.CSS_SELECTOR,"#metadata-line > span:nth-child(3)").text
    except:
        view = "광고"
    try:
        time = item.find_element(By.CSS_SELECTOR,"#metadata-line > span:nth-child(4)").text
    except:
        time = "광고"

    csvwriter.writerow([name,view,time])
    
f.close()
