"""Write labels file"""
import json
from collections import Counter
from pprint import pprint as pp

with open("token-tweets.json") as f:
    tokent = json.load(f)

tweets = [s for t in tokent for s in t]

ct = Counter(tweets)

mc = ct.most_common(30)

for w in mc:
    print "{},{}".format(*w)