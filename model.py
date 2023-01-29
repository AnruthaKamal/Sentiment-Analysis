import pandas as pd
import numpy as np
import utility
from sklearn.naive_bayes import MultinomialNB
def Get_Data():
    df_train = pd.read_csv('TextPreprocessed (1).csv')
    words = utility.readWords()
    X = []
    for i in df_train['text']:
        temp = []
        for j in words :
            if j in str(i).split():
                temp.append(1)
            else:
                temp.append(0)
        X.append(temp)
    return X


def Model():
    X =  Get_Data()
    df =  pd.read_csv('TextPreprocessed (1).csv')
    Y = df['category']
    clf = MultinomialNB(alpha=0.5)
    clf.fit(X, Y)
    return clf

def predict(vect):
    classifier = Model()
    return classifier.predict(vect)
