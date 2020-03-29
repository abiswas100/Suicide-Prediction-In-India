
#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB 
from sklearn.model_selection import train_test_split
from sklearn import metrics 
import os 


'''
education level encoding
'''
def lvl_encoding(x):
    if(x == 'No Education'):
        return 0
    elif(x == 'Primary'):
        return 1
    elif(x == 'Middle'):
        return 2
    elif(x == 'Matriculate/Secondary'):
        return 3
    elif(x == 'Hr. Secondary/Intermediate/Pre-Universit'):
        return 4
    elif(x == 'Diploma'):
        return 5
    elif(x == 'Graduate'):
        return 6
    elif(x == 'Post Graduate and Above'):
        return 7
    else: return 8


def main():
    df = pd.read_csv("Education_Status.csv")

    cataegory = pd.Series([]) 
    for ind,row in df.iterrows():
        df.loc[ind,"Cataegory"] = lvl_encoding(df.loc[ind,"Type"])
    df = df.astype({"Cataegory": int})

    df = df.drop(['State','Year','Type_code','Type','Age_group'],axis='columns')
    df = df[['Cataegory','Total','Gender']]


    X = df.drop(['Gender'],axis='columns')
    Y = df.Gender

    #Performing Naive bayes

    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.1,random_state = 3)

    gnb = GaussianNB() 
    gnb.fit(x_train, y_train) 

    y_pred = gnb.predict(x_test)
    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
    print("Finished.....")


if __name__ == "__main__":
    main()