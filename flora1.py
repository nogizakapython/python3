# 企業概要取得ツール
# 新規開発   2024/3/2
# Create by 乃木坂好きのITエンジニア

#ライブラリのインポート
from bs4 import BeautifulSoup
import urllib3
import codecs
import datetime
import re
import os
import requests

#会社概要ページのURLの定義
get_url = "https://flora-inc.co.jp/page/company.php"
# 現在日時の取得
dt = datetime.datetime.now()
#現在日時を年4桁、月2桁、日付2桁、時間、分、秒のフォーマットで取得する
now_date = dt.strftime('%Y%m%d%H%M%S')
# 格納先ファイル名の定義
file_name = "flora" + now_date + ".txt"
#取得したHTMLから、必要なデータを抽出し、抽出ファイルに書き込む
result_file = "flora.txt"
# 検索文字列
pattern1 = '<td class="title">'
pattern2 = '<td class="content">'
pattern3 = '<td class="title">事業所所在地</td>'

# スクレイピング関数
def scrapping():
    http = urllib3.PoolManager()
    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    r = requests.get(get_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # tableタグ内の文字列を取得する
    title_text = soup.find('table')
    print(title_text,file=codecs.open(file_name,'a','utf-8'))    # セクションタグを取得する

# メイン関数
def main():
    scrapping()
    file_data = open(file_name,"r",encoding="utf-8")

    file_exist = os.path.isfile(result_file)
    if file_exist:
        os.remove(result_file)
    # テーブルタグを取得したタグファイルから、不必要tableタグデータ行を読み込んだ時にファイル出力
    # ループから抜ける。
    for line in file_data:
        result3 = re.match(pattern3,line)
        if result3:
            break
        else:
            result1 = re.match(pattern1,line)
            result2 = re.match(pattern2,line)
            # 必要なデータをファイルに出力する
            with open(result_file,mode="a",encoding="utf-8") as f:
                if result1:
                    f.write(line)
                elif result2:
                    f.write(line)
    # 出力ファイルを閉じる
    file_data.close()

if __name__ == "__main__":
    main()

