""" Convert Tweets to Tokens"""
import json
import pyperclip
from nltk.corpus import stopwords
from tqdm import tqdm

stopwords = stopwords.words("english")
blahwords = {'rt'}

with open("data/all-tweets.json") as f:
    allt = json.load(f)

def filterWords(t):
    return [s for s in t if s.encode("utf-8").isalpha()]

def removeStopwords(t):
    return [s for s in t if s.lower() not in stopwords]

    return
def removeCustomKeywords(t):
    return [s for s in t if s.lower() not in blahwords]

allt = [t.lower().split() for t in tqdm(allt)]

allt = [filterWords(t) for t in tqdm(allt)]

allt = [removeStopwords(t) for t in tqdm(allt)]

allt = [removeCustomKeywords(t) for t in tqdm(allt)]


with open("data/token-tweets.json", "w") as f:
    json.dump(allt, f, indent=True)
