# crawler_china_news

使用的程序包：
pyquery
gensim
thulac
python3.8

本项目目的：
对中国神华集团的舆情信息进行获取并整理，形成可视化的结果。

crawler_chinese_news.py：
按相关度排序爬取关键词为“神华”的中国新闻网发布的信息，爬取内容为相关新闻的url链接

article_content.py：
根据crawler_chinese_news.py中获取的url链接获取相关新闻正文，爬取内容以txt文档形式保存

sentence_count.py：
对所爬取的新闻进行清洗、词频统计

LDA.py：
对所爬取的新闻进行LDA聚类


