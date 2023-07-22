numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Разобьем список на два без None, используя слайсирование с шагом 1
first_list = numbers[0: 4]
second_list = numbers[5:]

# Объединим оба списка и посчитаем их сумму
sum_ = sum(first_list + second_list)
# print(sum_)

# Посчитаем количество элементов в списке numbers
count_ = len(numbers)
# print(count_)

# Посчитаем среднее арифметическое
average_ = sum_ / count_
# print(average_)

# Добавим среднее арифметическое в список вместо None
numbers[4] = average_

print("Измененный список:", numbers)
