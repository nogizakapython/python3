# 数当てゲーム

import random

answer = random.randint(1, 10)
count = 0

while True:
    print("Your guess? ", end="")
    guess = int(input())
    count += 1
    
    if answer == guess:
        print("Bingo! It took %i guesses!" %count)
        break
    elif answer > guess:
        print("Bigger!")
    else:
        print("Smaller!")