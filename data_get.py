from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import os
import time
wholesoup = []
def get_one(url):
    try:
        return urlopen(url,timeout=2).read()
    except:
        print("Again!!!")
        return get_one(url)

def get_total(uid,num,outputDir):
    for i in range(num):
        time.sleep(1)
        url = "https://api.bilibili.com/x/space/arc/search?mid="+ str(uid) +"&ps=30&tid=0&pn="+str(i+1)+"&keyword=&order=pubdate&jsonp=jsonp"
        print("[",i+1,"/"+ str(num) +"]")
        html = get_one(url)
        text = str(html.decode('utf-8'))
        f = open(outputDir + "/page"+str(i+1)+".json",'w')
        f.write(text)
        f.close()

get_total(54992199,36,"./guanshipin")
get_total(10330740,207,"./guancha")

