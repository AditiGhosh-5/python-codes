def count_characters(text):
    count = 0
    for ch in text:
        count += 1
    print("Characters =", count)

text = input("Enter text: ")
count_characters(text)