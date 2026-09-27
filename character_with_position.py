def display_position(text):
    for i in range(len(text)):
        print("Position", i, ":", text[i])

text = input("Enter text: ")
display_position(text)