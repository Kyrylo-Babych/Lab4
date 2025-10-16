def quicksort(items):
    if len(items) <= 1:
        return items
    
    pivot = items[0]
    rest_of_items = items[1:]

    lesser_items = []
    greater_items = []
    for element in rest_of_items:
        if element <= pivot:
            lesser_items.append(element)
        else:
            greater_items.append(element)
            
    return quicksort(lesser_items) + [pivot] + quicksort(greater_items)

try:
    user_list = list(map(int, input('Введіть список чисел для сортування через пробіл: ').split()))
    
    # Сортуємо отриманий список
    sorted_list = quicksort(user_list)
    
    print(f"Початковий список: {user_list}")
    print(f"Відсортований список: {sorted_list}")

except ValueError:
    print("Помилка! Будь ласка, вводьте тільки числа, розділені пробілом.")