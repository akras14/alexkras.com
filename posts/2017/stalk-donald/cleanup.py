""" Convert Tweets to Tokens"""
import json
import pyperclip
from nltk.corpus import stopwords
from tqdm import tqdm

stopwords = stopwords.words("english")

with open("all-tweets.json") as f:
    allt = json.load(f)

def filterWords(t):
    return [s for s in t if s.encode("utf-8").isalpha()]

def removeStopwords(t):
    return [s for s in t if s not in stopwords]

allt = [t.lower().split() for t in allt]

allt = [filterWords(t) for t in allt]

allt = [removeStopwords(t) for t in allt]


with open("token-tweets.json", "w") as f:
    json.dump(allt, f)
