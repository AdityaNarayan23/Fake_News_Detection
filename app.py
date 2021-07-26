# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 20:42:57 2021

@author: anarayan
"""

import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import string as st
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

check_model = pickle.load(open("final_model.pkl", "rb"))
check_vector = pickle.load(open("count_vectorizer.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    
    str_features = [str(x) for x in request.form.values()]
    
    title = str_features[0]
    print(title)
    author = str_features[1]
    print(author)
    text = str_features[2]
    print(text)

    stop_words = stopwords.words('english')
    stopwords_dict = Counter(stop_words)
        
    author_title = author + ' ' + title
    author_title = author_title.lower()
    author_title = "".join([ch for ch in author_title if ch not in st.punctuation])
    author_title = [word for word in author_title.split() if word not in stopwords_dict]
    author_title_clean = ' '.join([str(word) for word in author_title])
    print(author_title_clean)
    
    if len(author_title_clean) != 0:
        text_list = [author_title_clean]
        text_count = check_vector.transform(text_list)
        prediction = check_model.predict(text_count)
        print(check_model.predict(text_count))
        print("Hello Output")
    
        if prediction[0] == 0:
            prediction = "Fake News"
        else:
            prediction = "Real News"
        return render_template('index.html',prediction_text='The News published is : {}'.format(prediction))
    else:
        return render_template('index.html',prediction_text='Please enter valid Input - Title, Author and Text')
    

    

if __name__ == '__main__':
    app.run(debug=True)


    