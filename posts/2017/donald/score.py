"""Write labels file"""
import json
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("token-tweets.json") as f:
    tokent = json.load(f)

# http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/

tokent = [set(t) for t in tokent]
data = [" ".join(t) for t in tokent]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data)

cs = cosine_similarity(tfidf_matrix, tfidf_matrix)

saved = {}
with open("edges.csv", "w") as f:
    f.write("Source;Target;Weight;Type\n")
    for i, row in enumerate(tqdm(cs)):
        for j, col in enumerate(row):
            if col < 0.99 and col > 0.2:
                if (j,i) not in saved:
                    saved[(i,j)] = True
                    f.write('{};{};{};"Undirected"\n'.format(i,j,col))
