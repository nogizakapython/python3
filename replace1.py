###############################################################
####     ログファイル半角スペースからTabへの置換ツール    #######
###############################################################
# モジュールのインポート
import re
import os

IN_FILE = "NCM29_202310.log"
OUT_FILE = "NCM29_202310replace.log"

if os.path.exists(OUT_FILE):
    os.remove(OUT_FILE)

with open(IN_FILE,mode='r') as f:
    for line in f:
        line1 = line.replace(" ","\t")
        f2 = open(OUT_FILE,'a')
        f2.write(line1)
        f2.close()

