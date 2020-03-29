import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics  
import os


'''
SOcial Status Encoding
'''
def encoding(x):
    if (x == 'Never Married'):
        return 0
    elif(x == 'Married'):
        return 1
    elif(x == 'Seperated'):
        return 2
    elif(x == 'Divorcee'):
        return 3
    elif (x == 'Widowed/Widower'):
        return 4


df = pd.read_csv("Social_Status.csv")

cataegory = pd.Series([]) 
for ind,row in df.iterrows():
    df.loc[ind,"Cataegory"] = encoding(df.loc[ind,"Type"])
df = df.astype({"Cataegory": int})


df = df.drop(['State','Year','Type_code','Type','Age_group'],axis='columns')
df = df[['Cataegory','Total','Gender']]


X = df.drop(['Gender'],axis = 'columns')
Y = df.Gender

#Performing Naive Bayes

X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.1,random_state = 25) 

gnb = GaussianNB()
gnb.fit(X_train1,Y_train1)

y_pred = gnb.predict(X_test1)
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(Y_test1, y_pred)*100)
print("Finished ......")

 