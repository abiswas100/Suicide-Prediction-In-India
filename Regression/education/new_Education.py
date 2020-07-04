import pandas as pd
pd.options.mode.chained_assignment = None 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import csv

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
    

def find_indivitual_probability(df):
    
    a,b,c,d,e,f,g,h = 0,0,0,0,0,0,0,0
    for i, j in df.iterrows(): 
        if   j[1] ==  0: a = a + j[0]
        elif j[1] ==  1: b = b + j[0]
        elif j[1] ==  2: c = c + j[0]
        elif j[1] ==  3: d = d + j[0]
        elif j[1] ==  4: e = e + j[0]
        elif j[1] ==  5: f = f + j[0]
        elif j[1] ==  6: g = g + j[0] 
        elif j[1] ==  7: h = h + j[0]
    
    total = a+b+c+d+e+f+g+h
    
    prob_a = a/total
    prob_b = b/total
    prob_c = c/total
    prob_d = d/total
    prob_e = e/total
    prob_f = f/total
    prob_g = g/total
    prob_h = h/total
    
    return prob_a,prob_b,prob_c,prob_d,prob_e,prob_f,prob_g,prob_h,a,b,c,d,e,f,g,h


def main():
    df = pd.read_csv("Education.csv")
        
    Education_train = df.loc[(df['Year'] >= 2001) & (df['Year'] <= 2010)]
    Education_test = df.loc[(df['Year'] >= 2011) & (df['Year'] <= 2012)]
    
    '''
    Adding Encoding to Education and Gender 
    '''
    #Encoding Training Dataset
    for ind,row in Education_train.iterrows():
        Education_train.loc[ind,"Cataegory"] = encoding(Education_train.loc[ind,"Type"])
    Education_train= Education_train.astype({"Cataegory": int})
    #Encoding Testing Dataset
    for ind,row in Education_test.iterrows():
        Education_test.loc[ind,"Cataegory"] = encoding(Education_test.loc[ind,"Type"])
    Education_test = Education_test.astype({"Cataegory": int})

    Education_train = Education_train.drop(['State','Type','Type_code','Gender','Age_group'],axis='columns')
    Education_test = Education_test.drop(['State','Type','Type_code','Gender','Age_group'],axis='columns')
    
    group_Year = Education_train.groupby('Year') 
    group_Year_test = Education_test.groupby('Year')
    

    # #creating training dataset
    total_per_cataegory = []
    prob_per_cataegory = []
    
    for year in set(Education_train['Year']):
        grp = group_Year.get_group(year)
        prob_a,prob_b,prob_c,prob_d,prob_e,prob_f,prob_g,prob_h,a,b,c,d,e,f,g,h =  find_indivitual_probability(grp) 
        total_per_cataegory.append([a,b,c,d,e,f,g,h ])
        prob_per_cataegory.append([prob_a,prob_b,prob_c,prob_d,prob_e,prob_f,prob_g,prob_h])

    year = 2001
    with open('Education_train.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['YEAR','CATAEGORY','TOTAL-DEATHS','PROBABILITY'])
        for i in range(len(total_per_cataegory)):
            total_each_year = total_per_cataegory[i]
            prob_each_year = prob_per_cataegory[i]
            cataegory = ['No Education','Primary','Middle','Matriculate/Secondary','Hr. Secondary','Diploma','Graduate','Post-Grad or above']
            for j in range(len(total_each_year)):
                total = total_each_year[j]
                prob = prob_each_year[j]
                catae = cataegory[j]
                writer.writerow([year,catae,total,prob])    
            year = year + 1    
    
    #creating testing dataset
    total_per_cataegory_test = []
    prob_per_cataegory_test = []
    
    for y in set(Education_test['Year']):
        grp = group_Year_test.get_group(y)
        prob_a,prob_b,prob_c,prob_d,prob_e,prob_f,prob_g,prob_h,a,b,c,d,e,f,g,h =  find_indivitual_probability(grp) 
        total_per_cataegory_test.append([a,b,c,d,e,f,g,h ])
        prob_per_cataegory_test.append([prob_a,prob_b,prob_c,prob_d,prob_e,prob_f,prob_g,prob_h])

    year = 2011
    with open('Education_test.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(total_per_cataegory_test)):
            total_each_year = total_per_cataegory_test[i]
            prob_each_year = prob_per_cataegory_test[i]
            cataegory = ['No Education','Primary','Middle','Matriculate/Secondary','Hr. Secondary','Diploma','Graduate','Post-Grad or above']
            for j in range(len(total_each_year)):
                total = total_each_year[j]
                prob = prob_each_year[j]
                catae = cataegory[j]
                writer.writerow([year,catae,total,prob])    
            year = year + 1    


if __name__ == "__main__":
    main()