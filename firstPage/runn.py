import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import joblib
import pickle
with open('nb_pickle','rb') as f:
    model = pickle.load(f)
with open('cv_pickle','rb') as f:
    tt = pickle.load(f)
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
s=str(input())
c =fn(s)
y = model.predict(c)
print(y)
