import requests
from bs4 import BeautifulSoup



for page in range(1, 7):
    URL = f'https://scrapingclub.com/exercise/list_basic/?page={page}'
    HOST = 'https://scrapingclub.com'

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')

    cards = soup.find_all('div', class_ = 'w-full rounded border')

    for card in cards:
        name = card.find('h4').text.strip()
        price = card.find('h5').text.strip()
        url_img = HOST + card.find('img', class_ = 'card-img-top img-fluid').get('src')

        print(name, price, url_img)
