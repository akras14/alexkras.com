
"""Write labels file"""
import json
from tqdm import tqdm

with open("token-tweets.json") as f:
    tokent = json.load(f)

tokent = [set(t) for t in tokent]

def findIntersection(first, second):
    intersection = first & second               # Find a sub set of words that is present in both lists
    intersectionLength = len(intersection)      # Words both comments have in common
    intersectionLength = float(intersectionLength)
    wordCount = len(first) + len(second)        # Total length of both comments

    if wordCount == 0:                          # Corner case
        return 0
    else:
        return (intersectionLength/wordCount)   # Intersection score between two comments

alliter = {}
for i,l in enumerate(tqdm(tokent[:5000]), 1):
    for j,r in enumerate(tokent[:5000], 1):
        if l == r:
            continue
        res = findIntersection(l,r)
        if res > 0.4:
            res = (res - 0.4) * 100
            t1 = (i, j, res)
            t2 = (j, i, res)
            if t1 not in alliter and t2 not in alliter:
                alliter[t1] = True
                alliter[t2] = True

with open("edges.csv", "w") as f:
    f.write("Source;Target;Weight;Type\n")
    for a in alliter:
        f.write('{};{};{};"Undirected"\n'.format(*a))
