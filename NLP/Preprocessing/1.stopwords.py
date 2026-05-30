# Stop words are common words in the language which don't carry much meaning e.g. "and", "of", "a", "to".

# We remove these words because it removes a lot of complexity from the data. 
# These words don't add much meaning to text so by removing them we are left with a smaller, cleaner dataset. 
# Smaller, cleaner datasets often lead to increased accuracy in machine learning and will also speed up processing times.

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

en_stopwords = stopwords.words('english')
# print(en_stopwords)


sentence = "it was too far to go to the shop and he did not want her to walk"

# keep the words in the sentance if the word is not in the list of stop words
sentance_no_stopwords = ' '.join([word for word in sentence.split() if word not in (en_stopwords)])
print(sentance_no_stopwords)

# removing stop words from list
en_stopwords.remove("too")
en_stopwords.remove("not")
sentance_no_stopwords = ' '.join([word for word in sentence.split() if word not in (en_stopwords)])
print(sentance_no_stopwords)

# add custom stop words
en_stopwords.append("go")
sentance_no_stopwords = ' '.join([word for word in sentence.split() if word not in (en_stopwords)])
print(sentance_no_stopwords)

