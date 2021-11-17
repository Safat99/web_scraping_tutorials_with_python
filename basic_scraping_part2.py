from bs4 import BeautifulSoup
import requests

link = "http://www.cuet.ac.bd/"
data = requests.get(link)

if requests.status_code ==200:
    print('request success!!')

    soup = BeautifulSoup(data.content, 'html.parser')
    
