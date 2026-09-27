def character_frequency(text, ch):
    count = 0

    for c in text:
        if c == ch:
            count += 1

    print("Frequency =", count)

text = input("Enter text: ")
character = input("Enter character: ")
character_frequency(text, character)