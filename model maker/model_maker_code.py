import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import re
import nltk
nltk.download('stopwords')

from sklearn.feature_extraction.text import CountVectorizer

import string

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split

#Load dataset
dataset = pd.read_csv("C:\\Users\\HP\\Desktop\\Email-Spam-detection-using-NLP-master\\emails.csv")

dataset.drop_duplicates(inplace = True)

dataset.spam.value_counts()

print (pd.DataFrame(dataset.isnull().sum()))

#split text column into array of words


dataset['text'] = dataset['text'].map(lambda text:re.sub('\W+', ' ',text)).apply(lambda x: (x.lower()).split())

dataset['text']=dataset['text'].map(lambda text: text[1:])

#Remove stpwords
nltk.download('stopwords')
stopword = nltk.corpus.stopwords.words('english')

def remove_stopwords(tokenized_list):
    text = [word for word in tokenized_list if word not in stopword]
    return text

dataset['text'] = dataset['text'].apply(lambda x: remove_stopwords(x))

nltk.download('wordnet')
wn = nltk.WordNetLemmatizer()

def lemmatizing(tokenized_text):
    text = ' '.join([wn.lemmatize(word) for word in tokenized_text])
    return text

dataset['text'] = dataset['text'].apply(lambda x: lemmatizing(x))

#Tfidf vectororizer #########################

tfidf_vect = TfidfVectorizer()
X_tfidf = tfidf_vect.fit_transform(dataset['text'])
#print(X_tfidf.shape)
#print(tfidf_vect.get_feature_names())

X_tfidf_df = pd.DataFrame(X_tfidf.toarray())

X_tfidf_df.columns = tfidf_vect.get_feature_names()


########### Create features #################



############### Using tfidf vectorizer lets see the accuracy of the model ##################
#Taking independent variables separately

X_train, X_test, y_train, y_test = train_test_split(dataset[['text']], dataset['spam'], test_size=0.2)

tfidf_vect = TfidfVectorizer()
tfidf_vect_fit = tfidf_vect.fit(X_train['text'])

tfidf_train = tfidf_vect_fit.transform(X_train['text'])
tfidf_test = tfidf_vect_fit.transform(X_test['text'])

X_train_vect =  pd.DataFrame(tfidf_train.toarray())
X_test_vect = pd.DataFrame(tfidf_test.toarray())

#Choosing best parameters
rf = RandomForestClassifier(n_estimators=50, max_depth=None, n_jobs=-1)

rf_model = rf.fit(X_train_vect, y_train)

y_pred = rf_model.predict(X_test_vect)

precision, recall, fscore, train_support = score(y_test, y_pred, pos_label=1, average='binary')
print(' ---- Precision: {} / Recall: {} / Accuracy: {}'.format(
     round(precision, 3), round(recall, 3), round((y_pred==y_test).sum()/len(y_pred), 3)))


##############################

import pickle

#creating and training a model
#serializing our model to a file called model.pkl
pickle.dump(rf, open("C:\\Users\\HP\\Desktop\\Email-Spam-detection-using-NLP-master\\model_email_yat.pkl","wb"))

pickle.dump(tfidf_vect, open("C:\\Users\\HP\\Desktop\\Email-Spam-detection-using-NLP-master\\tfidf_vectorizer.pkl","wb"))