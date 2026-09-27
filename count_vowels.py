def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    print("Vowels =", count)

text = input("Enter text: ")
count_vowels(text)