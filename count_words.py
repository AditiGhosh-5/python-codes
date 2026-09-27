def count_words(text):
    words = 0
    w = False

    for ch in text:
        if ch != " " and w == False:
            words += 1
            w = True
        elif ch == " ":
            w = False

    print("Words =", words)

text = input("Enter sentence: ")
count_words(text)