###############################################################
####     ログファイル半角スペースからTabへの置換ツール    #######
###############################################################
# モジュールのインポート
import re
import os

FILE_NAME = "gra_nogizaka.txt"
OUT_FILE = "gra_nogizakareplace.txt"

if os.path.exists(OUT_FILE):
    os.remove(OUT_FILE)

with open(FILE_NAME,mode='r') as f:
    for line in f:
        line1 = line.replace(" ","\t")
        f2 = open(OUT_FILE,'a')
        f2.write(line1)
        f2.close()

