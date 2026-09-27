def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum =", total)

n = int(input("Enter n: "))
sum_natural(n)