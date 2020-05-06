import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from yellowbrick.text import TSNEVisualizer

data=pd.read_csv('../dataset/politi_data.csv')

data=data.fillna(' ')
data['total']=data['title']+' '+data['author']+data['text']

transformer = TfidfTransformer(smooth_idf=False)
count_vectorizer = CountVectorizer(ngram_range=(1,2))
counts = count_vectorizer.fit_transform(data['total'].values)
tfidf = transformer.fit_transform(counts)
targets = data['label'].values
x_train, x_test, y_train, y_test = train_test_split(counts, targets, random_state=0)

tsne = TSNEVisualizer()
tsne.fit(x_train,y_train)
tsne.show()