# TODO Найдите количество книг, которое можно разместить на дискете
pages_num = 100
lines_num = 50
symbol_num = 25
symbol_size = 4
disk_size_in_bite = 1.44 * 1024 * 1024
book_num = disk_size_in_bite \
           / (pages_num * lines_num * symbol_num * symbol_size)
print("Количество книг, помещающихся на дискету:", int(book_num))

