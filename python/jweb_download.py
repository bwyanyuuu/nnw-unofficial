# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
from fillcontent import*
import time
from datetime import datetime
import os
import sys

# 儲存路徑
path = "../diary-resource"

# 預定義
nameMem = [None, "大吾", "流星", "米七", "恭平", "長尾", "丈君", "大橋"]
imgMem = [None, "nishihata", "onishi", "michieda", "takahashi", "nagao", "fujihara", "ohashi"]

def getHtml(url, headers):
    req = urllib.request.Request(url, headers = headers)
    page = urllib.request.urlopen(req)
    html = page.read().decode('UTF-8')
    return html

def getDiary(memidx, url, headers, findPre):
    dcnt = 0
    # 得到網頁本體
    html = getHtml(url, headers)
    if html == None:
        print("Something Wrong! Check Cookie!")
    soup = BeautifulSoup(html, "html.parser")

    # 判斷此 post 是否有下載過
    content = soup.find(class_="entry__date")
    day = content.text.split(" ")[0].split(".")
    day = [int(d) for d in day]
    daystr = "%02d%02d%02d" % (day[0] % 100, day[1], day[2])
    filename = "%s/%s %s.html" % (path, daystr, nameMem[memidx])
    
    if os.path.isfile(filename):
        print(filename + " already exist!")
        return 0
    else:
        print(filename + " downloading!")
        dcnt += 1

    # 找到以前所有 post
    if findPre == True:
        print("tr")
        content = soup.find(class_="back_number__list")
        content = content.find_all(class_="panel")
        for i in content:
            dcnt += getDiary(memidx, "https://www.johnnys-web.com" + i["href"], headers, False)
            time.sleep(2)

    # 下載日記中的圖片
    content = soup.find(class_="entry__body")
    img = content.find_all("img")
    cnt = 1
    for i in img:
        imgurl = "https://www.johnnys-web.com" + i['src']
        imgnn = "/" + daystr + "_" + imgMem[memidx] + "_" + str(cnt) + ".jpg"
        imgName = path + "/images" + imgnn
        html = html.replace(i['src'][i['src'].rfind('/'):], imgnn) 
        urllib.request.urlretrieve(imgurl, imgName)
        imgName = "../images/content" + imgnn
        urllib.request.urlretrieve(imgurl, imgName)
        cnt += 1
        
    # 更改網頁 static 檔案路徑到本地
    # 需要創建三個資料夾，並把常駐的檔案下載下來放進去
    content = soup.find_all("link")
    for c in content:
        if c['rel'][0] == "stylesheet":
            html = html.replace(c['href'][:c['href'].rfind("/")], "./assets/css")
        else:
            html = html.replace(c['href'][:c['href'].rfind("/")], "./images")
    content = soup.find_all("img")
    for i in content:
        html = html.replace(i['src'][:i['src'].rfind("/")], "./images")
    content = soup.find_all("script")
    for i in content:
        try:
            html = html.replace(i['src'][:i['src'].rfind("/")], "./assets/js")
        except:
            pass
    html = html.replace("/images/53/287/", "./images/")
    
    # 加入網頁
    n = '../diarya%d.html' % memidx
    d = open(n, 'r', encoding='utf-8')
    h = d.read()
    sd = BeautifulSoup(h, "html.parser")
    addDiarylist(daystr, sd)
    d.close()
    d = open(n, 'w', encoding='utf-8')
    d.write(sd.prettify(indent_width=4))
    d.close()

    

    # 儲存網頁
    fd = open(filename, "w", encoding="UTF-8")
    fd.write(html)
    fd.close()

    contentFile('../', daystr, memidx, filename)
    
    return dcnt
    
    

def main():
    if len(sys.argv) == 1:
        print("Usage: python jweb_download.py [mem index] [-a]\n-a\tDownload all contain past")
        exit()

    memidx = int(sys.argv[1])
    isAll = False
    if len(sys.argv) > 2 and sys.argv[2] == "-a":
        isAll = True

    # header 填入自己的 cookie
    userAgent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36 Edg/97.0.1072.69"
    cookies = "jwb_inbox_access=202204272059; 2982884DD3255EBE=108fbf4c9ca15ebb97c9a02967497028c9d8b5c5; S5SI=5kh1enjdbnk5kvujrgfn4mp5sn8es06k; _gid=GA1.2.946364478.1651323892; _gat_UA-138599890-11=1; _ga=GA1.2.453061115.1646057252; _ga_HSEHV5RVJR=GS1.1.1651323891.7.1.1651323917.0"
    headers = {'User-Agent': userAgent, 'Cookie': cookies}

    # 掃所有成員的所有日記
    cnt = 0
    if memidx == 0:
        for i in range(1, 8):
            url = "https://www.johnnys-web.com/s/jwb/diary/766/list?ct=%s" % i
            cnt += getDiary(i, url, headers, isAll)
            time.sleep(2)
    else:
        url = "https://www.johnnys-web.com/s/jwb/diary/766/list?ct=%s" % memidx
        cnt += getDiary(memidx, url, headers, isAll)
    # git push
    if cnt > 0:
        os.system('git add ..')
        x = datetime.now()
        os.system('git commit -m "%s" -m "daily update"' % x.strftime("%y%m%d-%H%M"))
        os.system('git push')

if __name__ == '__main__':
    main()
