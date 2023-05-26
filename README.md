# SensiScan - Sentiment Analyzer

SensiScan is a sentiment analyzer that helps analyze the sentiment of given text or sentences. It classifies the sentiment as positive, negative, or neutral, providing insights into the emotional tone of the input.

## Features

- Sentiment Analysis: Analyze the sentiment of input text or sentences.
- Classification: Classify sentiment as positive, negative, or neutral.
- User-friendly Interface: Provide a simple and intuitive interface to input text and view the sentiment analysis results.

## Dataset

SensiScan utilizes the "Twitter US Airline Sentiment" dataset for training and evaluation. This dataset contains tweets related to major US airlines and their associated sentiment labels. The dataset is widely used in sentiment analysis research and provides a diverse range of sentiments expressed by Twitter users towards different airlines.

### Dataset Details

- Dataset: Twitter US Airline Sentiment
- Source: [Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
- Description: The dataset consists of approximately 14,640 tweets labeled with sentiment values: positive, negative, or neutral. The tweets were collected between February 2015 and February 2016, and they cover opinions and experiences of customers towards various US airlines.

## Data Preprocessing

Prior to training the sentiment analysis model, the dataset undergoes several preprocessing steps, including:
- Text cleaning: Removing special characters, URLs, and unnecessary whitespace.
- Tokenization: Splitting the text into individual tokens (words).
- Stopword removal: Eliminating common words that do not contribute to sentiment analysis.

The preprocessed dataset is then used to train the sentiment analysis model in SensiScan.


