import json




class rawData:
    def __init__(self, aid, bvid, createdTime, title, length, description, play, comment, videoReview):
        self.aid = aid
        self.bvid = bvid
        self.createdTime = createdTime
        self.title = title
        self.length = length
        self.description = description
        self.play = play
        self.comment = comment
        self.videoReview = videoReview
        self.coin = 0
        self.danmaku = 0
        self.favorite = 0
        self.like = 0
        self.reply = 0
        self.share = 0



output = open("./gspRaw.csv",'w')
output.write('aid\tbvid\tcreated\ttitle\tlength\tdescription\tplay\tcomment\treview\tcoin\tdanmaku\tfavorite\tlike\treply\tshare\n')

for i in range(36):
    fp = open('./guanshipin/page'+ str(i+1) +'.json')
    raw = json.load(fp)
    for i in range(30):
        try:
            temp = raw['data']['list']['vlist'][i]
            des = temp['description'].replace('\r','\n')
            output.write(str(temp['aid']) + '\t' + temp['bvid'] + '\t' + str(temp['created']) + '\t' + temp['title'] + '\t' + temp['length'] + '\t' + des.replace('\n',' ') + '\t' + str(temp['play']) + '\t' + str(temp['comment'] )+ '\t' + str(temp['video_review'] )+ '\t' + '0' + '\t' + '0' + '\t' + '0' + '\t' + '0' + '\t' + '0' + '\t' + '0' + '\n')
        except:
            pass
output.close()

output = open("./gczRaw.csv",'w')
output.write('aid\tbvid\tcreated\ttitle\tlength\tdescription\tplay\tcomment\treview\tcoin\tdanmaku\tfavorite\tlike\treply\tshare\n')
for i in range(207):
    fp = open('./guancha/page'+ str(i+1) +'.json')
    raw = json.load(fp)
    for i in range(30):
        try:
            temp = raw['data']['list']['vlist'][i]
            des = temp['description'].replace('\r','\n')
            output.write(str(temp['aid']) + '\t' + temp['bvid'] + '\t' + str(temp['created']) + '\t' + temp['title'] + '\t' + temp['length'] + '\t' + des.replace('\n',' ') + '\t' + str(temp['play']) + '\t' + str(temp['comment'] )+ '\t' + str(temp['video_review'] )+ '\t' + '0' + '\t' + '0' + '\t' + '0' + '\t' + '0' + '\t' + '0' + '\t' + '0' + '\n')
        except:
            pass
output.close()
