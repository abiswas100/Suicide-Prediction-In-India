import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



def find_indivitual_probability(df):
    a,b,c,d,e = 0,0,0,0,0
    for i, j in df.iterrows(): 
        if   j[1] ==  0: a = a + j[0]
        elif j[1] ==  1: b = b + j[0]
        elif j[1] ==  2: c = c + j[0]
        elif j[1] ==  3: d = d + j[0]
        elif j[1] ==  4: e = e + j[0]
    print(a,b,c,d,e)
    total = a+b+c+d+e
    
    prob_a = a/total
    prob_b = b/total
    prob_c = c/total
    prob_d = d/total
    prob_e = e/total
    
    print(prob_a,prob_b,prob_c,prob_d,prob_e)
    
    
    
def main():
    df = pd.read_csv("Education_Status.csv")
    
    df = df.drop(['State','Year','Type_code','Age_group'],axis = 'columns')
    
    
    pass