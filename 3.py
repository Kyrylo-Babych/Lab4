def insert_after():
    A = list(map(int, input('Введіть список: ').split()))
    target_element = int(input('Введіть елемент для пошуку: '))
    new_element = int(input('Введіть новий елемент: '))

    result = []

    for element in A:
        result.append(element)
        if element == target_element:
            result.append(new_element)

    print("Результат:", result)
    return result

insert_after()