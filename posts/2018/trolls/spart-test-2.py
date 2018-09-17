from pyspark import SparkContext
from tqdm import tqdm
import json
sc = SparkContext("local[3]", "word count")
sc.setLogLevel("ERROR")
print("test1")
with open("data/token-tweets.json") as f:
    tt = json.load(f)
df = sc.parallelize(tt[:100])
df2 = sc.parallelize(tt[:100])
print("test2")
def findIntersection(first, second):
    intersection = first & second               # Find a sub set of words that is present in both lists
    intersectionLength = float(len(intersection))      # Words both comments have in common
    wordCount = len(first) + len(second)        # Total length of both comments
    return (intersectionLength/wordCount)   # Intersection score between two comments
print("test3")
test = df.cartesian(df2).collect()
print(len(test))
print("\n\nalldone\n\n")
