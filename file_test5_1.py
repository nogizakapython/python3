# ファイルの読み込み
# 2023/3/14

file_name = "file_test4_1.txt"

names = [{"name":"秋元真夏","score":80},{"name":"白石麻衣","score":55},{"name":"西野七瀬","score":60}]


with open(file_name, mode="r") as f:
    names = f.read()

print(names,end="")
