import os
import sys
__dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dirname, '../lib'))
from _init_ import _init_

from bs4 import BeautifulSoup
import io
import time


if __name__ is '__main__':
    init = _init_()
    resp = init.requests('get', 'https://www.dcard.tw/f')
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    for element in soup.findAll('a', {'class': 'sc-1v1d5rx-3 kPUUNB'}):
        # print(element.get('href'))
        url = 'https://www.dcard.tw' + element.get('href')

        resp = init.requests('get', url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            title = soup.find('h1')
            print(title.text)