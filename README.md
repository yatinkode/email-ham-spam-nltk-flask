Email Spam Detector
Email Spam detector with Flask app

![data](https://github.com/yatinkode/email-ham-spam-nltk-flask/blob/master/images/cap1.jpg)

https://emailspamdetector.herokuapp.com/

Steps Taken:
1) Reading Data 

| __Column name__    | __Detail__                                                 |
|--------------------|------------------------------------------------------------|
| text               |  Email Content                                             |
| spam               |  if mail is spam then 1, else 0                            |

2) Tokenizing text into words
3) Removing stopwords and punctuations
4) Lemmatization (Using Wordnet Lemmatization)
5) Vectorization (Using Tfidf Vectorization)
6) Pickling the vectorization object ()

Adding NLTK into heroku server

Go to you app page. Click on "More" on right hand side. Then select "Run console"

![data](https://github.com/yatinkode/email-ham-spam-nltk-flask/blob/master/images/cap2.jpg)

Write bash and Run

![data](https://github.com/yatinkode/email-ham-spam-nltk-flask/blob/master/images/cap3.jpg)



```bash
ls
mkdir nltk_data
python -m nltk.downloader
```

Choose option d

![data](https://github.com/yatinkode/email-ham-spam-nltk-flask/blob/master/images/cap4.jpg)


Then write "all"

![data](https://github.com/yatinkode/email-ham-spam-nltk-flask/blob/master/images/cap5.jpg)


Then choose "c"

![data](https://github.com/yatinkode/email-ham-spam-nltk-flask/blob/master/images/cap6.jpg)


All nltk libraries will be downloaded in nltk_data folder in ypur app repository in heroku. Use "ls" command to check for this folder.

Note: You may have to carry out above steps again if you deploy a new version of the app


