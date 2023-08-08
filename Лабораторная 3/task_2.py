# TODO Напишите функцию find_common_participants
def find_common_participants(first_string, second_string, symbol=","):
    first_list = first_string.split(symbol)
    second_list = second_string.split(symbol)
    common = set(first_list).intersection(second_list)
    list_common = list(common)
    list_common.sort()
    return list_common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))