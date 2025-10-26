def write_secret():
    message = input("Введите секретное сообщение: ")

    secret = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                secret += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                secret += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            secret += char

    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(secret + "\n")
    print("Сообщение записано в дневник!")


def read_secrets():
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            secrets = file.readlines()

        if not secrets:
            print("Дневник пустой")
            return

        print("\nСекретные сообщения:")
        for i, secret in enumerate(secrets, 1):
            message = ""
            for char in secret.strip():
                if char.isalpha():
                    if char.islower():
                        message += chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
                    else:
                        message += chr((ord(char) - ord('A') - 1) % 26 + ord('A'))
                else:
                    message += char
            print(f"{i}. {message}")
    except FileNotFoundError:
        print("Дневник не найден")


while True:
    print("\n1 - Записать секрет")
    print("2 - Прочитать секреты")
    print("3 - Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        write_secret()
    elif choice == "2":
        read_secrets()
    elif choice == "3":
        break