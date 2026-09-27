def reverse_loop(text):
    rev = ""
    for ch in text:
        rev = ch + rev
    print("Loop:", rev)

text = input("Enter text: ")
reverse_loop(text)