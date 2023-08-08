# TODO Напишите функцию для поиска индекса товара
def search_items(list_of_items, item):
    for fruit in list_of_items:
        try:
            return list_of_items.index(item)
        except ValueError:
            return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_items(items_list, find_item)  # TODO Вызовите функцию, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
