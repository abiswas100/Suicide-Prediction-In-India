import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB 
import os


df = pd.read_csv("Social_Status.csv")
df = df.drop(['State','Year','Type_code','Age_group'],axis = 1)

df  = df['Type'].replace({
    'Seperated' : 2,
    'Widowed/Widower' : 4,
    'Married' : 1, 
    'Divorcee' : 3,
    'Never Married' : 0
}, inplace = True)

print(df)

#Performing Naive Bayes

# X = df.drop(['Gender'],axis = 1)
# Y = df.Gender

# from sklearn.model_selection import train_test_split 
# X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.1) 

# gnb = GaussianNB()
# gnb.fit(X_train1,Y_train1)

print("Finished ......")