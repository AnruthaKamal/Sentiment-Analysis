import pickle
import pandas as pd
import utility
import TextPreprocess
import model
import  streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(menu_title='Main Menu',options=['About','Check Score'])
if selected == 'About':
    st.title('WELCOME ')
    intro = """<!DOCTYPE html>
    <html>
    <head>
    <title>SENTIMENT ANALYSER</title>
    </head>
    <body>
    <h1>SENTIMENT ANALYSER</h1>
    <p style="font-family:Trebuchet MS;">Sentiment analysis is a field dedicated to extracting subjective emotions and feelings from text. One common use of sentiment analysis is to figure out if a text expresses negative or positive feelings.</p>
    <h2>How to check ?</h2>
    <ol>
    <li>Enter Text</li>
    <li>Click to view tone </li>
    </ol>
    </body>
    </html>"""
    st.components.v1.html(intro, width=None, height=600, scrolling=True)

else :
    st.title('Get Started ... ')
    text = st.text_input('text')
    t1 = TextPreprocess.TextPreprocesing(text)
    vect = utility.text_Vect(t1)
    label = model.predict([vect])
    if label == 1:
        tone = 'POSITIVE'
    elif label == 0 :
        tone = 'NEUTRAL'
    else :
        tone = 'NEGATIVE'
    if st.button('CHECK TONE '):
        st.write('TONE IS ',tone)
