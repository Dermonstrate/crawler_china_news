import thulac
import re
from gensim import corpora, models
import os
with open("D:/internalship/Deloitte_consulting/Python_crawler_data/stopwords_cn.txt","r",encoding="utf-8") as f:
    stopwords_list = f.readlines()
stopwords = [stopword.strip() for stopword in stopwords_list]

fnames = os.listdir("D:/internalship/Deloitte_consulting/Python_crawler_data/article")
articles = []
for fn in fnames:
    if fn[-3:] != "txt":
        continue
    fin = open("D:/internalship/Deloitte_consulting/Python_crawler_data/article/" + fn, "r", encoding="utf8")
    articles.append(fin.read()) # readline()
    fin.close()

lac = thulac.thulac(seg_only=True)
i=0
texts = []
for article in articles:
    print(i)
    i = i+1
    data = article
    words = lac.cut(data)
    text = []
    for word in words:
        real_word = re.sub(r'[^\u4e00-\u9fa5]+', '', word[0])
        if len(real_word) > 1 and real_word not in stopwords:
            text.append(real_word)
    if text:
        texts.append(text)
print(texts)
print("Step1 Finished")
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# 建立 LDA 模型
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20, iterations= 10000)

# 打印所有主题信息
for topic in lda.print_topics(num_words=20, num_topics=20):
    print(topic)
    k = open("D:/internalship/Deloitte_consulting/Python_crawler_data/lda_data.txt", "a", encoding="utf-8")
    k.write(str(topic))
    k.write("\n")
    k.close()