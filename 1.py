n = int(input("Введіть кількість елементів Фібоначчі: "))

if n <= 2:
    print("Помилка: будь ласка, введіть число більше 2.")
    quit()
else:
    fib_sequence = [1, 1]

    for i in range(n - 2):
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])

    print("Результат:", fib_sequence)