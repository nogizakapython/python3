# web上のPDFファイルをローカルに保存せずに文字列情報を取得
from io import BytesIO
from urllib import request
from pdfminer.high_level import extract_text

url = "https://flora-inc.co.jp/score/%E4%BB%A4%E5%92%8C5%E5%B9%B4%E5%BA%A6%E3%83%95%E3%83%AD%E3%83%BC%E3%83%A9IT%E9%83%A8%E9%96%80%E6%94%AF%E6%8F%B4%E5%AE%9F%E7%B8%BE.pdf"

with request.urlopen(url) as res:
    f = BytesIO(res.read())
    text = extract_text(f)
    print(text[:600])
