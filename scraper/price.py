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
    items = soup.find_all('div',attrs={'data-index':re.compile(r'^[0-9]*')})
    print(len(items))
    item_name  = []
    image = []
    price = []

    for i in range(len(items)):
        dic = {}
        if items[i].find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'}) is None:
            continue
        name = items[i].find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'}).get_text()
        # tag = quote[i].find('span',attrs={'class':'text'}).get_text()
        item_name.append(name)
        print(name)
    for i in range(len(items)):
        dic = {}
        if items[i].find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'}) is None:
            continue
        img = items[i].find('img')['src']
        # tag = quote[i].find('span',attrs={'class':'text'}).get_text()
        image.append(img)
        print(img)
    for i in range(len(items)):
        dic = {}
        if items[i].find('span',attrs={'class':'a-price'}) is None:
            continue
        p = items[i].find('span', attrs={'class':'a-offscreen'}).get_text()
        # tag = quote[i].find('span',attrs={'class':'text'}).get_text()
        price.append(p)
    return item_name, image, price

def update(url, htmlDoc):
    # htmlDoc = open('./templates/quotes.html',"r+")
    soup = BeautifulSoup(htmlDoc)
    text, image, price  = content(url)
    a = soup.find_all('p')
    for i in range(len(a)):
        a[i].string = a[i].text.replace(a[i].text, text[i])
    b = soup.find_all('h3')
    for j in range(len(b)):
        b[j].string = b[j].text.replace(b[j].text,str(j))
    img = soup.find_all('img')
    for i in range(len(img)):
        img[i]['src'] = image[i]
    pri = soup.find_all('span', attrs={'class':'price'})
    for i in range(len(pri)):
        pri[i].string = pri[i].text.replace(pri[i].text, price[i])
	
    print(soup)
    html = soup.prettify('utf-8')
    with open('./Lib/site-packages/templates/priceout.html','wb') as file:
        file.write(html)
    return soup

#content('https://www.amazon.com/s?k=computer/1/')
#update('https://www.amazon.com/s?k=computer', open('../templates/quotes.html',"r+"))