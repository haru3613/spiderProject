import requests
from logger import logger

class _init_(object):
    def __init__(self):
        self.SESSION = requests.Session()        
        self.logger = logger("CURL")

        self.SESSION.headers.update({
            'content-type': 'application/json',
            'accept': 'application/json',
        })


    def requests(self, method, host, append='', **kwargs):
        ''' method:
                e.g.: get post patch delete
            append:
                e.g.: /<path>
            **kwargs:
                e.g.: data={"name":"test"} or json={"name":"test2"}
        '''
        url = host + append
        # self.logger.log_pattern(url, locals()["kwargs"], self.SESSION.headers, method)
        resp = self.SESSION.request(method, url, **kwargs)
        return resp