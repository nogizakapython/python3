# 例外処理を使ってファイルの存在確認をする
# 新規作成 2023/3/14

import os

file_name = "file_test3.txt"

# if not os.path.isfile(file_name):
#     with open(file_name, mode="w") as f:
#         f.write("Saburo\n")
# else:
#     print("File exists!")
try:
    with open(file_name, mode="x") as f:
        f.write("Siro\n")
except FileExistsError:
    print("File Exist!")
