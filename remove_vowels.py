def remove_vowels(text):
    result = ""

    for ch in text:
        if ch.lower() not in "aeiou":
            result += ch

    print(result)

text = input("Enter text: ")
remove_vowels(text)