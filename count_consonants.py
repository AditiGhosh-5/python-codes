def count_consonants(text):
    count = 0

    for ch in text.lower():
        if ch.isalpha() and ch not in "aeiou":
            count += 1

    print("Consonants =", count)

text = input("Enter text: ")
count_consonants(text)