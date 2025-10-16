fib_list = [0, 1]

while True:
    next_fib = fib_list[-1] + fib_list[-2]
    if next_fib <= 50:
        fib_list.append(next_fib)
    else:
        break

print(f"Множина чисел Фібоначчі до 50: {fib_list}")