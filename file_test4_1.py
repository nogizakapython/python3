# ファイルの追記処理
# 連想配列を使った書き込み
# 2023/3/14

file_name = "file_test4_1.txt"

names = [{"name":"秋元真夏","score":80},{"name":"白石麻衣","score":55},{"name":"西野七瀬","score":60}]


with open(file_name, mode="a") as f:
    for score in names:
        f.write(f"{score['name']}の成績は{score['score']}です。\n")
