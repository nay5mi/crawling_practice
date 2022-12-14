#pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time






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

driver.get("https://www.naver.com")
driver.find_element(By.CSS_SELECTOR,"a.nav.shop").click()
time.sleep(3)

search = driver.find_element(By.CSS_SELECTOR,"input._searchInput_search_text_3CUDs")
search.click()


search.send_keys('아이폰')
search.send_keys(Keys.ENTER)

#f12 console 창 들어가기 window.scrollY 치기 




# driver.switch_to.frame("iframe")

# #본문 iframe 은페이지 안에 다른페이지로 인식됨
# driver.find_element(By.CSS_SELECTOR,"body > div > div.workseditor-content").send_keys("본문입니다")
# time.sleep(2)

# driver.swithc_to.default_content()

# driver.find_element(By.CSS_SELECTOR,"#content > div.mail_toolbar.type_write > div:nth-child(1) > div").click()

