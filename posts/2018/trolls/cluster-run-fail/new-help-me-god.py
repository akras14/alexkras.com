from pyspark import SQLContext, SparkContext, SparkConf
from pyspark.sql import Row
import json
from itertools import izip_longest

if __name__ == '__main__':
    def ziph(num, max):
        return list(izip_longest([], range(num+1, max), fillvalue=num))

    with open("token-tweets.json") as f:
        tt = json.load(f)

    tokent = [set(t) for t in tt]

    conf = SparkConf().setAppName("please work")
    sc = SparkContext(conf=conf) 
    #sc = SparkContext()
    sc.setLogLevel("WARN")
    sqlContext = SQLContext(sc)
    rdd = sc.parallelize(tt, numSlices=1000)
    t = rdd.zipWithIndex().filter(lambda x: len(x[0]) > 4).map(lambda x: Row(t1=x[0],i1=x[1]))
    t2 = rdd.zipWithIndex().filter(lambda x: len(x[0]) > 4).map(lambda x: Row(t2=x[0],i2=x[1]))
    df = sqlContext.createDataFrame(t)
    df2 = sqlContext.createDataFrame(t2)

    d = df.crossJoin(df2)

    def findIntersection(r):
        first = tokent[r.i1]
        second = tokent[r.i2]
        intersection = first & second               # Find a sub set of words that is present in both lists
        intersectionLength = float(len(intersection))      # Words both comments have in common
        wordCount = len(first) + len(second)        # Total length of both comments
        score = intersectionLength/wordCount        # Intersection score between two comments
        return Row(t1=r.t1, t2=r.t2, i1=r.i1, i2=r.i2, score=score)

    r = d.filter(d.i1 < d.i2).rdd.map(findIntersection)
    f = sqlContext.createDataFrame(r)
    f.createOrReplaceTempView("TEST")
    ff = sqlContext.sql("select * FROM TEST where score > 0.2")

    with open("t.json", "w") as f:
        for l in ff.toJSON().collect():
            f.write(l + "\n")
