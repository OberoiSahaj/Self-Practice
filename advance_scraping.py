from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import pandas as pd

basic_link= "https://www.lumendatabase.org/notices/search?utf8=%E2%9C%93&term={}&sort_by="
# x='youtube.com'
df = pd.read_csv('test.csv').values

#Class to obtain textual data from the link
class Get_text():
    def __init__(self,linkk):
        self.l= linkk
        driver.get(self.l)
        time.sleep(1)
        self.soup2 = BeautifulSoup(driver.page_source, "lxml")
        self.data = self.soup2.find_all(text=True)
    def visible(self, element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title', 'h1','h2','h3','h4', 'span', 'strong', 'yt','pre']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True

    def Result(self):
        self.result = filter(self.visible, self.data)
        self.final_res = [self.res.strip() for self.res in self.result]
        self.final_res = [self.res for self.res in self.final_res if self.res is not ""]
        return self.final_res

#Iterating in the lumen database to obtain the infringing links and get text of each link
for t in df:
    link = basic_link.format(t[0])
    print('\n ###### DATASET OF {} ######\n'.format(t[0]))
    driver = webdriver.Chrome("C:\\Users\\Sahaj Oberoi\\Desktop\\Naxap\\chromedriver.exe")
    driver.get(link)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "lxml")
    data = soup.find_all('li', class_='excerpt')

    for i in data:
        linkk = '{}'.format(str(i.text))
        print(linkk.strip())
    print("\n ###### TEXTUAL DATA ###### \n")
    # for i in data:
    #     linkk = '{}'.format(str(i.text))
    #     txt = Get_text(linkk)
    #     print(txt.Result())
    #     del txt

