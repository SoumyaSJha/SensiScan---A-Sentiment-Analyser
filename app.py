from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import re
import nltk
import re, string, nltk
from sklearn.feature_extraction.text import CountVectorizer
from utils import tokenize
app = Flask(__name__)

# Load the SVM sentiment analysis model
with open('model.pickle', 'rb') as file:
    vectorizer, model = pickle.load(file)

nltk.download('stopwords')    
stopword_list = nltk.corpus.stopwords.words('english') 


    
def remove_stopwords(text):
    tokens = tokenize(text)
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text

def normalize_corpus(corpus):
    
    normalized_corpus = []
    for index, text in enumerate(corpus):
        text = text.lower()
        text = remove_stopwords(text)
        normalized_corpus.append(text)
    return normalized_corpus


# feature extraction  



# Endpoint for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint for sentiment prediction
@app.route('/predict', methods=['POST'])
def predict_sentiment():

    
    # Get the input sentence from the request
    sentence = request.form['sentence']
    sentence1=np.array([sentence])
    norm_test1 = normalize_corpus(sentence1)  
# extract features                                     
    test_features1 = vectorizer.transform(norm_test1)

    # Make sentiment prediction using the SVM model
    sentiment = model.predict(test_features1)
    sentiment_str = str(sentiment.item())  # Convert the sentiment to a string

    return render_template('result.html', sentence=sentence, sentiment=sentiment_str)

if __name__ == '__main__':
    app.run(debug=True)
