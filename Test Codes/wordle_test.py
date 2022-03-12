import re

import requests
from bs4 import BeautifulSoup


vgm_url = 'https://www.nytimes.com/games/wordle/index.html'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')


if __name__ == '__main__':
    data = soup.find_all('div')

    print(data)