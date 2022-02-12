
from bs4 import BeautifulSoup
import random
import re
orig_prettify = BeautifulSoup.prettify
r = re.compile(r'^(\s*)', re.MULTILINE)
def prettify(self, encoding=None, formatter="minimal", indent_width=4):
    return r.sub(r'\1' * indent_width, orig_prettify(self, encoding, formatter))
BeautifulSoup.prettify = prettify
f = open("./diary-template.html")
html = f.read()
li = [1, 2, 3, 4, 5, 6, 7]
for i in range(1, 8):
    soup = BeautifulSoup(html, "html.parser")
    soup.find('html')['id'] = 'nnw%d' % i
    soup.find('img', class_='diary-img')['src'] = './images/diary/nnw%d-1.png' % i
    d = soup.find_all('div', class_='diary-imglist')
    random.shuffle(li)
    cnt = 0
    for j in range(7):
        if i != li[j]:
            d[cnt]['href'] = './diarya%d.html' % li[j]
            d[cnt]['id'] = 'm%d' % li[j]
            d[cnt].find('img')['src'] = './images/diary/m%d.png' % li[j]
            cnt += 1
    file = './diarya%d.html' % i
    ff = open(file, 'w')
    ff.write(soup.prettify(indent_width=4))
