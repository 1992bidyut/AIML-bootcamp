"""
The next step in preprocessing is to standardise the text. One option for this is stemming, where words are reduced to their base form. 
For example, words like ‘connecting’ or ‘connected’ will be stemmed to the base form ‘connect’. 
Stemming works by removing suffix/ending of word but can sometimes lead to the base form not being meaningful or a proper word.

We standardize the text in this way because it will lower the number of unique words in our dataset; 
therefore reducing the size and complexity of our data. 
Removing complexity and noise from the data is an important step for preparing our data properly for machine learning.
"""

from nltk.stem import PorterStemmer

# create stemmer
stemmer = PorterStemmer()
connect_tokens = ['connecting', 'connected', 'connectivity', 'connect', 'connects']
for t in connect_tokens:
    print(t, " : ", stemmer.stem(t))


learn_tokens = ['learned', 'learning', 'learn', 'learns', 'learner', 'learners']
for l in learn_tokens:
    print(l, ' : ', stemmer.stem(l))


likes_tokens = ['likes', 'better', 'worse']
for l in likes_tokens:
    print(l, " : ", stemmer.stem(l))