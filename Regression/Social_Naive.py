import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics  
import os
import csv
import streamlit as st

import new_Education as edu
import new_Professional as prof
import new_Social as social


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

def main():
    train = pd.read_csv('Social_train.csv')
    test = pd.read_csv('Social_test.csv')
    
    for ind,row in train.iterrows():
        train.loc[ind,"Type"] = encoding(train.loc[ind,"CATAEGORY"])
    train = train.astype({"Type": int})
    
    for ind,row in test.iterrows():
        test.loc[ind,"Type"] = encoding(test.loc[ind,"CATAEGORY"])
    test = test.astype({"Type": int})
    
    train_X = train.drop(['TOTAL-DEATHS','CATAEGORY'],axis='columns')
    train_Y = train['TOTAL-DEATHS']
    
    test_X = test.drop(['TOTAL-DEATHS','CATAEGORY'],axis='columns')
    test_Y = test['TOTAL-DEATHS']
    
    '''
    Performing Naive Bayes with X = Cataegory,Year and Total-Deaths , Y = probability 
    '''
    gnb = GaussianNB()
    gnb.fit(train_X,train_Y)

    y_pred = gnb.predict(test_X)
    print(y_pred)
    
    
    print("Done")
    
if __name__ == "__main__":
    main() 
    