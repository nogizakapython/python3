# 乃木坂写真集リスト
# 新規作成 2023/4/7


from nogizaka_list1f import BookItem

item1 = BookItem('賀喜遥香','まっさら', 2200)
item2 = BookItem('梅澤美波','夢の近く', 1980)
item3 = BookItem('山下美月','忘れられない人', 1980)
item4 = BookItem('与田祐希','無口な時間', 2035)
# item5 = BookItem('秋元真夏','振り返れば乃木坂', 2300)

# 指定されたリストを変数 menu_items に代入してください
# menu_items = [item1, item2, item3, item4,item5]
menu_items = [item1, item2, item3, item4]


# for 文を作成してください
for item in menu_items:
  print(item.info())
  print(item.membercheck())
  