import collections
import csv
import re
from gensim.parsing.preprocessing import remove_stopwords
import gensim
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from collections import  Counter

gensim.parsing.preprocessing.STOPWORDS = {'a', 'the', 'to', 'in'}
all_stopwords = gensim.parsing.preprocessing.STOPWORDS

list_spam_ham = []
contentList = []#тут и спам и хам

spamList = []
hamList = []

arrWord_Spam = {}
arrWord_Ham = {}


porter = PorterStemmer()
lancaster = LancasterStemmer()
#привести слова к корню
def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    token_words
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

#Посчитать к-во слов в массиве
def add_and_count(someList,outputArr):
    for item in someList:
        split_words = word_tokenize(item)
        for word in split_words:
            #print(word)
            if not  word in outputArr :
                outputArr[word] = 1
            else:
                outputArr[word]+=1
    return someList

def openFile_fillArrays():
    with open("sms-spam-corpus.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        i = 1
        for row in reader:
            i += 1
            #list_spam_ham.append(row['v1'])#В файле набор строк Spam Ham
            contentList.append(stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))# заполняю массив сообщений(общий)
            if row['v1'] =='spam':
                spamList.append(stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))
            else:
                hamList.append(stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))
            # print(i, '|', row['v1'], '|', stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))

        # print('"ham" встречается: ',List_s_h.count('ham'),' раз')
        # print('"spam" встречается: ', List_s_h.count('spam'), ' раз')
    csvfile.close()

openFile_fillArrays()
add_and_count(spamList, arrWord_Spam)
add_and_count(hamList, arrWord_Ham)

print(arrWord_Spam)
print(arrWord_Ham)

# Сортировка слов по алфавиту
# tmp = collections.OrderedDict(sorted(arrWord_Spam.items()))
# print(tmp)

def fillSpamFile():#по алфавиту
    w = csv.writer(open("spam.csv", "w"))
    tmp = collections.OrderedDict(sorted(arrWord_Spam.items()))
    for key, val in tmp.items():
        w.writerow(['word: ', key, ' amount: ', val])

def fillHamFile():#дефолтный
    w = csv.writer(open("ham.csv", "w"))
    for key, val in arrWord_Ham.items():
        w.writerow(['word: ', key, ' amount: ', val])

fillHamFile()
fillSpamFile()

# Популярные слова в словаре
# MostCommonSpamWords = Counter(arrWord_Spam).most_common()
# MostCommonHamWords = Counter(arrWord_Ham).most_common()
# print(MostCommonSpamWords)
# print(MostCommonHamWords)