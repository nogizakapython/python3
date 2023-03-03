# 新規作成 2023/3/3
# 例外処理

# SyntaxError : () '' "" for/if/while
# IndentationError

# 例外
# NameError
# TypeError
# ValueError
try:
    initial_balance = int(input("Initial Balance? "))
except ValueError:
    print("Invalid input,exiting.....")
    exit()
RATE = 1.1
for year in range(3):
    print(f"Year {year}: {initial_balance * RATE ** year:,.2f}")
