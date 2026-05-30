"""
Where stemming removes the last few characters of a word, 
lemmatization stems the word to a more meaningful base form and ensures it does not lose it's meaning. 
Lemmatization works more intelligently, referencing a pre-defined dictionary containing the context of words and uses this when diminishing the word to the base form.
"""

from nltk.stem import PorterStemmer

# create stemmer
stemmer = PorterStemmer()
connect_tokens = ['connecting', 'connected', 'connectivity', 'connect', 'connects']
learn_tokens = ['learned', 'learning', 'learn', 'learns', 'learner', 'learners']
likes_tokens = ['likes', 'better', 'worse']
print("##Stemming")
for t in connect_tokens:
    print(t, " : ", stemmer.stem(t))

for l in learn_tokens:
    print(l, ' : ', stemmer.stem(l))

for l in likes_tokens:
    print(l, " : ", stemmer.stem(l))


print("\n##Lemmatization")
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

# create lemmatizer 
lemmatizer = WordNetLemmatizer()
for t in connect_tokens:
    print(t, " : ", lemmatizer.lemmatize(t))

for t in learn_tokens:
    print(t, " : ", lemmatizer.lemmatize(t))

for t in likes_tokens:
    print(t, " : ", lemmatizer.lemmatize(t))
