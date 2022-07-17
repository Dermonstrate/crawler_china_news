import thulac
import re
from gensim import corpora, models
import os
with open("D:/internalship/Deloitte_consulting/Python_crawler_data/stopwords_cn.txt","r",encoding="utf-8") as f:
    stopwords_list = f.readlines()
stopwords = [stopword.strip() for stopword in stopwords_list]

fin = open("D:/internalship/Deloitte_consulting/Python_crawler_data/merge.txt", "r", encoding="utf8")

lac = thulac.thulac(seg_only=True)
texts = []

data = fin.read()
words = lac.cut(data)
print(words)
text = []
for word in words:
    real_word = re.sub(r'[^\u4e00-\u9fa5]+', '', word[0])
    if len(real_word) > 1 and real_word not in stopwords:
        text.append(real_word)
    print(word)
print(text)
wordcount = {}
for word in text:
    wordcount[word] = wordcount.get(word, 0)+1
print(sorted(wordcount.items(), key=lambda x:x[1], reverse=True)[:30])
fin.close()

