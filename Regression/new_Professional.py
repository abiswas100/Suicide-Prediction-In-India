import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def encoding(x):    
    if (x == 'Professional Activity' or x == 'Service (Private)' or x == 'Self-employed (Business activity)' or x == 'Service (Government)' or x == 'Public Sector Undertaking' or x == 'Farming/Agriculture Activity'):
        return 2        #Employed
    elif (x == 'Student' or x == 'House Wife' or x == 'Unemployed' or x == 'Others (Please Specify)'):
        return 1         #Unemployed
    else : return 0


def find_indivitual_probability(df):
    a,b,c = 0,0,0
    for i, j in df.iterrows(): 
        if   j[1] ==  0: a = a + j[0]
        elif j[1] ==  1: b = b + j[0]
        elif j[1] ==  2: c = c + j[0]
    print(a,b,c)
    total = a+b+c
    
    prob_a = a/total
    prob_b = b/total
    prob_c = c/total
    
    print(prob_a,prob_b,prob_c)
    
    return prob_a,prob_b,prob_c    

def main():
    df = pd.read_csv("Professional.csv")
    
    df = df.drop(['State','Year','Type_code','Age-group'],axis = 'columns')
    
    Professional_train = df.loc[(df['Year'] >= 2001) & (df['Year'] <= 2010)]
    Professional_test = df.loc[(df['Year'] >= 2011) & (df['Year'] <= 2012)]
    
    
    '''
    Adding Encoding to Education and Gender 
    '''
    for ind,row in Professional_train.iterrows():
        Professional_train.loc[ind,"Cataegory"] = encoding(df.loc[ind,"Type"])
    Professional_train = Professional_train.astype({"Cataegory": int})

    Professional_train = Professional_train.drop(['Type','Gender'],axis='columns')
    # Getting the Averages for each social types
            
    prob_a,prob_b,prob_c =  find_indivitual_probability(df)
    total_per_cataegory = []
    total_per_cataegory.append(prob_a)
    total_per_cataegory.append(prob_b)
    total_per_cataegory.append(prob_c)
    
    