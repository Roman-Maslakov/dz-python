def math_power(n1, n2):
    if n2 == 1:
        return n1
    return n1 * math_power(n1, n2 - 1)

a = int(input("Input A: "))
b = int(input("Input B: "))

print(math_power(a, b))