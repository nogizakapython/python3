# 新規作成 2023/3/2
# 2つの文字列を受け取ってFirstname lastnameを出力する

num = 0
fname = ""
lname = ""
separator = "*="
while True:
  input_str = input("スペース分けでFirstname,lastnameを入力してください")
  s = input_str.rstrip().split(' ')
  num = len(s)
  if num == 2:
    print("入力チェックOK")
    break
  else:
    print("入力が違います")

for i in range(num):
  if i == 0:
    fname = s[i]
  elif i == 1:
    lname = s[i]

print(separator * 10)
print(fname + " " + lname)
print(separator * 10)
