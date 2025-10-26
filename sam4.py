with open("input.txt", "r", encoding="utf-8") as file:
    banned_words = file.read().split()


text = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!!"


for banned_word in banned_words:
    start = 0
    while start < len(text):

        index = text.lower().find(banned_word.lower(), start)
        if index == -1:
            break

        stars = '*' * len(banned_word)
        text = text[:index] + stars + text[index + len(banned_word):]
        start = index + len(stars)

print("Результат:")
print(text)