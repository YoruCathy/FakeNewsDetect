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

print(np.mean(real_pol))
print(np.mean(real_sub))
print(np.mean(fake_pol))
print(np.mean(fake_sub))
"""
0.09431173611639185
0.37469315543155585
0.0614691342428349
0.42879508803864447
"""

# TODO:calculate mean and variance on gossip and political datasets
# TODO:write them into a txt file
