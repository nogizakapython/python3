# ファイルの存在確認処理
# 新規作成 2023/3/14

# osライブラリを読み込む
import os

file_name = "names1.txt"

# ファイルが存在しなかったら書き込む
if not os.path.isfile(file_name):
    with open(file_name, mode="w") as f:
        f.write("Saburo\n")
# ファイルが存在したらメッセージを出力する
else:
    print("File exists!")
