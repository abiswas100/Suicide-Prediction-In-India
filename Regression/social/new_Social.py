import pandas as pd
pd.options.mode.chained_assignment = None 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import csv

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

def find_indivitual_probability(train):
    a,b,c,d,e = 0,0,0,0,0
    # print(train)
    for i, j in train.iterrows():
        if   j[2] ==  0: a = a + j[1]
        elif j[2] ==  1: b = b + j[1]
        elif j[2] ==  2: c = c + j[1]
        elif j[2] ==  3: d = d + j[1]
        elif j[2] ==  4: e = e + j[1]

    total = a+b+c+d+e
    prob_a = a/total
    prob_b = b/total
    prob_c = c/total
    prob_d = d/total
    prob_e = e/total
    
    return prob_a,prob_b,prob_c,prob_d,prob_e,a,b,c,d,e   
    
def main():
    df = pd.read_csv("Social.csv")
          
    Social_train = df.loc[(df['Year'] >= 2001) & (df['Year'] <= 2010)]
    Social_test = df.loc[(df['Year'] >= 2011) & (df['Year'] <= 2012)]
       
    '''
    Adding Encoding to Education and Gender 
    '''
    for ind,row in Social_train.iterrows():
        Social_train.loc[ind,"Cataegory"] = encoding(Social_train.loc[ind,"Type"])
    Social_train = Social_train.astype({"Cataegory": int})
    
    for ind,row in Social_test.iterrows():
        Social_test.loc[ind,"Cataegory"] = encoding(Social_test.loc[ind,"Type"])
    Social_test = Social_test.astype({"Cataegory": int})
    
    
    Social_train = Social_train.drop(['State','Type','Type_code','Gender','Age_group'],axis='columns')
    Social_test = Social_test.drop(['State','Type','Type_code','Gender','Age_group'],axis='columns')
        
    group_Year = Social_train.groupby('Year')
    group_Year_test = Social_test.groupby('Year')
    
    total_per_cataegory = []
    prob_per_cataegory = []
    
    for year in set(Social_train['Year']):
        grp = group_Year.get_group(year)
        prob_a,prob_b,prob_c,prob_d,prob_e ,a,b,c,d,e =  find_indivitual_probability(grp) 
        total_per_cataegory.append([a,b,c,d,e])
        prob_per_cataegory.append([prob_a,prob_b,prob_c,prob_d,prob_e])

    year = 2001
    with open('Social_train.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['YEAR','CATAEGORY','TOTAL-DEATHS','PROBABILITY'])
        for i in range(len(total_per_cataegory)):
            total_each_year = total_per_cataegory[i]
            prob_each_year = prob_per_cataegory[i]
            cataegory = ['Never Married','Married','Seperated','Divorcee','Widowed/Widower']
            for j in range(len(total_each_year)):
                total = total_each_year[j]
                prob = prob_each_year[j]
                catae = cataegory[j]
                writer.writerow([year,catae,total,prob])    
            year = year + 1    
    # print(Social_test) 
    
    total_per_cataegory_test = []
    prob_per_cataegory_test = []
    
    for year_test in set(Social_test['Year']):
        grp = group_Year_test.get_group(year_test)
        prob_a,prob_b,prob_c,prob_d,prob_e ,a,b,c,d,e =  find_indivitual_probability(grp) 
        total_per_cataegory_test.append([a,b,c,d,e])
        prob_per_cataegory_test.append([prob_a,prob_b,prob_c,prob_d,prob_e])
    
    year = 2011
    with open('Social_test.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['YEAR','CATAEGORY','TOTAL-DEATHS','PROBABILITY'])
        for i in range(len(total_per_cataegory_test)):
            total_each_year = total_per_cataegory_test[i]
            prob_each_year = prob_per_cataegory_test[i]
            cataegory = ['Never Married','Married','Seperated','Divorcee','Widowed/Widower']
            for j in range(len(total_each_year)):
                total = total_each_year[j]
                prob = prob_each_year[j]
                catae = cataegory[j]
                writer.writerow([year,catae,total,prob])    
            year = year + 1    


if __name__ == "__main__":
    main()




    
