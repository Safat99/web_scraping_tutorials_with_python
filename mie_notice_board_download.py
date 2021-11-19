## i have checked that the pdf notices are inside a table... so i did this 

import requests
from bs4 import BeautifulSoup

mie_notice_board_url = "https://www.cuet.ac.bd/dept/mie/notice-board"
data = requests.get(mie_notice_board_url)

if data.status_code != 200:
    print('can\'t properly connect')
    print('status code {}'.format(data.status_code))

soup = BeautifulSoup(data.content,'html.parser')
table = soup.table
table_head = table.find('tr')
# print(table_head)
table_rows = table.find_all('tr')[1:]
# print(table_rows)

latest_notice_number = 0

for tr in table_rows:
    td = tr.find_all('td')
    for i in td:
        if latest_notice_number==5:
            break
        if i.a:
            if '.pdf' in i.a.get('href'):
                # print(i.a.get('href'))
                latest_notice_number +=1
                print("Downloading file: ", latest_notice_number)
                dwnld_link = mie_notice_board_url + '/../' + i.a.get('href')

                response = requests.get(dwnld_link)

                #writing content in pdf file
                pdf = open("latest_notice" + str(latest_notice_number) + ".pdf" , 'wb')
                pdf.write(response.content)
                pdf.close()
                print("file ", latest_notice_number, "downloaded")
    
print("latest 5 notice downloaded")


