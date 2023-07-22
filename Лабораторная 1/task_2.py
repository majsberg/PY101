# TODO Найдите количество книг, которое можно разместить на дискете
# Посчитаем размер дискеты в байтах
value_floppy_disk = 1.44
translate_to_bytes = value_floppy_disk * 1024 * 1024

# Посчитаем объем одной книги в байтах
book_value = 4 * 25 * 50 * 100

# Посчитаем количество одинаковых книг, помещающихся на дискету
count_books = round(translate_to_bytes // book_value)
print("Количество книг, помещающихся на дискету:", count_books)
