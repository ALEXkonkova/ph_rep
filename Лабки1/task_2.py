# TODO Найдите количество книг, которое можно разместить на дискете

value = 1.44 * 1024 * 1024
count_let = 100
count_str = 50
count_sym = 25

syms = count_sym * count_str * count_let * 4

print("Количество книг, помещающихся на дискету:", int(value//syms))
