import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import (RandomForestClassifier, ExtraTreesClassifier,
                              AdaBoostClassifier)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import (LinearSVC,NuSVC)
from sklearn.metrics import roc_auc_score
import time
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
adaboost_decision_tree = AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=5)
adaboost_decision_tree.fit(x_train, y_train)
print('Acc of Ada boost on training set: {:.2f} \n'
               .format(adaboost_decision_tree.score(x_train, y_train)))
print('Acc of Ada boost on testing set: {:.2f}\n'
               .format(adaboost_decision_tree.score(x_test, y_test)))
print('auc is : {:.2f} \n'.format(roc_auc_score(y_test, adaboost_decision_tree.predict(x_test))))

adaboost_decision_tree = AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=5)
adaboost_decision_tree.fit(x_train, y_train)
print('Acc of Ada boost on training set: {:.2f} \n'
               .format(adaboost_decision_tree.score(x_train, y_train)))
print('Acc of Ada boost on testing set: {:.2f}\n'
               .format(adaboost_decision_tree.score(x_test, y_test)))
print('auc is : {:.2f} \n'.format(roc_auc_score(y_test, adaboost_decision_tree.predict(x_test))))