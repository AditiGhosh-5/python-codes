def count_digits(n):
    n = abs(n)

    if n == 0:
        print("Digits = 1")
        return

    count = 0
    while n > 0:
        count += 1
        n //= 10

    print("Digits =", count)

num = int(input("Enter number: "))
count_digits(num)