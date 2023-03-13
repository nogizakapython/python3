# mathライブラリ
# 新規作成 2023/3/13

# mathライブラリを読み込む
import math
# √2
print(math.sqrt(2))
# 3.5より大きい最小の整数
print(math.ceil(3.5))
# 3.5より小さい最大の整数
print(math.floor(3.5))
# 12,20,8の最大公約数
print(math.gcd(12,20,8))

# 銀行まるめ
print(round(3.5))
print(round(2.5))

# 掛け算の結果の論理評価
print(0.1 * 3 == 0.3)
print(math.isclose(0.1 * 3,0.3))
