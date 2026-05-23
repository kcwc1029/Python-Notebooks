def show_menu(menu):
    print("=== 菜單 ===")
    for item, price in menu.items():
        print(f"{item}: {price} 元")


def add_order(menu, orders, item):
    if item in menu:
        orders.append(item)
        print(f"已加入：{item}")
    else:
        print("沒有這個餐點。")


def calculate_total(menu, orders):
    total = 0
    for item in orders:
        total += menu[item]
    return total


def print_receipt(menu, orders):
    print("\n=== 收據 ===")

    if not orders:
        print("沒有點任何餐點。")
        return

    for item in orders:
        print(f"{item}: {menu[item]} 元")

    total = calculate_total(menu, orders)
    print(f"總金額：{total} 元")


def main():
    menu = {
        "漢堡": 60,
        "薯條": 35,
        "可樂": 25,
        "雞塊": 45,
        "蛋餅": 40
    }

    orders = []

    while True:
        show_menu(menu)
        choice = input("\n請輸入餐點名稱，輸入 q 結帳：")

        if choice == "q":
            break

        add_order(menu, orders, choice)

    print_receipt(menu, orders)


main()