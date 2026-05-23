def show_menu():
    print("\n=== ATM 系統 ===")
    print("1. 查詢餘額")
    print("2. 存款")
    print("3. 提款")
    print("4. 離開")


def show_balance(balance):
    print(f"目前餘額：{balance} 元")


def deposit(balance, amount):
    if amount <= 0:
        print("存款金額必須大於 0。")
        return balance

    balance += amount
    print(f"成功存入 {amount} 元")
    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("提款金額必須大於 0。")
        return balance

    if amount > balance:
        print("餘額不足，無法提款。")
        return balance

    balance -= amount
    print(f"成功提出 {amount} 元")
    return balance


def main():
    balance = 1000

    while True:
        show_menu()
        choice = input("請選擇功能：")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            amount = int(input("請輸入存款金額："))
            balance = deposit(balance, amount)

        elif choice == "3":
            amount = int(input("請輸入提款金額："))
            balance = withdraw(balance, amount)

        elif choice == "4":
            print("感謝使用 ATM 系統。")
            break

        else:
            print("請輸入正確選項。")


main()