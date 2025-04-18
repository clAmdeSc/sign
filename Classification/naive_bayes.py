# -*- coding: utf-8 -*-
"""Naive Bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N49R_IMaVgpkXQmGR5tsZM1FfBWBktnr
"""

import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sbn
from sklearn.metrics import confusion_matrix

data=pd.read_csv(r'Code\Classification\csv files\train.csv',low_memory=False)
data.head()

x=data.iloc[:,0:150]
y=data.iloc[:,-1]

le=LabelEncoder()
y=le.fit_transform(y)

GaussNB=GaussianNB()
print("Naive Bayes Started!")
GaussNB.fit(x,y)
print("Naive Bayes Finished !")

test=pd.read_csv(r'Code\Classification\csv files\test.csv',low_memory=False)

x_test=test.iloc[:,0:150]
y_test=test.iloc[:,-1]

x_test.head()

y_test=le.fit_transform(y_test)
print(y_test)
x_test.shape

y_expect=y_test
y_pred=GaussNB.predict(x_test)

print(accuracy_score(y_expect,y_pred))

MultiNB=MultinomialNB()
print("Naive Bayes Started!")
MultiNB.fit(x,y)
print("Naive Bayes Finished !")

y_expect=y_test
y_pred=MultiNB.predict(x_test)

print(accuracy_score(y_expect,y_pred))

BernNB=BernoulliNB(binarize=True)
print("Naive Bayes Started!")
BernNB.fit(x,y)
print("Naive Bayes Finished !")

y_expect=y_test
y_pred=BernNB.predict(x_test)

print(accuracy_score(y_expect,y_pred))

c_m=confusion_matrix(y_test,y_pred)

df_cm=pd.DataFrame(c_m)

plt.figure(figsize=(20,17))
plt.title("Confusion Matrix for Gaussian Naive Bayes")
sbn.heatmap(df_cm,annot=True)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

