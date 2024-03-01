#######   日経新聞HP 人事検索テスト　###########
#######   新規作成  2024/3/1  ##########
#######   Author  takao.hattori ###########



# 時間を計るライブラリをインポート
import datetime
import re
import os
# WebDriverライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl as op
import codecs
from time import sleep
import shutil
import selenium
import sys

dt = datetime.datetime.now()
date1 = dt.strftime('%Y%m%d%H%M%S')
date2 = dt.strftime('%Y')
date3 = dt.strftime('%Y%m%d')


file_name = "jcuu" + date1 + ".txt"
out_file = "jcuu.txt"
string1 = '<div id="sideCallouts">'
date_str = ""
w_title = ""
base_url = 'https://jccu.coop'

target_url = 'https://www.nikkei.com/news/jinji/hatsurei/?page=1'
max_row = 5
#base_file = "【企業個別】検索結果_yyyymmdd.xlsx"
export_file = "【企業個別】検索結果_" + date3 + ".xlsx"
row_count = 0
write_flag = 0
xpath_str1 = ""
# Chromeを指定する

driver = webdriver.Chrome()

# Chromeを開いてCOOP企業HPにアクセスする
try:
    driver.get(target_url)
    sleep(5)
    
    for h in range(1,3):
        for i in range(1,20):
            
            xpath_str1 = '/html/body/div[5]/main/div[3]'
            try:
                element_str1 = driver.find_element(by=By.XPATH,value=xpath_str1)
            except:
                break
            print(element_str1.get_attribute("outerHTML"),file=codecs.open(file_name,'a','utf-8'))
            
    

except EnvironmentError as e:
    str100 = e     