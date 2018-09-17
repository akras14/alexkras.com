from tqdm import tqdm
tweets = range(0,500)

fastk = set()
for i,k in enumerate(tqdm(tweets)):
    for j,l in enumerate(range(i+1, len(tweets))):
        fastk.add((k,l))
slowk = set()
for i,k in enumerate(tqdm(tweets)):
    for j,l in enumerate(tweets):
        if j != i and (l,k) not in slowk:
            slowk.add((k,l))
print len(fastk)
print len(slowk)
for k in slowk:
    assert k in fastk or (k[1],k[0]) in fastk
for k in fastk:
    assert k in slowk or (k[1],k[0]) in fastk
