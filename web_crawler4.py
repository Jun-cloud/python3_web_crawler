# 자동화 테스트를 위해 셀레니움(Selenium)을 불러옵니다
from selenium import webdriver
import time

# 크롬 웹 드라이버의 경로를 설정합니다.
driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver.exe')

# 크롬을 통해 네이버 로그인 화면에 접속합니다.
driver.get('https://nid.naver.com/nidlogin.login')

# 아이디와 비밀번호를 입력합니다. (0.5초씩 기다리기)
time.sleep(0.5)
#driver.find_element_by_name('id').send_keys('id')
driver.execute_script("document.getElementsByName('id')[0].value=\"id\"")
time.sleep(0.5)
#driver.find_element_by_name('pw').send_keys('pw')
driver.execute_script("document.getElementsByName('pw')[0].value=\"pw\"")

# XPath를 이용해 로그인을 시도합니다.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
