# Omer Mustafa - F2016-472
# Artificial Intelligence by Dr. Iftikhar Hussain
# Lab no. 4

# Write Python code to perform the following operations using Natural language
# toolkit (NLTK) library.
# 1. Tokenize Text (sentence wise and also word wise)
# Read the text file “abc.txt” given below

# 2. Get Synonyms From WordNet of the following words
# Facilitate, flourish, bridge, warm, expansion

# 3. Get Antonyms From WordNet

# Global, largest, dominant, alliance, continue

# 4. Word Stemming

# Helping, speaking, bedroom, purple, jokes
# 5. Lemmatizing Words Using WordNet
# Helping, speaking, bedroom, purple, jokes


import nltk
nltk.download()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

my_sent = "Hi man, how have you been?"
tokens = word_tokenize(my_sent)

print(tokens)