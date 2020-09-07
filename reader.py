import csv
import re
from gensim.parsing.preprocessing import remove_stopwords
import gensim

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

# словарь стоп слов
gensim.parsing.preprocessing.STOPWORDS = {'a', 'the', 'to', 'in'}
# печать стоп слов(по дефолту там другие)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)

text = "Nick likes to a play the in football"
filtered_sentence = remove_stopwords(text)
print(filtered_sentence + "\n")


# Привести слов в предложении к единному корню
# word_tokenize - разбивает предложение на слов
def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    token_words
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


with open("spam_file.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    i = 1
    porter = PorterStemmer()
    lancaster = LancasterStemmer()

    for row in reader:
        i += 1
        # re.sub(r'[^a-zA-Z ]', r'' - заменяет все кроме букв  на ''
        # cleanSumbNum = remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())
        # result = stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower()))

        print(i, '|', row['v1'], '|', stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))

# str="some 1 tex4t fo# %^*( fdf wsdsd dff!  A SHO TAK MONA Heelen _+dr1 , fgdfg . df ?/"
# print(str+"\n")
#
# cleanString1 = re.sub(r'[^a-zA-Z ]',r'',str)
# print(cleanString1)
# cleanString2 = cleanString1.lower()
# print(cleanString2+"\n")
#
# porter = PorterStemmer()
# lancaster=LancasterStemmer()
# #proide a word to be stemmed
# print("Porter Stemmer")
# print(porter.stem("cats"))
# print(porter.stem("but swimming as playing"))
