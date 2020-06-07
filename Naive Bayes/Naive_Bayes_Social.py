import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder
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

def gender_encoding(x):
    if (x == 'Female'):return 1
    else : return 0

def main():
    df = pd.read_csv("Social_Status.csv")
    
    '''
    Adding Encoding to Education and Gender 
    '''
    for ind,row in df.iterrows():
        df.loc[ind,"Cataegory"] = encoding(df.loc[ind,"Type"])
    df = df.astype({"Cataegory": int})

    for ind,row in df.iterrows():
        df.loc[ind,"Coded_Gender"] = gender_encoding(df.loc[ind,"Gender"])
    df = df.astype({"Coded_Gender": int})
    
    '''
    Creating training and Testing Data
    ''' 
    df = df[['Cataegory','Total','Coded_Gender']]
    X = df.drop(['Coded_Gender'],axis = 'columns')
    Y = df.Coded_Gender
    X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.1,random_state = 25) 
    
    '''
    Performing Naive Bayes with X = Cataegory and Total-Deaths , Y = Gender 
    '''
    gnb = GaussianNB()
    gnb.fit(X_train1,Y_train1)

    y_pred = gnb.predict(X_test1)
    print(y_pred)
    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(Y_test1, y_pred)*100)

    probabilities = gnb.predict_proba(X_test1)
    print(probabilities)
    print("Finished ......")


if __name__ == "__main__":
    main() 