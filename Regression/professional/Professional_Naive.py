import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics  
import csv

import new_Professional as prof

def encoding(x):    
    
    if ( x == 'Unemployed'):
        return 0
    elif(x == 'Farming/Agriculture'):
        return 1
    elif(x == 'Government Service'):
        return 2
    elif(x == 'Private Sector'):
        return 3
    elif (x == 'Self-Employed or Other Activity'):
        return 4    
        

def main():
    train = pd.read_csv('Professional_train.csv')
    test = pd.read_csv('Professional_test.csv')
    
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
    