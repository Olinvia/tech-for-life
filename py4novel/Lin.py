import time
from requests_html import HTMLSession
import ssl
import requests_cache
import re
from bs4 import BeautifulSoup
import requests

ssl._create_default_https_context = ssl._create_unverified_context
# 定义会话Session
session = HTMLSession()
url = 'https://www.biquka2.com/Html/Book/101/101631/10427148.html'

with open('raw2.txt', 'a') as f:
    for i in range(200):
        r = session.get(url)

        all_text = r.text

        soup = BeautifulSoup(all_text, 'html.parser')

        div_data = ''.join(str(x) for x in soup.find('div', {'id': 'content'}).contents)
        print(div_data.encode("gbk", 'ignore').decode("gbk", "ignore"))

        # div_data = soup.find('div', {'id': 'content'})
        # print(div_data.get_text())
        f.write('第'+str(i)+'章')
        f.write(div_data.encode("gbk", 'ignore').decode("gbk", "ignore"))
        f.write('\n')

        list = []
        for name in r.html.find('a', containing='下一章', clean=True):
            list.append(name.attrs.get('href'))
        url = list[0]
        url = 'https://www.biquka2.com'+url
        time.sleep(1)
        print(url)

f.close()

