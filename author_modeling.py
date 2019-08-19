import spacy
import nltk

from nltk.corpus import gutenberg
import random
import pandas as pd
import matplotlib.pyplot as plt


nlp = spacy.load('en')
emma = gutenberg.raw('austen-emma.txt')
parsed_emma = nlp(emma)

import re
sample_size = 100
my_sample = random.sample(list(parsed_emma.sents),sample_size)

sample = []
for sent in my_sample:
    sent = re.sub("\s+"," ",sent.text)
    print(sent,"\n")
    sample.append(sent)
