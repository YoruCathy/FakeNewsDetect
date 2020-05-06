from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd

data='D:/FakeNewsBackup/dataset/politi_data.csv'
content=pd.read_csv(data)
text=content['text']
title=content['title']
label=content['label']

real_pol=[]
real_sub=[]
fake_pol=[]
fake_sub=[]
for i,_ in tqdm(enumerate(text)):
    if label[i]==0:
        blob=TextBlob(text[i])
        real_pol.append(blob.sentiment.polarity)
        real_sub.append(blob.sentiment.subjectivity)
    else:
        blob = TextBlob(text[i])
        fake_pol.append(blob.sentiment.polarity)
        fake_sub.append(blob.sentiment.subjectivity)

fig, ax = plt.subplots()
_, _, _ = ax.hist(real_pol, 50, alpha=0.4,label='real',color='pink')
_, _, _ = ax.hist(fake_pol, 50, alpha=0.4,label='fake',color='skyblue')
fig.tight_layout()
plt.xlabel('polarity')
plt.ylabel('frequency')
plt.legend()
plt.show()

fig, ax = plt.subplots()
_, _, _ = ax.hist(real_sub, 50, alpha=0.4,label='real',color='pink')
_, _, _ = ax.hist(fake_sub, 50, alpha=0.4,label='fake',color='skyblue')
fig.tight_layout()
plt.xlabel('subjectivity')
plt.ylabel('frequency')
plt.legend()
plt.show()