# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:23:33 2018

@author: Prometheus
"""
## 1st: text Preprocessing with Python
# Load data
filename = "metamorphosis_clean.txt"
file = open('metamorphosis.txt', 'rt')
text = file.read()
file.close()

#Split raw text into words by white space
words = text.split()
print(words[:100])

# Remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:100])

# Normalize to lower case
words = [word.lower() for word in words]
print(words[:100])

## 2nd: Using NLTK library tools

# 1. Split into sentences
from nltk import sent_tokenize
sentences = sent_tokenize(text)
print(sentences[0])

# 2. Split into Words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens[:100])

# 3. Filter out punctuation (removing non alphabetic tokens)
words = [word for word in tokens if word.isalpha()]
print(words[:100])

# 4. Filter Stop Words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)

# 3rd. Applying a Pipeline
'''Load the raw text.
Split into tokens.
Convert to lowercase.
Remove punctuation from each token.
Filter out remaining tokens that are not alphabetic.
Filter out tokens that are stop words.'''

# 3.1 Load Data
filename = 'metamorphosis_clean.txt'
file = open('metamorphosis.txt', 'rt')
text = file.read()
file.close()

# 3.2 Split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

# 3.3  Converting to lower case
tokens = [w.lower() for w in tokens]

# 3.4 Remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# 3.5 Remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# 3.6 Filtering out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])

## 3.7 Stem words: Reducing words to their root
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
print(stemmed[:100])