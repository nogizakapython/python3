# ジム予約サイト、自動化ツール

# WebDriverライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
# URL変数
target_url1 = "https://www.helloweb.jp/Reservation/Rapport/Members/Account/Login?ReturnUrl=%2fReservation%2fRapport%2fMembers%2f"
target_url2 = "https://www.helloweb.jp/Reservation/Rapport/Members/"
# XPATH変数
xpath1 = '//*[@id="UserName"]'
xpath2 = '//*[@id="Password"]'
xpath3 = '//*[@id="container"]/form/div[2]/input'
xpath4 = '/html/body/div[1]/div/div[2]/ul[2]/li[2]/a'
xpath5 = '//*[@id="container"]/div/div[2]/form[1]/input[6]'
xpath6 = '//*[@id="container"]/div/div/form[1]/input[6]'

# ログインページにアクセスし、ユーザー名、パスワードを自動入力してログインする。
driver = webdriver.Chrome()
driver.get(target_url1)
sleep(5)

text1 = driver.find_element(By.XPATH, xpath1)
text1.send_keys("0100002043")

text2 = driver.find_element(By.XPATH, xpath2)
text2.send_keys("hattori1#")

button1 = driver.find_element(By.XPATH, xpath3)
button1.click()

sleep(5)

# ログインしたので、メニューから予約をクリックする
driver.get(target_url2)
menu4 = driver.find_element(By.XPATH, xpath4)
menu4.click()
sleep(5)

#トレーニングジムボタンをクリックする
elem1 = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, xpath5))
elem1.click()

# 予約日ボタンをクリックする
elem2 = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, xpath6))
elem2.click()

sleep(180)
driver.quit()
