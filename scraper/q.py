from bs4 import BeautifulSoup
import requests
import time
import re

def get_page(url):
    session = requests.session()
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    headers={"User-Agent":user_agent}
    res = session.get(url, headers=headers)
    return res
    print(res.text)

def content(url):
    wb_data = get_page(url)
    soup =BeautifulSoup(wb_data.text, 'lxml')
    quote = soup.find_all('div',attrs={'class':'quote'})
    print(len(quote))
    t  = []

    for i in range(len(quote)):
        dic = {}
        text = quote[i].find('span',attrs={'class':'text'}).get_text()
        # tag = quote[i].find('span',attrs={'class':'text'}).get_text()
        t.append(text)
    return t

def update(url, htmlDoc):
    # htmlDoc = open('./templates/quotes.html',"r+")
    soup = BeautifulSoup(htmlDoc)
    text  = content(url)
    a = soup.find_all('p')
    for i in range(len(a)):
        a[i].string = a[i].text.replace(a[i].text, text[i])
    b = soup.find_all('h3')
    for j in range(len(b)):
        b[j].string = b[j].text.replace(b[j].text,str(j))
    print(soup)
    html = soup.prettify('utf-8')
    with open('./Lib/site-packages/templates/quotesout.html','wb') as file:
        file.write(html)
    return soup

