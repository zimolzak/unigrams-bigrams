import re

EST_DOCS = 20
WORDS_PER_DOC = 1667


bytes_per_word = 6 # just empiric fudge factor
bytes_to_read = bytes_per_word * WORDS_PER_DOC * EST_DOCS
corpus = open('pride_prej.txt', 'r').read(bytes_to_read)
words_list = re.sub(r"[^A-Za-z0-9 \n]", "", corpus).lower().split()

documents = []
while len(words_list) >= WORDS_PER_DOC:
    documents.append(words_list[0:WORDS_PER_DOC])
    del words_list[0:WORDS_PER_DOC]

pct = str(round(bytes_to_read / 704881.0 * 100, 1))
print("Read %d bytes (%s pct). Created %d documents of %d words each." % \
          (bytes_to_read, pct, len(documents), WORDS_PER_DOC))

for (i, D) in enumerate(documents):
    n_unigrams = len(set(D))
    bigrams = []
    bg_count = {}
    for j in range(len(D)):
        if j+1 >= len(D):
            continue
        bg = D[j] + ' ' + D[j+1]
        bigrams.append(bg)
        if bg_count.has_key(bg):
            bg_count[bg] += 1
        else:
            bg_count[bg] = 1
    n_bigrams = len(set(bigrams))
    print("%d uni \t %d bi" % (n_unigrams, n_bigrams))

    if i + 1  == len(documents):
        print("")
        print("Most common bigrams in last document:")
        for k in sorted(bg_count, key=bg_count.get, reverse=True):
            if bg_count[k] > 2:
                print k, bg_count[k]
