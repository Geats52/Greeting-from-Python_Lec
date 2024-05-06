'''
list_1 = []
list_1 = list()
list_1=[1,2,3,4,5]
print(*list_1)# "*" - убирает квадратные скобки и запятые

# for i in list_1:
#     print(i)

#print(len(list_1)) # len() - считает коллличество элементов
print(list_1[0])#list_1 [] - выводит элемент из списка

'''
# list_1=[1, 5]
# print(list_1)
# list_1.append(8)# .append() - добавляет элемент в список
# print(list_1)

# list_1=[]
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)
'''
#Удаление последнего элемента из списка .pop
list_1 = [12,7,-1,21,0]
print(list_1.pop()) #0
print(list_1)#[12, 7, -1, 21]
print(list_1.pop()) #21
print(list_1)#[12, 7, -1] и т.д.
'''
'''
#Удаление конкретного элемента из списка .pop
list_1 = [12,7,-1,21,0]
print(list_1.pop(0)) #12
print(list_1) [7, -1, 21, 0]
'''
'''
#Добавление элемента в нужную позицию .insert
list_1 = [12,7,-1,21,0]
print(list_1.insert(2,11))# 2 - позиция/индекс, 11 - значение, которое нужно вставить в лист
print(list_1)#[12, 7, 11, -1, 21, 0]
'''

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]
