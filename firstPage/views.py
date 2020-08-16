from django.shortcuts import render
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import joblib
import pickle
from django.db import connection
with open('/home/varundutia/development/webapp/firstPage/nb_pickle','rb') as f:
    model = pickle.load(f)
with open('/home/varundutia/development/webapp/firstPage/cv_pickle','rb') as f:
    tt = pickle.load(f)
import mysql.connector as mysql
def fn(c):
    new = c
    new = re.sub('[^a-zA-Z]', ' ', new)
    new = new.lower()
    new = new.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    new= [ps.stem(word) for word in new if not word in set(all_stopwords)]
    new = ' '.join(new)
    new_corpus = [new]
    new_X_test = tt.transform(new_corpus).toarray()
    return new_X_test

def index(request):
    context = {'a':'HelloWorld'}
    return render(request,'index.html',context)

def predict(request):
    if (request.method == 'POST'):
        d = request.POST.dict()
        s = request.POST.dict()['subject']
        c =fn(s)
        y = model.predict(c)
        print(y)
        db = mysql.connect(
        host='localhost',
        user='root',
        passwd='Varun@12061999',
        database='feedbackdb'
        )
        cursor = db.cursor()
        query = 'INSERT INTO `feedback`(`fname`, `lname`, `mail`, `area`, `feed`, `type`) VALUES ("%s","%s","%s","%s","%s","%s")'
        values = (d['firstname'],d['lastname'],d['mailid'],d['Area'],d['subject'],str(y[0]))
        cursor.execute(query,values)
        db.commit()
        print(cursor.rowcount,"rec inserted")
        print('POST request')
        if(y[0]==1):
            return render(request,'good.html')
        else:
            return render(request,'bad.html')
def viewdB(request):
    return render(request,'viewdB.html')
def updatedB(request):
    return None
