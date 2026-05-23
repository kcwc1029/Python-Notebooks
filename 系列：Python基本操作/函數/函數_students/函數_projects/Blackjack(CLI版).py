### 摘要
# 這是一個在命令列介面（CLI）運行的經典 21點遊戲。
# 玩家的目標是讓手牌總分 盡量接近 21 點但不超過，並擊敗電腦莊家。

### 遊戲特色
# - 初始發牌：玩家與莊家各拿兩張牌。
# - 莊家隱藏牌：只顯示莊家的第一張牌，增加懸念。
# - 玩家選擇：可決定要牌 (y) 或停牌 (n)。
# - A牌彈性：Ace 可算 11 點，若超過 21 會自動改為 1 點。
# - 莊家策略：莊家在總分 < 17 時會自動要牌。
# - 判斷機制：支援 Blackjack（首兩張牌即 21）與爆牌（超過 21）。

import random # 使用randim隨機

# 發一張牌
def deal_card():
    """發牌並返回一張隨機的牌。"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# 計算排的分數
def calculate_score(cards):
    """計算牌組的總分。"""
    # 如果有 2 張牌且分數為 21，則是 Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 代表 Blackjack
    # 如果分數大於 21 且牌組中有 11 (A)，將其改為 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# 比較分數(傳入玩家跟電腦的分數)
def compare_scores(user_score, computer_score):
    """比較玩家和電腦的分數並返回遊戲結果。"""
    if user_score == computer_score:
        return "平手 🙃"
    elif computer_score == 0:
        return "對手有 Blackjack，你輸了 😩"
    elif user_score == 0:
        return "你有 Blackjack，你贏了 😁"
    elif user_score > 21:
        return "你爆牌了，你輸了 😭"
    elif computer_score > 21:
        return "對手爆牌了，你贏了 😀"
    elif user_score > computer_score:
        return "你贏了 😊"
    else:
        return "你輸了 😢"
    
    # Blackjack 遊戲主流程
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # 初始發牌
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 玩家決策迴圈
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   你的牌組：{user_cards}, 目前分數: {user_score}")
        print(f"   電腦的第一張牌: {computer_cards[0]}")

        # 檢查是否有人拿到 Blackjack (0) 或 爆牌 (>21)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("要再拿一張牌嗎？輸入 'y' 繼續，或輸入 'n' 停牌: ")
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 玩家結束後，若玩家沒爆牌，則換電腦要牌 (Dealer's Turn)
    # 注意：如果玩家已經 Blackjack 或爆牌，電腦就不需要再抽牌了
    while computer_score != 0 and computer_score < 17 and user_score <= 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # --- 關鍵修正：輸出最終結果 ---
    print("\n" + "="*30)
    print(f"   你的最終手牌: {user_cards}, 最終分數: {user_score}")
    print(f"   電腦的最終手牌: {computer_cards}, 最終分數: {computer_score}")

    # 呼叫你寫好的比較函數並印出結果
    result = compare_scores(user_score, computer_score)
    print(f"   結果：{result}")
    print("="*30 + "\n")

if __name__ == "__main__":
    # 遊戲迴圈
    while True:
        n = input("你想玩一場 Blackjack 遊戲嗎？輸入 'y' 繼續或 'n' 退出: ")
        if n == "y": play_game()
        else: break
    print("感謝您的遊玩！")