from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import (RandomForestClassifier, ExtraTreesClassifier,
                              AdaBoostClassifier)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import (LinearSVC,NuSVC,SVC)
from sklearn.metrics import roc_auc_score
import time
import numpy as np

data=pd.read_csv('../dataset/politi_data.csv')

data=data.fillna(' ')
data['total']=data['title']+' '+data['author']+data['text']

transformer = TfidfTransformer(smooth_idf=False)
count_vectorizer = CountVectorizer(ngram_range=(1,2))
counts = count_vectorizer.fit_transform(data['total'].values)
tfidf = transformer.fit_transform(counts)

targets = data['label'].values
x_train, x_test, y_train, y_test = train_test_split(counts, targets, random_state=0)

current_time=time.strftime('%m-%d-%H-%M-%S',time.localtime(time.time()))
with open('grid_{}.txt'.format(current_time),'w') as log_file:
    param_grid = {'C': [x for x in np.arange(1,2,0.1)], 'gamma': [1, 0.1], 'kernel': ['rbf']}
    grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)
    grid.fit(x_train, y_train)
    print(grid.best_estimator_)
