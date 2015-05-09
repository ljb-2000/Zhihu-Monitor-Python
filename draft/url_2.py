# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'http://www.zhihu.com/topic/19767666'


session = requests.session()
response = session.get(url)
soup = BeautifulSoup(response.content)
urls = soup.find_all('a')

for url in urls:
    part_url = url['href']
    if part_url and part_url[0:20] == 'http://www.zhihu.com':
        print part_url
    elif part_url and part_url[0:10] == '/question':
        full_url = 'http://www.zhihu.com/' + part_url[0:18]
        print full_url
    elif part_url and part_url[0:7] == '/people':
        full_url = 'http://www.zhihu.com/' + part_url
        print full_url
    elif part_url and part_url[0:6] == '/topic':
        full_url = 'http://www.zhihu.com' + part_url
        print full_url
    else:
        None
