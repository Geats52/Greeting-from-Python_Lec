data = "15 156 96 3 5 8 52 5"
print(data)

# data = data.split()#преобразование в список
# print(data)

data = list(map(int, data.split()))#преобразование строк в числа
print(data)