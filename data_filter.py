import csv
from urllib.request import urlopen, Request
import time
import json

# https://api.bilibili.com/x/web-interface/archive/stat?bvid=BV1AC4y1W7zV

def get_one(url):
    try:
        return urlopen(url,timeout=2).read()
    except:
        print("Again!!!")
        return get_one(url)

class rawData:
    def __init__(self, aid, bvid, createdTime, title, length, description, play, comment, videoReview):
        self.aid = aid
        self.bvid = bvid
        self.createdTime = createdTime
        self.title = title
        self.length = length
        self.description = description
        if play == '--':
            play = 0
        self.play = play
        self.comment = comment
        self.videoReview = videoReview
        self.coin = 0
        self.danmaku = 0
        self.favorite = 0
        self.like = 0
        self.reply = 0
        self.share = 0
    def __str__(self):
        return str(self.aid) + '\t' + self.bvid + '\t' + str(self.createdTime) + '\t' + self.title + '\t' \
        + self.length + '\t' + self.description + '\t' + str(self.play) + '\t' + str(self.comment) + '\t' \
        + str(self.videoReview)+ '\t' + str(self.coin)+ '\t' + str(self.danmaku)+ '\t' + str(self.favorite )+ '\t' \
        + str(self.like) + '\t' + str(self.reply) + '\t' + str(self.share) + '\n'
    def __hash__(self):
        return hash(self.title)
    def search(self):
        time.sleep(1)
        url = "https://api.bilibili.com/x/web-interface/archive/stat?bvid=" + str(self.bvid)
        req = Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
        html = get_one(req)
        jsonObj = json.loads(html)
        self.coin = jsonObj['data']['coin']
        self.danmaku = jsonObj['data']['danmaku']
        self.favorite = jsonObj['data']['favorite']
        self.like = jsonObj['data']['like']
        self.reply = jsonObj['data']['reply']
        self.share = jsonObj['data']['share']
        print(self)
    def __eq__(self, value):
        return self.bvid == value.bvid
key_dict = [['王骁', '骁', '骁话一下'], ['董佳宁', '懂点儿啥'], ['张维为', '这就是中国', '维为'], ['丁一凡', '非同凡想'], ['王炳忠'], ['施佬胡诌', '施佬', '胡诌'], ['巴黎日记'], ['冷凇'], ['席亚洲', '亚洲特快'], ['大包', '科技战'], ['马前卒', '睡前消息', '督工'], ['余亮', '从书说起'], ['科技袁周虑', '科技袁人'], ['郑若麟', '又见法国', '又见'], ['陈平', '眉山论剑'], ['老马', '【也说】','也说：'], ['翟东升', '政经启翟']]

result = {'王骁': [], '董佳宁': [], '张维为': [], '丁一凡': [], '王炳忠': [], '施佬胡诌': [], '席亚洲': [], '大包': [], '马前卒': [], '余亮': [], '科技袁周虑': [], '郑若麟': [], '陈平': [], '老马': [] , '翟东升': [],'巴黎日记': [], '冷凇': [], '大包': [] }

def load(fileDir):
    fp = open(fileDir)
    reader = csv.reader(fp, delimiter='\t')
    header = next(reader)
    temp = []
    for row in reader:
        temp += [rawData(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])]
    return temp


gcz_ed = load('gczRaw.csv')
gsp_ed = load('gspRaw.csv')

for row in gsp_ed:
    for i in key_dict:
        key = i[0]
        for j in i:
            if j in row.title or j in row.description:
                try:
                    result[key] += [row]
                except:
                    pass
for row in gcz_ed:
    for i in key_dict:
        key = i[0]
        for j in i:
            if j in row.title or j in row.description:
                try:
                    result[key] += [row]
                except:
                    pass


output = open("./searched.csv",'w')
output.write('aid\tbvid\tcreated\ttitle\tlength\tdescription\tplay\tcomment\treview\tcoin\tdanmaku\tfavorite\tlike\treply\tshare\n')
for host in result:
    result[host] = list(set(result[host]))
    for video in result[host]:
        video.search()
        output.write(video.__str__())
output.close()


