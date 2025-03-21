def replace_missing_with_average(numbers):
    # Найти индекс пропущенного элемента
    missing_index = numbers.index(None)

    # Вычислить сумму всех элементов, кроме пропущенного
    total_sum = sum(num for i, num in enumerate(numbers) if i != missing_index)

    # Количество элементов включает пропущенный элемент
    count = len(numbers)

    # Рассчитать среднее арифметическое
    average = total_sum / count

    # Заменить пропущенный элемент средним арифметическим
    numbers[missing_index] = average


# Ваш список чисел
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

replace_missing_with_average(numbers)

# Вывести обновленный список
print(numbers)


