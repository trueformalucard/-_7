def add_expense():
    amount = input("Введите сумму расхода: ")
    category = input("Введите категорию расхода: ")

    with open("expenses.txt", "a", encoding="utf-8") as file:
        file.write(f"{amount} - {category}\n")


def show_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            expenses = file.readlines()

        if not expenses:
            print("Расходы отсутствуют")
            return

        print("Список расходов:")
        for expense in expenses:
            print(expense.strip())
    except FileNotFoundError:
        print("Файл с расходами не найден")


while True:
    print("\n1 - Добавить расход")
    print("2 - Показать расходы")
    print("3 - Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break