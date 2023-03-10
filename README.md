# Sentiment Analysis of Twitter Data
This project is a Streamlit-based web application that performs sentiment analysis on tweets using the Naive Bayes algorithm. The purpose of this application is to determine the overall sentiment of a particular tweets on Twitter.

## Data
The data used in this project is a Twitter dataset that consists of tweets along with their sentiments (positive, negative, or neutral). This dataset was pre-processed to remove any irrelevant information.

## Methodology
The Naive Bayes algorithm was used for sentiment analysis. This algorithm is a probabilistic algorithm that makes classifications based on Bayes' theorem. The algorithm was trained on the Twitter dataset, and the model was then used to predict the sentiment of a given tweet.

## Prerequisites
You will need to have the following packages installed in order to run this project:
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- NLTK
- Streamlit
- 
## Deployment
> Checkout the Live application: https://anruthakamal-sentiment-analysis-app-msezey.streamlit.app/

## Installing
Use the following command to install all the required packages:
> pip install -r requirements.tx
## Usage
To use this application, simply clone the repository and run the following command in the terminal:

> streamlit run app.py

This will launch the web application in your default browser, and you can input a Twitter hashtag to perform sentiment analysis on. The results of the analysis will be displayed in the form of a pie chart, with the percentage of tweets classified as positive, negative, and neutral.

## Conclusion
In conclusion, this Sentiment Analysis of Twitter Data project demonstrates the capability of the Naive Bayes algorithm in performing sentiment analysis on a large dataset. This application can be used to determine the overall sentiment of a particular topic or hashtag on Twitter and can provide valuable insights into public opinion on a particular subject.
