def sum(n1, n2):
    if n2 == 1:
        return n1 + 1
    return sum(n1 + 1, n2 -1)

a = int(input("Input A: "))
b = int(input("Input B: "))

print(sum(a, b))