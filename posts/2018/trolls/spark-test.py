from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext("local[3]", "word count")
    sc.setLogLevel("ERROR")
    print("test")
    lines = sc.textFile("data/tweets.csv")
    print(lines)
    words = lines.flatMap(lambda l: l.split(" "))
    wc = words.countByValue()
    s = sorted(wc.items(), key=lambda x: x[1], reverse=True)
    for w,c in s[:100]:
        print("{},{}").format(c,w.encode('utf-8'))
