def count_case(text):
    upper = lower = digits = spaces = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1

    print("Uppercase:", upper)
    print("Lowercase:", lower)
    print("Digits:", digits)
    print("Spaces:", spaces)

text = input("Enter text: ")
count_case(text)