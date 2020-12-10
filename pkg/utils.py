import os
import pandas as pd
import joblib

import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def remove_punc(text):
    for punc in string.punctuation:
        text = text.replace(punc, '')
    return text

def remove_digit(text):
    text = ''.join(word for word in text if not word.isdigit())
    return text  

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word.lower() for word in word_tokenize(text) if not word in stop_words])
    return text

def lemmatizer(text):
    lst = [WordNetLemmatizer().lemmatize(word) for word in word_tokenize(text)]
    return (' '.join(lst))

def preprocess(text):
    text = remove_punc(text)
    text = remove_digit(text)
    # text = remove_stopwords(text)
    # text = lemmatizer(text)
    return text

def get_latent_df():
    file_path = "https://storage.googleapis.com/video-game-rec-99/data/latent_df.csv"
    df = pd.read_csv(file_path).set_index('Unnamed: 0')
    return df

def get_game_lst():
    file_path = "https://storage.googleapis.com/video-game-rec-99/data/Catelog.csv"
    df = pd.read_csv(file_path)
    return df['Name'].tolist()

def get_model(model_name = 'NaiveBayes'):
    file_path = f"{model_name}.joblib"
    model = joblib.load(file_path)
    return model


    