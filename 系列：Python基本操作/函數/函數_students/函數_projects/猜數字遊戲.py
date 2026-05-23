### 猜數字遊戲-文字版
# 程式會隨機生成一個介於 1 到 100 之間的目標數字，玩家的目標是在限定的猜測次數內猜中該數字。本遊戲最大的特色是提供了兩種難度模式，以調整遊戲的挑戰性。

import random

# 設置難度模式和允許的猜測次數
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    """
	讓玩家選擇遊戲難度並設定猜測次數。
	"""
    while True:
        level = input("請選擇一個難度。輸入 'easy' (簡單) 或 'hard' (困難): ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("輸入無效，請重新輸入。")

def check_guess(guess, answer, turns):
    """
	檢查猜測的數字是否正確，並返回剩餘的猜測次數
	"""
    if guess > answer:
        print("太高了。")
        return turns - 1
    elif guess < answer:
        print("太低了。")
        return turns - 1
    else:
        print(f"你猜對了！答案是 {answer}。")
        return 0 # 猜對了，剩餘次數歸零以結束遊戲
    
### 遊戲主流程
print("猜數字遊戲")
print("我正在想一個 1 到 100 之間的數字。")

answer = random.randint(1, 100)

# 設置難度
turns = set_difficulty()
print(f"你選擇了 {turns} 次機會來猜數字。")
# 玩家猜的數字
guess = 0

# 遊戲迴圈：直到猜對 (turns=0) 或次數用完
while guess != answer and turns > 0:
	print(f"你還剩下 {turns} 次猜測機會。")

	# 處理無效輸入
	try:
		guess = int(input("請猜一個數字: "))
	except ValueError:
		print("無效輸入，請輸入一個整數。")
		continue # 跳過本次循環，不扣除次數

	# 檢查猜測結果並更新剩餘次數
	turns = check_guess(guess, answer, turns)

	if turns > 0 and guess != answer:
		print("再猜一次。")

	elif turns == 0 and guess != answer:
		print("你所有的猜測機會都用完了。你輸了！")
		print(f"正確答案是 {answer}")