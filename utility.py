import pandas as pd
import numpy as np

def readWords():
    df_words = pd.read_csv('TextPreprocessed (1).csv')
    text = ''
    for i in df_words['text']:
        text += str(i) + ' '
    words = text.split()
    words = set(words)
    words = list(words)
    return words



def text_Vect(text):
    words = readWords()
    temp = []
    for i in words :
        if i in text.split():
            temp.append(1)
        else:
            temp.append(0)
    return temp




