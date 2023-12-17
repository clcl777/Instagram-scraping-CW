from selenium import webdriver
import urllib.request
import time
import re
import openpyxl
import pyautogui as pg
import os
import configparser

url = 'https://instagram.com/kitty_in_the_big_city?utm_medium=copy_link'
driver = webdriver.Chrome(executable_path="C:\\Users\\tisk0\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

#ログイン
r_config = configparser.ConfigParser()
r_config.read('Config.ini')
ID = r_config.get('login', 'id')
PASSWORD = r_config.get('login', 'password')
driver.get('https://www.instagram.com/accounts/login/')
id_element = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
id_element.send_keys(ID)
password_element = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
password_element.send_keys(PASSWORD)
button_element = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)')
button_element.click()
time.sleep(5)

driver.get(url)
#プロフィール取得
profile_element = driver.find_element_by_class_name('-vDIg')
profile_elements =profile_element.find_elements_by_tag_name('span')
profile = profile_elements[1].get_attribute("textContent")
#print(profile)

#投稿URL取得
post1_element = driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a')
post1 = post1_element.get_attribute('href')
post2_element = driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a')
post2 = post2_element.get_attribute('href')

driver.get(post1)
number1_element = driver.find_element_by_css_selector('#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.EDfFK.ygqzn > div > div.Nm9Fw > a > span')
number1 = number1_element.get_attribute("textContent")
print(number1)
driver.get(post2)
number2_element = driver.find_element_by_css_selector('#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.EDfFK.ygqzn > div > div.Nm9Fw > a > span')
number2 = number2_element.get_attribute("textContent")
