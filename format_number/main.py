def format_number_with_spaces(number: str, sep: str = ",", places: str = " ") -> str:
    symbol = number.find(sep)                         # ищем индекс разделителя целой и дробной части
    if symbol != -1:                                  # если индекс не равен (-1) - т.е. существует, тогда:
        part1_list = list(number[0:symbol])           # первый список равен началу строки до разделителя (целой части)
        part2_list = list(number[symbol:])            # второй - от разделителя до конца строки (дробной части)
    else:
        part1_list = list(number)              # в противном случае - первый список равен всей строке
        part2_list = []                        # а второй - пустому списку (работаем со списками, т.к. они изменяемы)
    part0_list = []                            # нулевой список - для непопавших в разряд цифр
    space = places                             # разделитель между разрядами

    number_of_category = len(part1_list) // 3  # вычиляем число разрядов для первой части строки
    out_of_category = len(part1_list) % 3      # вычисляем количество цифр, которые не попали в разряд

    if out_of_category > 0 and number_of_category > 0:  # обработка цифр непопавших в разряд (т.е. > 999)
        for i in range(out_of_category):                # проходим по непопавшим в разряд цифрам
            part0_list.append(part1_list.pop(0))        # вырезаем их из первого списка и добавляем в нулевой
        part0_list.append(space)                        # когда закончим - добавим разделитель в конец

    j = 3                                         # обработка разрядов, установим начальное значение для разделителя
    for i in range(number_of_category - 1):       # обходим все все разеделители, которых на один меньше числа разрядов
        part1_list.insert(j, space)               # добавляем разделитель после окончания разряда
        j += 4                                    # следующее значение индекса для разделителя

    new_string = "".join(part0_list) + "".join(part1_list) + "".join(part2_list)    # собираем строку воедино из списков
    return new_string                                                               # возвращаем ее из функции


print(format_number_with_spaces("12345678,9"))       # вызываем функцию
