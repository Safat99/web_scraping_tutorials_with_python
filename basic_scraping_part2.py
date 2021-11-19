from bs4 import BeautifulSoup
import requests

# link = "http://www.cuet.ac.bd/"
link = "https://www.kuet.ac.bd/department/CSE/index.php"
# link = "https://www.cuet.ac.bd/dept/mie/notice-board"
data = requests.get(link)
print("request status code {}".format(data.status_code))

if data.status_code ==200:
    print('request success!!\n')
else: 
    print('requets not found')
    exit()

soup = BeautifulSoup(data.content, 'html.parser')
# nav = soup.nav
# print(nav)
# print(type(nav))

if type(nav) is not None:
    for url in nav.find_all('a'):
        print('links of navbars are:\n\n')
        print(url.get('href'))
print()

body = soup.body 
for paragraph in body.find_all('p'):
    print(paragraph.text)

# for links in body.find_all('a'):
#     print(links.get('href'))

for div in soup.find_all('div', class_='body'):
    print(div.text)

#for finding the nav for kuet website...
for nav in soup.find_all('section', class_= 'menubar')
    print(nav.text)
