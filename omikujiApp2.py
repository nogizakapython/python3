# おみくじアプリ
# 新規作成  2024/2/9

# ライブラリを読み込む
import tkinter as tk
import random

# おみくじ結果を表示する関数
def dispResult():
    # おみくじの種類を配列で定義
    kuji = ['大吉', '中吉', '小吉', '吉','末吉','凶']
    # 配列の要素(0～5)からランダムに配列の番号を取得
    rand1 = random.randint(0,len(kuji)-1)
    # ラベルにおみくじの結果を表示する
    lbl.configure(text=kuji[rand1])

# GUIオブジェクトインスタンスを呼び出す
root = tk.Tk()
# アプリの大きさを指定する
root.geometry("300x200")
# ラベルオブジェクトを定義する
lbl = tk.Label(text="LABEL")
# ボタンオブジェクトを定義する
btn = tk.Button(text="CliCk", command = dispResult)
# オブジェクトを配置する
lbl.pack()
btn.pack()
# 閉じるボタンを押すまで繰り返す
tk.mainloop()
