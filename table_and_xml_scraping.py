import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.cuet.ac.bd/dept/mie/notice-board"
data = requests.get(link)

print('data.status_code is {}'.format(data.status_code))

soup = BeautifulSoup(data.content, "html.parser")
table = soup.find('table') # if wanna find only the first table then table = soup.table 
# print(table)

table_rows = table.find_all('tr')
# print(table_rows)
tmp_df = []
columnss = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    # print(row)
    tmp_df.append(row)



for tr in table_rows:
    th = tr.find_all('th')
    # print(th)
    header =[i.text for i in th]
    columnss.append(header)

columnss = columnss[0] # keeping only the first row
tmp_df.pop(0) # since 0 index is an empty list because th is not in the frst row

# print(columnss)
# print(tmp_df) # printing as the list

df = pd.DataFrame(tmp_df, columns=columnss)
print(df)

try:
    dfs = pd.read_html(link, header=0)
    for df in dfs:
        print(df)

except:
    print('can\'t connect with pandas')


####---------------------------------for xml --------------------------
## reading from xml >> 

link2 = "https://pythonprogramming.net/sitemap.xml"
data2 = requests.get(link2)
soup = BeautifulSoup(data2.content,'xml')
for url in soup.find_all('loc'):
    print(url.text)