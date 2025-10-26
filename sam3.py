with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

letter_count = 0
word_count = 0
line_count = len(lines)

for line in lines:
    for char in line:
        if char.isalpha() and char.isascii():
            letter_count += 1

    words = line.split()
    word_count += len(words)

print(f"Input file contains:")
print(f"{letter_count} латинский")
print(f"{word_count} слов")
print(f"{line_count} строк")