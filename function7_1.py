# デフォルト仮引数
# 新規作成 2023/3/3

#デフォルト仮引数
def show_time(h,m,s=0,ms=0):
    # 数値を0埋めする
    print(f"{h:02}:{m:02}:{s:02}.{ms:03}")

show_time(4,12,23,120)
show_time(10,7,5,2)
show_time(2,19)
show_time(4,3,1)
