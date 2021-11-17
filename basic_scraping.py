### this is from the sentdex vdo tutorial of web sracping and parsing with BeautifulSoup part 1
## this covers getting all the links, paragraphs and text from a website...

from bs4 import BeautifulSoup
import requests


#download a page
page = "http://www.cuet.ac.bd/" #page name
result = requests.get(page)

if result.status_code==200:
    soup = BeautifulSoup(result.content, 'html.parser')

# to find the title
title = soup.title.text
print("title is >> {}".format(title))

#to find all the paragraph
# print(soup.find_all('p')) # for string doesn't return empty string

#to find the first paragraph
#print(soup.p)

for paragraph in soup.find_all('p'):
    print(paragraph.text)


print('\n\n\n\n')
# print(soup.find_all('p')) # for text, return empty string
for paragraph in soup.find_all('p'):
    print(paragraph.string) ## string e onek kisu miss hoy

## string er kaaj na korar karon hocche ...paragraph er vetor child tag thakle segula kaaj kore na string e ....
## like span tag use kori amra...egula string e dhorbe na...jegula navigable se kebol oigulai dhorbe

print('\n\n\n\n')
## now jodi amra all jinish pati chai... not only just the paragraph tag...tokhon eta korbo
print(soup.get_text())

## for finding all the links::
for url in soup.find_all('a'):
    # print(url.text)  #eta dile amar shob gula link er moddhekar text gula ashbe...
    print(url.get('href'))
