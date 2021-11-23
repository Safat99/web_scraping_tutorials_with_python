##this is from the https://www.youtube.com/watch?v=t2k5Lsbpj8Y tutorials

import requests
from bs4 import BeautifulSoup
import os
import webbrowser
import argparse



#image.google.com link
googleimage = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&" 
data = "biriyani"

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}


search_url = googleimage + 'q=' + data
print(search_url)

response = requests.get(search_url, headers=usr_agent)
print("response status code ",response.status_code)

html = response.text
# print(html)

########### to open the html file with browser ############
# path = os.path.abspath('temp.html')
# with open(path, 'w') as f:
#     f.write(html)
# webbrowser.open(path)
#########################################################


soup = BeautifulSoup(response.content,'html.parser')
results = soup.findAll('img', {'class': 'rg_i'})
print(len(results))


