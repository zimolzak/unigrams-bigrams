import sys
import re

if len(sys.argv) > 1:
    print(sys.argv[1])

corpus = open('pride_prej.txt', 'r').read(24000)

words_list = re.sub(r"[^A-Za-z0-9 \n]", "", corpus).lower().split()

documents = []
while len(words_list) >= 200:
    documents.append(words_list[0:200])
    del words_list[0:200]

print(str(documents[0]) +  '\n\n\n' + str(documents[1]))
