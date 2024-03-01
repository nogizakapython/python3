import requests
from bs4 import BeautifulSoup
import codecs
file_name = "test21.txt"
# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('https://www.nikkei.com/news/jinji/hatsurei/')

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

# title タグの文字列を取得する
title_text = soup.find_all(class_=["dateHeadline_d18sgrke","container_cyywo23"])
for i in list(title_text):
    print(i,file=codecs.open(file_name,'a','utf-8'))
# print(title_text)
# > Quotes to Scrape

# ページに含まれるリンクを全て取得する
# links = [url.get('href') for url in soup.find_all('a')]
# print(links)
# > ['/', '/login', '/author/Albert-Einstein', '/tag/change/page/1/', '/tag/deep-thoughts/page/1/', '/tag/thinking/page/1/', '/tag/world/page/1/', '/author/J-K-Rowling', '/tag/abilities/page/1/', '/tag/choices/page/1/', '/author/Albert-Einstein', '/tag/inspirational/page/1/', '/tag/life/page/1/', '/tag/live/page/1/', '/tag/miracle/page/1/', '/tag/miracles/page/1/', '/author/Jane-Austen', '/tag/aliteracy/page/1/', '/tag/books/page/1/', '/tag/classic/page/1/', '/tag/humor/page/1/', '/author/Marilyn-Monroe', '/tag/be-yourself/page/1/', '/tag/inspirational/page/1/', '/author/Albert-Einstein', '/tag/adulthood/page/1/', '/tag/success/page/1/', '/tag/value/page/1/', '/author/Andre-Gide', '/tag/life/page/1/', '/tag/love/page/1/', '/author/Thomas-A-Edison', '/tag/edison/page/1/', '/tag/failure/page/1/', '/tag/inspirational/page/1/', '/tag/paraphrased/page/1/', '/author/Eleanor-Roosevelt', '/tag/misattributed-eleanor-roosevelt/page/1/', '/author/Steve-Martin', '/tag/humor/page/1/', '/tag/obvious/page/1/', '/tag/simile/page/1/', '/page/2/', '/tag/love/', '/tag/inspirational/', '/tag/life/', '/tag/humor/', '/tag/books/', '/tag/reading/', '/tag/friendship/', '/tag/friends/', '/tag/truth/', '/tag/simile/', 'https://www.goodreads.com/quotes', 'https://scrapinghub.com']

# class が quote の div 要素を全て取得する
# quote_elms = soup.find_all('div', {'class': 'quote'})
# print(len(quote_elms))
# > 10