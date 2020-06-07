import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

    return prob_a,prob_b,prob_e,prob_d,prob_e    
    
def main():
    df = pd.read_csv("Social_Status.csv")


    df = df.drop(['State','Year','Type_code','Age_group'],axis='columns')


    social_types = df['Type'].unique()

    # print(type(social_types[0]))

    '''
    Adding Encoding to Education and Gender 
    '''
    for ind,row in df.iterrows():
        df.loc[ind,"Cataegory"] = encoding(df.loc[ind,"Type"])
    df = df.astype({"Cataegory": int})

    df = df.drop(['Type','Gender'],axis='columns')
    # Getting the Averages for each social types
            
    prob_a,prob_b,prob_c,prob_d,prob_e =  find_indivitual_probability(df)
    total_per_cataegory = []
    total_per_cataegory.append(prob_a)
    total_per_cataegory.append(prob_b)
    total_per_cataegory.append(prob_c)
    total_per_cataegory.append(prob_d)
    total_per_cataegory.append(prob_e)
        
    # print(df)
    
    model = LinearRegression()
    X = total_per_cataegory
    Y =  [0,1,2,3,4]
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=1/3)
    
    model.fit(x_train,y_train)
    
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

    plt.scatter(x_train,y_train,color = 'yellow')
    plt.plot(x_train,model.predict(x_train),color='green')


if __name__ == "__main__":
    main()




    
