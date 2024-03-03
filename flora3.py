#  会社概要をエクセルファイルに書き込む処理
#  新規作成  2024/3/3
#  Create by  乃木坂好きのITエンジニア

# ライブラリのインポート
import re
import openpyxl as op
import shutil
import os

#項目を取得
pattern1 = '<td class="title">'

#内容を取得
patturn2 = '<td class="content">'
patturn3 = '</td>'
patturn4 = '<br/>'

# pタグを取得
patturn5 = '<p>'

# データ切り替えレコード変数の定義
record1 = '<td class="content">'
record2 = '<td class="title">事業内容</td>'

# 入力ファイル
input_file =  "flora.txt"
# テンプレートエクセルファイル
template_excel_file = "会社概要.xlsx"
# 会社名、ホールディング名判定カウント
w_count = 0
# pタグ会社名、ホールディング名判定カウント
w_p_count = 0
w_p_company_content = ""
w_p_holding_content = ""



# タイトルのデータクレンジング関数
def title_cleansing(line):
    w_array1 = line.split(">")
    w_item = w_array1[1]
    w_item = w_item.replace('</td',"")
    return w_item

# 会社内容のデータクレンジング関数
def content_cleansing(line):
    w_array2 = line.split(">")
    w_content = w_array2[1]
    w_content = w_content.replace('<a href="',"")
    w_content = w_content.replace('tel:',"")
    w_content = w_content.replace('mailto:',"")
    w_content = w_content.replace('</td',"")
    w_content = w_content.replace('<br/',"")
    w_content = w_content.replace('"',"")
    return w_content

# pタグ内容のデータクレンジング関数
def p_tag_cleansing(line):
    w_array3 = line.split(">")
    w_p_content = w_array3[1]
    w_p_content = w_p_content.replace('</p',"")
    w_p_content = w_p_content.replace('・'," ")
    return w_p_content



# メイン処理

#タグ抽出ファイルを開く
file_data = open(input_file,"r",encoding="utf-8")
for line in file_data:
    line = line.replace("\n","")
    result1 = re.match(pattern1,line)
    result2 = re.match(patturn2,line)
    result3 = re.search(patturn3,line)
    result4 = re.search(patturn4,line)
    result5 = re.search(patturn5,line)

    if line == record1:
        w_p_count += 1
    if line == record2:
        w_p_count = 0

    if result1:
        w_count = 0
        w_item = title_cleansing(line)

    if (result2 and result3) or (result2 and result4):
        w_content = content_cleansing(line)
        if w_count == 0:
            w_company_content = w_content
        elif w_count == 1:
            w_holding_content = w_content
        w_count += 1

    if result5:
        w_p_content = p_tag_cleansing(line)
        print(w_p_content)
        if w_p_count == 1:
            w_p_company_content +=  w_p_content
        elif w_p_count == 2:
            w_p_holding_content += w_p_content
