# TODO Найдите количество книг, которое можно разместить на дискете
size_mb = 1.44
pages= 100
lines= 50
symbols= 25
bytes_for_symbol= 4
size_bytes=size_mb*1024*1024
book=pages*lines*symbols*bytes_for_symbol
a=size_bytes/book

print("Количество книг, помещающихся на дискету:", round(a))
