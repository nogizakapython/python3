###############################################################
####     ログファイル半角スペースからTabへの置換ツール    #######
###############################################################
# モジュールのインポート
import re
import os

# ファイル名
IN_FILE = "gra_nogizaka.txt"
OUT_FILE = "gra_nogizakareplace.txt"

# 古い置換ファイルがあれば削除
if os.path.exists(OUT_FILE):
    os.remove(OUT_FILE)

# 半角スペースファイルから１行ずつ読み込み、半角スペースをtabスペースに置換し、ファイルに
# 出力する。
with open(IN_FILE,mode='r',encoding='utf-8') as f:
    for line in f:
        line1 = line.replace(" ","\t")
        f2 = open(OUT_FILE,'a')
        f2.write(line1)
        f2.close()

