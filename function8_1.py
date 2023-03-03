# 早期リターン処理
# 新規作成 2023/3/3

def print_username(name):
    if name == "admin":
        return
    if name == "support":
        return

    print(name)

print_username("taro")
print_username("jiro")
print_username("admin")
print_username("sakura")
print_username("support")
