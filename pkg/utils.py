import os
import pandas as pd
import joblib

import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pickle
# import wikipedia

import requests
import io
import PIL

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
    text = remove_stopwords(text)
    text = lemmatizer(text)
    return text

def get_latent_df(local = True):
    if local:
        file_path = "pkg/data/latent_df.csv"
    else:
        file_path = "https://storage.googleapis.com/video-game-rec-99/data/latent_df.csv"
    df = pd.read_csv(file_path).set_index('Unnamed: 0')
    return df

def get_game_lst(local = True):
    if local:
        file_path = "pkg/data/Catelog.csv"
    else:
        file_path = "https://storage.googleapis.com/video-game-rec-99/data/Catelog.csv"
    df = pd.read_csv(file_path)
    return df['Name'].tolist()





# def get_link(links):
#     for link in links:
#         if ".png" in link:
#             return link

# def get_page(name):
#     try: 
#         page = wikipedia.WikipediaPage(name)
#     except:
#         return None
#     return page

    
# def get_img_url(name):
    
#     page = get_page(name)
#     if page:
#         try:
#             link = get_link(page.images)
#         except:
#             pass
#     else:
#         link = None
#     return link