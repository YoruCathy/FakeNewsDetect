wordlist1=[]
wordnum=[]
def process_read(txt):
        txt=txt.lower()
        for symbol in txt:
            if symbol in "\…“”‘’...~@#$%^&*()_-+=<>?!/,.:;{}[]|" :
                txt=txt.replace(symbol," ")
        global words
        words=txt.split()
        return words


path='C:/Users/70735/Desktop/dataset/gossipcop'
_path='C:/Users/70735/Desktop/news content.json'
import json
with open(_path,"r")as data:
    data=json.load(data)
import os
fake_file_list=os.listdir(path)

#-------------------------------------------------text词频
for fakenews in fake_file_list:
    news_path='C:/Users/70735/Desktop/dataset/gossipcop/{0}/news content.json'.format(fakenews)
    if open(news_path,"r"):
        with open(news_path,"r")as fake_news:
            fake_news=json.load(fake_news)   #fake_news dict
            print(fake_news['source'])
            print(fake_news['title'])
            txt=fake_news['text']   #新闻内容 #txt
            for word in process_read(txt):
                ##########可补充不计入统计的词汇（虚词等）
                if word not in['and','the','a','an','to','on','in','more','of','off','for','this','that','when','are','is','or','by','be','not','has','he','she','they','it','news','where','into','than','with','at','about','no','out','his','from','was','as','have','but','who','what','their','her','people','their','up','you','one','after','also']:
                    if len(word)!=1:
                        if word in wordlist1:
                            n=wordlist1.index(word)
                            wordnum[n]+=1
                        else:
                            wordlist1.append(word)
                            wordnum=wordnum+[1]


print(wordlist1)
print(wordnum)
fakewords=[]
fakewordsnum=[0]*20

for i in range(20):
    maxnum=max(wordnum)
    No=wordnum.index(maxnum)
    print(wordlist1[No])
    fakewords.append(wordlist1[No])
    print(wordnum[No])
    wordnum[No]=0
 # 输出20个数词频结果
print('\n')
print(fakewords)                ###假新闻词频最高的20个词汇
