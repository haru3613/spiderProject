import os
import sys
__dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dirname, '../lib'))
from _init_ import _init_


if __name__ is '__main__':
    init = _init_()
    resp = init.requests('get', 'https://www.ptt.cc/bbs/index.html')

    print(resp)