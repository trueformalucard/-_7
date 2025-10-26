with open("file.txt", "r") as file:
    text = file.read()

words = text.split()
words = [word.strip('.,!?;:"()').lower() for word in words]

total_words = len(words)

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)
most_common_count = word_count[most_common_word]

print(f"Общее количество слов: {total_words}")
print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {most_common_count} раз)")