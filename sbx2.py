from bs4 import BeautifulSoup
import requests


def get_html():
    r = requests.get('https://prom.ua/Sportivnye-sumki') #Менять ссылку тут
    return r.text


soup = BeautifulSoup(get_html() , 'html.parser')
content = soup.find('div', class_='x-catalog__content-line')
last_try = content.find_all('div', class_='x-gallery-tile__content')
art_list = [] #Лист со статьями
i=0
for article in last_try:
    #name = article.find('a', class_='x-gallery-tile__name').text #тоже работает 
    name = article.find('span', {'itemprop': 'name'}).text

    price = article.find('div', class_='x-gallery-tile__price')['data-qaprice']
    link = article.find('a', class_='x-gallery-tile__name')['href']
    art_list.append([link,price,name])
print(art_list)
