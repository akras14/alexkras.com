"""Write labels file"""
import json

with open("token-tweets.json") as f:
    tokent = json.load(f)

labels = []
for i,t in enumerate(tokent):
    labels.append((i, " ".join(t)))

with open("labels.csv", "w") as f:
    f.write("Id;Label\n")
    for l in labels:
        f.write(str(l[0]) + ";" + l[1] + "\n")
