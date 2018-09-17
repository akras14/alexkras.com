"""
1. Load token tweets
2. Remove duplicate words
3. Loop through every token
    Loop through every token again
        if not same token
            get key (1,2)
            get key (2,1)
            if reverse key not checked yet:
                find intersection for 2 tweets
                store intersection for 2 tweets
4. Write intersection data to CSV file
"""
import json
from tqdm import tqdm

with open("data/token-tweets.json") as f:
    tokent = json.load(f)

tokent = [set(t) for t in tokent if len(set(t)) > 0]

def findIntersection(first, second):
    intersection = first & second               # Find a sub set of words that is present in both lists
    intersectionLength = float(len(intersection))      # Words both comments have in common
    wordCount = len(first) + len(second)        # Total length of both comments
    return (intersectionLength/wordCount)   # Intersection score between two comments

alliter = {}
for i in tqdm(range(0,len(tokent[:10000]))):
    for j in range(i+1, len(tokent[:10000])):
        l = tokent[i]
        r = tokent[j]
        if l == r:
            continue
        t1 = (i,j)
        t2 = (j, i)
        assert t2 not in alliter
        res = findIntersection(l,r)
        alliter[t1] = res

with open("data/edges.csv", "w") as f:
    f.write("Source;Target;Weight;Type\n")
    for a in alliter:
        vals = list(a) + [alliter[a]]
        f.write('{};{};{};"Undirected"\n'.format(*vals))
