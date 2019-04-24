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


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

def tokenize_data_word(file):
    try:
        with open(file, 'r') as infile:
            for line in infile:
                return word_tokenize(line)
    except FileNotFoundError as identifier:
        print(identifier)

def tokenize_data_sentence(file):
    try:
        with open(file, 'r') as infile:
            for line in infile:
                return sent_tokenize(line)
    except FileNotFoundError as identifier:
        print(identifier)

def word_stemming():
    ps = PorterStemmer()
    words = ['Helping', 'speaking', 'bedroom', 'purple', 'jokes']
    word_token = tokenize_data_word('data.txt')
    for word in word_token:
        print(ps.stem(word))

def word_lemmatize():
    lemmatizer = WordNetLemmatizer()
    words = ['Helping', 'speaking', 'bedroom', 'purple', 'jokes']
    word_token = tokenize_data_word('abc.txt')
    for word in word_token:
        print(lemmatizer.lemmatize(word))

def word_synonyms():
    synonym_words = ['Facilitate', 'flourish', 'bridge', 'warm', 'expansion']

    for word in synonym_words:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                print(l.name(), word)

def word_antonyms():
    antonym_words = ['Global', 'largest', 'dominant', 'alliance', 'continue']

    for word in antonym_words:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    print(l.antonyms()[0].name())

# Uncomment the following line to run the functions
# print(tokenize_data_word('abc.txt'))
# print(tokenize_data_sentence('abc.txt'))
# word_stemming()
# word_lemmatize()
# word_synonyms_antonyms()
word_antonyms()


