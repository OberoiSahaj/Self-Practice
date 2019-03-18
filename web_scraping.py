# Just trying Web Scraping

import bs4 as bs
import urllib.request

link= urllib.request.urlopen("https://github.com/OberoiSahaj").read()  # link of site that has to be scraped
soup= bs.BeautifulSoup(link, features="html.parser") # Creating Beautiful Soup Object

#Here I am trying to scrape the Github contributions graph

graph= soup.find_all('div', class_='js-calendar-graph is-graph-loading graph-canvas calendar-graph height-full' )
print(graph) #When you create an empty html file and paste this output, you will obtain your github contributions