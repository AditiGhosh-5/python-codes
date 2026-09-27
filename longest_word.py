def find_longest_word(text):
    longest = ""
    current = ""

    for ch in text + " ":
        if ch != " ":
            current += ch
        else:
            if len(current) > len(longest):
                longest = current
            current = ""

    print("Longest word:", longest)

text = input("Enter sentence: ")
find_longest_word(text)