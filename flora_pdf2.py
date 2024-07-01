from pdfminer.layout import LAParams
from io import BytesIO
from urllib import request
from pdfminer.high_level import extract_text

url = "https://flora-inc.co.jp/score/%E4%BB%A4%E5%92%8C5%E5%B9%B4%E5%BA%A6%E3%83%95%E3%83%AD%E3%83%BC%E3%83%A9IT%E9%83%A8%E9%96%80%E6%94%AF%E6%8F%B4%E5%AE%9F%E7%B8%BE.pdf"


laparams = LAParams(
    line_overlap=0.5,
    char_margin=2,
    line_margin=0.5,
    word_margin=0.1,
    boxes_flow=0.5,
    detect_vertical=False,
    all_texts=False
)

with request.urlopen(url) as res:
    f = BytesIO(res.read())
    text = extract_text(f, laparams=laparams, page_numbers=[0])
