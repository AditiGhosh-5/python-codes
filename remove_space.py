def remove_spaces(text):
    result = ""

    for ch in text:
        if ch != " ":
            result += ch

    print(result)

text = input("Enter text: ")
remove_spaces(text)