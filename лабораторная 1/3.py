# Параметры книги
pages_per_book = 100      # количество страниц в книге
lines_per_page = 50       # строки на страницу
symbols_per_line = 25     # символы в строке
bytes_per_symbol = 4      # байтов на один символ

# Расчет размера одной страницы
page_size_bytes = lines_per_page * symbols_per_line * bytes_per_symbol

# Расчет размера одной книги
book_size_bytes = pages_per_book * page_size_bytes

# Размер дискеты в байтах
floppy_disk_size_mb = 1.44        # размер дискеты в мегабайтах
floppy_disk_size_bytes = floppy_disk_size_mb * 1024 * 1024

# Расчет количества книг, помещающихся на дискету
number_of_books = floppy_disk_size_bytes // book_size_bytes

# Вывод результата
print(f"Можно поместить {number_of_books} книг на дискету.")
