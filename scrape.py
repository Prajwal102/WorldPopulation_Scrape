import requests
from bs4 import BeautifulSoup as bs
import csv

url = requests.get("https://worldpopulationreview.com/#liveWorldPop").text

soup = bs(url,"lxml")

div = soup.find("div",class_="datatableStyles__TableContainer-bwtkle-0 dvLKHZ")
table = div.find("table")

th_arr = table.find_all('th')

headers = []
data = []

for e in th_arr:
    headers.append(e.find('a').getText().strip())


del headers[0]
del headers[1]

print(headers)

tbody = table.find('tbody')

tbody_tr = tbody.find_all('tr')



for tr in tbody_tr:
    dic = {}
    tbody_td = tr.find_all('td')
    dic['Country'] = tbody_td[1].find('a').getText()

    for i in range(1,len(headers)):
        dic[headers[i]] = tbody_td[i+2].getText()
    data.append(dic)
print(data[0])

with open("population_data.csv","w") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=headers)
    writer.writeheader()
    for d in data:
        writer.writerow(d)