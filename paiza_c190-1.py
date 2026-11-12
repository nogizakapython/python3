import sys

def solve():
    # 1行目から H, W, K を読み込む
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    H, W, K = map(int, input_data[0].split())
    
    # 上下の枠となる文字列（幅 W + 2K の '#'）
    border_line = '#' * (W + 2 * K)
    # 左右の枠となる文字列（幅 K の '#'）
    side_border = '#' * K
    
    # 1. 上部の枠を K 行出力
    for _ in range(K):
        print(border_line)
        
    # 2. 元の画像の各行の左右に K 個の '#' をつけて出力
    for i in range(1, H + 1):
        print(side_border + input_data[i] + side_border)
        
    # 3. 下部の枠を K 行出力
    for _ in range(K):
        print(border_line)

if __name__ == '__main__':
    solve()