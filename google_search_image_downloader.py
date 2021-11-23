##this is from the https://www.youtube.com/watch?v=t2k5Lsbpj8Y tutorials
## for more https://www.youtube.com/watch?v=YEUbMnMqJG0 tutorial is also helpful for bulk image
## with this code we can download around 100 image in a single html parsing

from bs4.builder import TreeBuilderRegistry
from bs4.dammit import html_meta
import requests
from bs4 import BeautifulSoup
import os
import webbrowser
import argparse

parser = argparse.ArgumentParser(description='finding and downloading image from google search below 100')
parser.add_argument('-s', '--search', required=True, help='keyword of the image_search')
parser.add_argument('-n', '--number', required=False, help='number of images to download within 100')
args = vars(parser.parse_args())


#image.google.com link
googleimage = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&" 
# data = "biriyani"
data = args['search']

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}


def search_image():
    search_url = googleimage + 'q=' + data
    print(search_url)
    print('connecting....')
    response = requests.get(search_url, headers=usr_agent)
    print("response status code ",response.status_code)

    if response.status_code == 200:
        print('Successfully connected!!')
    else:
        print('response code is not 200')

    html = response.text
    # print(html)
    return response

########### to open the html file with browser ############
def see_html():
    html = search_image().text
    path = os.path.abspath('temp.html')
    with open(path, 'w') as f:
        f.write(html)
    webbrowser.open(path)
#########################################################


def parse_html():
    response = search_image()
    soup = BeautifulSoup(response.content,'html.parser')
    results = soup.findAll('img', {'class': 'rg_i'})
    print('total {} images found!!'.format(len(results)))

    return results

download_folder = 'outputs/googleimage'
def download_image():
    if not os.path.exists(download_folder):
        os.mkdir(download_folder)

    count = 0
    imagelinks = []
    results = parse_html()
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count += 1
            if (count>= int(args['number'])):
                break
            
        except KeyError:
            continue
    
    print('Found {} imageLinks'.format(len(imagelinks)))
    print('Start Downloading...')

    for i,j in enumerate(imagelinks):
        response_img  = requests.get(j)

        #file writing operation
        imagename = download_folder + '/' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as img:
            img.write(response_img.content)
        
        print('Downloading {} {} image'.format(i+1,args['search']))
    
    print('Download Complete!!')



if __name__ == '__main__':
    # see_html()
    # parse_html()
    download_image()
