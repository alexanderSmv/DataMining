from nltk import word_tokenize

list = ['go until jurong point crazi avail onli bugi n great world la e buffet cine there got amor wat ', 'ok lar joke wif u oni ', 'free entri wkli comp win fa cup final','go until jurong point crazi avail onli bugi n great world la e buffet']

hemList={}
# d = dict([(tmp, 1)])
# d[tmp2] = 2
arr = {}
def add_and_count(someList):
    for item in someList:
        split_words = word_tokenize(item)
        for word in split_words:
            #print(word)
            if not  word in arr:
                arr[word] = 1
            else:
                arr[word]+=1
    return someList


add_and_count(list)
print(arr)






