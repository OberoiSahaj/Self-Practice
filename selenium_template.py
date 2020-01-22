from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = ''
 
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
time.sleep(1)
page_source = driver.page_source
driver.quit() 

soup = BeautifulSoup(page_source, 'html.parser')
