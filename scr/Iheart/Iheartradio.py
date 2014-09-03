#!/usr/bin/env python3
"""
__author__ = 'boss'



"""
 from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen





Station = input('Please enter web address:  ')
user_agent = '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
                       (KHTML, like Gecko)  Chrome/37.0.2062.94 Safari/537.36'''

req = Request('http://http://www.iheart.com/search/?q=' + Station)

reponse = urlopen(req)
headers = reponse.info()


print(reponse, headers)
