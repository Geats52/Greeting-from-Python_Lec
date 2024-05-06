# import modul1 # импортирование с другого файла

# print(modul1.max1(5, 9)) # вызов функции из другого файлика

# from modul1 import * # "*" - импортирование всех функций

# print(max1(10, 9)) 

import modul1 as m1 # as - переменование функции, м1 - другое имя

print(m1.max1(10, 9))