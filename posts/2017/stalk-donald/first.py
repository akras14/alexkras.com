import json
import pyperclip
!pip install pyperclip
import pyperclip
files = pyperclip.paste().split(" ")
files
files = pyperclip.paste().strip().split(" ")
files
all = {}
for f in files:
    with open(f) as d:
        data = json.load(d)
        all[f] = data
dall
all
all.keys()
all['2012.json']
for y in all:
    for t in all[y]:
        print t
        break
for y in all:
    for t in all[y]:
        print t['text']
        break
allt = []
for y in all:
    for t in all[y]:
        allt.append(t['text'])
allt
len(allt)
with open("all-tweets", "w") as f:
    json.dump(allt, f)
ls
!vim all-tweets
pwd
from nltk.corpus import stopwords
!pip install nltk
from nltk.corpus import stopwords
#filtered_words = [word for word in word_list if word not in stopwords.words('english')]
def removeStopWords(t):
    " ".join([ word for word in t.split(" ") if word not in stopwords.words("english")])
removeStopWords(allt[0])
allt[0]
allt[0].split(" ")
allt[0].split(" ")
removeStopWords(allt[0])
t
t = allt[0]
t
[ word for word in t.split(" ") if word not in stopwords.words("english")]
t.split(" ")
stopwords.words
stopwords
stopwords.subdir("english")
stopwords
stopwords.unicode_repr
stopwords.unicode_repr("english")
from nltk.tokenize import sent_tokenize, word_tokenize
word_tokenize(t)
t
nltk.download()
import nltk
nltk.download()
word_tokenize(t)
stopwords.words("english")
removeStopWords(allt[0])
def removeStopWords(t):
    return " ".join([ word for word in t.split(" ") if word not in stopwords.words("english")])
removeStopWords(allt[0])
removeStopWords(word_tokenize(allt[0]))
def removeStopWords(t):
    return [ word for word in t if word not in stopwords.words("english")]
removeStopWords(word_tokenize(allt[0]))
from nltk.corpus import wordnet
wordnet
wordnet.synsets("bro")
wordnet.synsets("alex")
wordnet.synsets("door")
wordnet.synsets("dude")
"bro".isAlpha()
t
t.isalpha()
words = removeStopWords(word_tokenize(allt[0]))
words
map(str.isalpha, words)
map(str.isalpha.encoding("utf-8"), words)
map(lambda x: x.encode("utf-8").isalpha, words)
map(lambda x: x.encode("utf-8").isalpha(), words)
filter(lambda x: x.encode("utf-8").isalpha(), words)
def filterWords(t):
    return filter(lambda x: x.encode("utf-8").isalpha(), words)
filterWords(t)
%hist
filterWords(removeStopWords(word_tokenize(allt[0])))
tokent = [filterWords(removeStopWords(word_tokenize(t))) for t in allt]
from tqdm import tqdm
!pip install tqdm
from tqdm import tqdm
tokent = [filterWords(removeStopWords(word_tokenize(t))) for t in tqdm(allt)]
tokent
tokent = [filterWords(removeStopWords(word_tokenize(t))) for t in tqdm(allt)]
allt
#tokent = [filterWords(removeStopWords(word_tokenize(t))) for t in tqdm(allt)]
tokent = []
for t in tqdm(allt):
    tokent.append(filterWords(removeStopWords(word_tokenize(t))))
tokent
t
tokent
ls
tqdm(allt)
allt
tokent = []
tokent
tokent = []
for t in tqdm(allt):
    tt = filterWords(removeStopWords(word_tokenize(t)))
    print tt
tokent = []
for t in tqdm(allt):
    print t
    tt = filterWords(removeStopWords(word_tokenize(t)))
    print tt
ls
cd ..
ls
vim all-tweets.json
!vim all-tweets.json
len(allt)
tokent = []
for t in tqdm(allt):
    print t
    tt = filterWords(removeStopWords(word_tokenize(t)))
    print tt
with open("all-tweets.json") as f:
    allt = json.load(f)
len(allt)
[t for t in allt inf "wonderful place" in t]
[t for t in allt if "wonderful place" in t]
[t for t in allt if "wonderful place" in t]
ls
def filterWords(t):
    return filter(lambda x: x.encode("utf-8").isalpha(), t)
tokent = [filterWords(removeStopWords(word_tokenize(t))) for t in tqdm(allt)]
tokent
len(tokent)
with open("token-tweets.json", "w") as f:
    json.dump(f, tokent)
with open("token-tweets.json", "w") as f:
    json.dump(tokent, f)
!vim token-tweets.json
ls
def findIntersection(first, second):
    intersection = set(first) & set(second)     # Find a sub set of words that is present in both lists
    intersectionLength = len(intersection)      # Words both comments have in common
    wordCount = len(first) + len(second)        # Total length of both comments
    if wordCount == 0:                          # Corner case
        return 0
    else:
        return (intersectionLength/wordCount)   # Intersection score between two comments
findIntersection(tokent[0], tokent[1])
tokent
for i,t in tokent.items():
    print i
    print t
    break
for i,t in tokent:
    print i
    print t
    break
for i,t in enumerate(tokent):
    print i
    print t
    break
for i,t in enumerate(tokent,1):
    print i
    print t
    break
for i,t in enumerate(tokent,1):
    print i
    print " ".join(t)
    break
for i,t in enumerate(tokent,1):
    print i
    print " ".join(t)
    break
labels = []
for i,t in enumerate(tokent,1):
    labels.append(i, " ".join(t))
labels = []
for i,t in enumerate(tokent,1):
    labels.append((i, " ".join(t)))
labels
len(labels)
ls
ls
ls
labels
with open("labels", "w") as f:
    f.write("Id;Label")
    for l in labels:
        f.write(l[0] + ";" + l[1])
with open("labels", "w") as f:
    f.write("Id;Label")
    for l in labels:
        f.write(str(l[0]) + ";" + l[1])
with open("labels", "w") as f:
    f.write("Id;Label\n")
    for l in labels:
        f.write(str(l[0]) + ";" + l[1] + "\n")
s
ls
who
for l in enumerate(tokent, 1):
    for r in enumerate(tokent, 1):
        print findIntersection(l,r)
        break
for l in enumerate(tokent, 1):
    for r in enumerate(tokent, 1):
        print findIntersection(l,r)
        break
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        print findIntersection(l,r)
        break
k
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            print res
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        print l
        print r
        res = findIntersection(l,r)
        print res
    break
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        print l
        print r
        res = findIntersection(l,r)
        print res
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        print l
        print r
        res = findIntersection(l,r)
        print res
findIntersection("test", "test")
tokent[0]
findIntersection(tokent[0], tokent[0])
def findIntersection(first, second):
    intersection = set(first) & set(second)     # Find a sub set of words that is present in both lists
    intersectionLength = len(intersection)      # Words both comments have in common
    intersectionLength = flaot(intersectionLength)
    wordCount = len(first) + len(second)        # Total length of both comments
    if wordCount == 0:                          # Corner case
        return 0
    else:
        return (intersectionLength/wordCount)   # Intersection score between two comments
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        print l
        print r
        res = findIntersection(l,r)
        print res
def findIntersection(first, second):
    intersection = set(first) & set(second)     # Find a sub set of words that is present in both lists
    intersectionLength = len(intersection)      # Words both comments have in common
    intersectionLength = float(intersectionLength)
    wordCount = len(first) + len(second)        # Total length of both comments
    if wordCount == 0:                          # Corner case
        return 0
    else:
        return (intersectionLength/wordCount)   # Intersection score between two comments
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        print l
        print r
        res = findIntersection(l,r)
        print res
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            print l
            print r
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            print l
            print r
            print
from repoze.lru import lru_cache
from repoze.lru import lru_cache
!pip install repoze.lru
from repoze.lru import lru_cache
%reload
from repoze.lru import lru_cache
pip install functools32 3.2.3-2
!pip install functools32 3.2.3-2
!pip install functools32
from functools32 import lru_cache
@lru_cache(maxsize=2048)
def findIntersection(first, second):
    intersection = set(first) & set(second)     # Find a sub set of words that is present in both lists
    intersectionLength = len(intersection)      # Words both comments have in common
    intersectionLength = float(intersectionLength)
    wordCount = len(first) + len(second)        # Total length of both comments
    if wordCount == 0:                          # Corner case
        return 0
    else:
        return (intersectionLength/wordCount)   # Intersection score between two comments
allinter = []
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            allinter.append((i,j,res))
alliter = []
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            allinter.append((i, j, res))
def findIntersection(first, second):
    intersection = set(first) & set(second)     # Find a sub set of words that is present in both lists
    intersectionLength = len(intersection)      # Words both comments have in common
    intersectionLength = float(intersectionLength)
    wordCount = len(first) + len(second)        # Total length of both comments
    if wordCount == 0:                          # Corner case
        return 0
    else:
        return (intersectionLength/wordCount)   # Intersection score between two comments
alliter = []
for i,l in tqdm(enumerate(tokent, 1)):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            allinter.append((i, j, res))
alliter = []
for i,l in enumerate(tokent, 1):
    print len(i/len(tokent))
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            allinter.append((i, j, res))
alliter = []
for i,l in enumerate(tokent, 1):
    print i/len(tokent)
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            allinter.append((i, j, res))
alliter = []
for i,l in enumerate(tokent, 1):
    print float(i)/len(tokent)
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            allinter.append((i, j, res))
alliter = []
for i,l in enumerate(tokent, 1):
    print float(i)/len(tokent)
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            allinter.append((i, j, res))
alliter = {}
for i,l in enumerate(tokent, 1):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            t1 = (i, j, res)
            t2 = (j, i, res)
            if t1 not in alliter and t2 not in alliter:
                alliter[t1] = True
                alliter[t2] = True
alliter
len(alliter)
len(tokent) * len(tokent)
_181/_180
alliter = {}
for i,l in enumerate(tokent, 1):
    print len(alliter)
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0:
            t1 = (i, j, res)
            t2 = (j, i, res)
            if t1 not in alliter and t2 not in alliter:
                alliter[t1] = True
                alliter[t2] = True
alliter = {}
for i,l in enumerate(tokent, 1):
    print len(alliter)
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0.3:
            t1 = (i, j, res)
            t2 = (j, i, res)
            if t1 not in alliter and t2 not in alliter:
                alliter[t1] = True
                alliter[t2] = True
alliter = {}
for i,l in enumerate(tqdm(tokent), 1):
    for j,r in enumerate(tokent, 1):
        res = findIntersection(l,r)
        if res > 0.3:
            t1 = (i, j, res)
            t2 = (j, i, res)
            if t1 not in alliter and t2 not in alliter:
                alliter[t1] = True
                alliter[t2] = True
%hist
%hist -f first.py
