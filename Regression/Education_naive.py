import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics  
import csv

import new_Education as edu
import new_Professional as prof
import new_Social as social

def encoding(x):
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
    
    print("Done")
    