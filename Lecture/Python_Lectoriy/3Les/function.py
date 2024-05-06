# #создадим функцию, которая будет считать сумму всех элементов от 1 до n.
 
# def sum_numbers(n, y = "Hello"):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa # остановка функции
#     print("stop") 

# a=sum_numbers(5, "qwerty")
# print(a) # вызов программы

def sum_str(*args): #"*" - неограниченное количество аргументов
    res = " "
    for i in args:
        res += i
    return res

print(sum_str('q', 'w', 'r'))
print(sum_str('q', 'w', 'r', 'y', '5'))
print(sum_str(str(1))) 