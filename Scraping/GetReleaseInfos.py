from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

CHROMEDRIVER = r"C:\Users\gwrhyr\.ego_drivers\chromedriver.exe"

# Accesss to mercari home page (NO LOGIN)
browser = webdriver.Chrome(CHROMEDRIVER)

## User page URL
load_url = 'https://jp.mercari.com/user/profile/393647851'
browser.get(load_url)

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
# HTML全体を表示する
print(soup)




