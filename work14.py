# 新規作成 2023/3/7
# リスト内包表記を使った処理の練習

member = ["白石麻衣","生田絵梨花","松村沙友理","西野七瀬","高山一実"]

# 生田絵梨花以外のメンバーをllc_member配列に格納する
llc_member = [men for men in member if men != "生田絵梨花"]

print(llc_member)

member2 = ["白石麻衣","生田絵梨花","松村沙友理","西野七瀬","高山一実","秋元真夏"]

# 生田絵梨花と秋元真夏をnllc_member配列に格納する
nllc_member = [men2 for men2 in member2 if men2 == "生田絵梨花" or men2 == "秋元真夏"]

print(nllc_member)

