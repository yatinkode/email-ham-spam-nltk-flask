#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for
import re
from nltk.corpus import stopwords 
import nltk
from nltk.stem import WordNetLemmatizer 
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
nltk.download('stopwords')
nltk.download('wordnet')

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

#prediction function
def ValuePredictor(vect):
    to_predict = vect
    print("==============in function ValuePredictor() printing df changed to array \n",to_predict)
    loaded_model = pickle.load(open("model_email_yat.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        
        to_predict_list=to_predict_list.get('emailbody').lower()
        print("=======dictionary value===\n",to_predict_list)

        to_predict_list = re.findall(r'[A-Za-z]+', to_predict_list)
        print("=======only words===\n",to_predict_list)
        
        stop_words = set(stopwords.words('english')) 
        filtered_sentence = [w for w in to_predict_list if not w in stop_words] 
        
        filtered_sentence = [] 
  
        for w in to_predict_list: 
            if w not in stop_words: 
                filtered_sentence.append(w) 
        
        print("=======without stop words===\n",filtered_sentence)
        
        lemmatizer = WordNetLemmatizer() 
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in filtered_sentence])
        #lemmatized_output = re.findall(r'[A-Za-z]+', lemmatized_output)
        
        print("=======with lemmatized words===\n",lemmatized_output)
        
        lemmatized_output = [lemmatized_output]
        
        tv = pickle.load(open("tfidf_vectorizer.pkl","rb"))
        vect = tv.transform(lemmatized_output).toarray()
        print("=========tfidf vectorized\n",vect)
        
        #X_df = vectorizer.transform(filtered_sentence).toarray()
        #X_df = pd.DataFrame(X.toarray())
        #X_df.columns = lemmatized_output
        #print("=========dataframe with tfidf vectorozed\n",X_df)
        
        loaded_model = pickle.load(open("model_email_yat.pkl","rb"))
        result = loaded_model.predict(vect)
        
        #result = 1
        print("==============Result \n",result)

        if int(result)==1:
            prediction='The mail is Spam'
        else:
            prediction='The mail is non Spam'
            
        return render_template("index.html",prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)