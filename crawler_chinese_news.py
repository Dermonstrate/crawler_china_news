import requests
from pyquery import PyQuery as pq
import time
import random

def get_page(url):
    #获取相应html的utf-8内容
    user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0']
    Cookie_list = ['ll="108288"; bid=yWvGAVL6Q8c; _pk_id.100001.8cb4=9ef052a9c4643216.1636442574.1.1636442574.1636442574.; _pk_ses.100001.8cb4=*; __utma=30149280.218475865.1636442585.1636442585.1636442585.1; __utmc=30149280; __utmz=30149280.1636442585.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.1.10.1636442585; dbcl2="147748543:Qa+y+Ngo/88"; ck=Kola',
                   'bid=Bc3v9b9CPF0; gr_user_id=6e495599-2cb0-4b8d-8bee-90e152adbe57; __gads=ID=77d21dca7086ba99-22244fe080ca00db:T=1627197466:RT=1627197466:S=ALNI_MZCj71jH5strHj1hMP4dypZcL5wtw; douban-fav-remind=1; __yadk_uid=njX0MVmvf3z9MQh6J15eZknYtSRfrOaz; ll="118226"; viewed="30304921_35275311_34842935_1024255_30175598"; __gpi=00000000-0000-0000-0000-000000000000; _ga=GA1.1.484906768.1627197466; _ga_RXNMP372GL=GS1.1.1635764998.1.0.1635765050.0; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1636435777%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dh1kZqv4QBoGcK-cV1wko57owiJiYCnvKJ6z8aICcOEMgHOql4GHBAAINZ4Y2ACNR%26wd%3D%26eqid%3Db5ff41f80001561100000003618a072d%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.484906768.1627197466.1635949384.1636435780.20; __utmz=30149280.1636435780.20.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; dbcl2="191043426:hAFuIB288eo"; ck=AyyO; __utmv=30149280.19104; ct=y; _pk_id.100001.8cb4=b70b06960f8adb7c.1627637011.8.1636441515.1634096342.; __utmb=30149280.182.7.1636441517038',
                   'bid=jEAtk5T5E50; gr_user_id=52bb9b91-d18b-446f-83a8-4771be906ab6; douban-fav-remind=1; ll="118217"; __utmv=30149280.17304; __yadk_uid=2wCJTpI2qptCPM6JYkBzNaYQxlZeNmtN; trc_cookie_storage=taboola%2520global%253Auser-id%3D593402db-4e6f-42e6-9019-07241206eedd-tuct7e40721; _cc_id=415bccb34a1fbf03288707072c3c4bbb; __gads=ID=effd6924e3133402-2213dd505ccc00db:T=1625933633:RT=1633795984:S=ALNI_MZvNJ67xueV4f-NklxO68f-HXZdug; ct=y; viewed="2816258_4863836_6758300_30443538_3750684_20105453_3696123_3298226_26309057_30579784"; __utmz=30149280.1636342612.45.41.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1636442540%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DxIu-LiNhZePURcJmCfX7HlYU0cFEIdku-rKEFivpY07jZPyRO_s3USt5BfQdUSa2Bai8DRLk4eIG7aczVPJMta%26wd%3D%26eqid%3Dbf1b0d570001f7af0000000661889a2f%22%5D; _pk_id.100001.8cb4=043dca47419782b9.1625890065.24.1636442540.1636342572.; _pk_ses.100001.8cb4=*; __utma=30149280.1158035249.1625795781.1636342612.1636442541.46; __utmc=30149280; __utmt=1; __utmb=30149280.1.10.1636442541']
    random_num_cookie = random.randint(0,2)
    random_num_agent = random.randint(0,4)

    headers = {
        'Cookie': Cookie_list[0],
        'User-Agent': user_agent_list[3]
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8-sig'
    if response.status_code == 200:
        return response.text
    else:
        print("Error")
        time.sleep(60)
        get_page(url)
    return None

def get_url(html):
    #通过首页获取全部详情页的url
    doc = pq(html)
    items =doc("#news_list .news_item .news_title").items
    for item in items():
        #将url存储到相应的txt文件中以备之后使用
        url = item.find('a').attr("href")
        print(url)
        if url=="None":
            continue
        file = open('D://internalship//Deloitte_consulting//Python_crawler_data//url_data.txt', 'a', encoding='utf-8')
        file.write('\n'.join([str(url),""]))
        file.close()

for i in range(0,689):
    url = 'https://sou.chinanews.com.cn/search.do?q=%E7%A5%9E%E5%8D%8E&sort=_score&start=' + str(10 * i)
    html = get_page(url)
    get_url(html)
