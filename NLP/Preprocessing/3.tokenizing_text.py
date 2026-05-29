"""
Fundamental step in NLP involves converting our text into smaller units through a process known as tokenization. 
These smaller units are known as our tokens. Word tokenization is the most common form of tokenization, 
where individual words in the text becomes a token, but tokens can also be sentences, 
sub words or individual characters depending on your use case.

Why do we do this? The meaning of the overall text is better understood if we can analyse and understand the individual parts as well as the whole. 
It's also an important step before we vecotrize our data.
"""

import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize

# Sentance tokenization
sentences = "Her cat's name is Luna. Her dog's name is max"
tokens = sent_tokenize(sentences)
print(tokens)

# Word tokenization
sentences = "Her cat's name is Luna. Her dog's name is max"
tokens = word_tokenize(sentences.lower())
print(tokens)
