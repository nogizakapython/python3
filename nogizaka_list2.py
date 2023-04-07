# 乃木坂写真集リスト
# 新規作成 2023/4/7

# ライブラリのインポート
from nogizaka_list2f import BookItem

# インスタンス変数の定義
item1 = BookItem('賀喜遥香','まっさら', 2200)
item2 = BookItem('梅澤美波','夢の近く', 1980)
item3 = BookItem('山下美月','忘れられない人', 1980)
item4 = BookItem('与田祐希','無口な時間', 2035)


# menu_items配列
menu_items = [item1, item2, item3, item4]

#index変数の定義
index = 0
# 選択番号変数の定義
select_number = 0
# 購入冊数変数の定義
count = 0

for item in menu_items:
  print(str(index) + "." + item.info())
  index += 1

while True:
  try:
    select_number1 = int(input(f"0から{len(menu_items)}までの番号を入力してください"))
    if select_number1 < 0 or select_number1 >= len(menu_items):
      raise ValueError 
    else:
      select_number = select_number1
      break
    
  except:
    print(f"選択された番号が間違っています。")  

selected_menu = menu_items[select_number]

# 「 選択されたメニュー: 〇〇 」と出力してください
print("選択されたメニュー→" + selected_menu.membercheck())

while True:
  try:
    count_number = int(input(f"購入冊数を1以上の整数を入力してください"))
    if count_number < 1:
      raise ValueError 
    else:
      count = count_number
      break
    
  except:
    print(f"購入冊数の入力方法が違います")  

result = selected_menu.get_total_price(count)
print(f"購入合計金額は{result}円です")