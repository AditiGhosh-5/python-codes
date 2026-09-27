def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
print("Largest:", find_largest(a, b, c))