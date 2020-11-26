n = int(input("Введите число: "))
result = 1
for i in range(n, n%2, -2):
    result *= i
print("n!! =", result)
