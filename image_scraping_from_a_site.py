import requests
from bs4 import BeautifulSoup

# link = "http://www.rmabd.org/"
link = "https://www.cuet.ac.bd/"
data = requests.get(link)

if data.status_code==200:
    print('successfully connected')

soup = BeautifulSoup(data.content,'html.parser')
i=1

for img in soup.find_all('img'):
    tmp = img.get('src')
    if tmp[:1] == "/":
        image = link + tmp # for the realative links
    else:
        image = tmp

    # print(image)
    # temp_name = img.get('alt')

    # if len(temp_name)==0:
    #     filename = str(i)
    #     i+=1
    # else:
    #     filename = temp_name

    filename = str(i)
    i+=1
    if i>=10:
        break
    with open('outputs/' + 'cuet_website_' + filename + '.jpeg','wb') as imagefile:
        imagefile.write(requests.get(image).content)