def check_palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

text = input("Enter text: ")
check_palindrome(text)