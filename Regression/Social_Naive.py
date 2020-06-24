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


def main():
    train = pd.read_csv('Social_train.csv')
    test = pd.read_csv('Social_test.csv')
    
    train_X = train['YEAR','TOTAL-DEATHS']
    train_Y = train['PROBABILITIES']
    
    test_X = test['YEAR','TOTAL-DEATHS']
    test_Y = train['PROBABILITIES']

    '''
    Performing Naive Bayes with X = Cataegory and Total-Deaths , Y = Gender 
    '''
    gnb = GaussianNB()
    gnb.fit(train_X,train_Y)

    y_pred = gnb.predict(test_X)
    print(y_pred)
    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(test_Y, y_pred)*100)

    probabilities = gnb.predict_proba(test_X)
    
    print(probabilities)

if __name__ == "__main__":
    main() 
    