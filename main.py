import requests
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent

HEADERS = {'User-Agent': UserAgent().random}
HOST = 'https://scrapingclub.com'



def get_url():
    for page in range(1, 7):
        URL = f'https://scrapingclub.com/exercise/list_basic/?page={page}'

        print(f'Собираю страницу: {page}')

        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')
        cards = soup.find_all('div', class_ = 'w-full rounded border')

        for card in cards:
            card_url = HOST + card.find('a').get('href')
            yield card_url



def make_array():
    for card_url in get_url():
        response = requests.get(card_url, headers=HEADERS)
        # sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')
        card = soup.find('div', class_ = 'my-8 w-full rounded border')

        name = card.find('h3', class_ = 'card-title').text.strip()
        price = card.find('h4', class_ = 'my-4 card-price').text.strip()
        description = card.find('p', class_ = 'card-description').text.strip()
        img_url = HOST + card.find('img', class_ = 'card-img-top').get('src')

        print('Собрал карточку')

        download(img_url)

        yield name, price, description, img_url


def download(url):
    response = requests.get(url, stream=True, headers=HEADERS)
    with open(r'D:\\Code\\Scraping\\images\\' + url.split('/')[-1], 'wb') as f:
        for value in response.iter_content(1024*1024):
            f.write(value)

