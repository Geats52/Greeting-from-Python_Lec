'''
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')# .remove - удаляет из множества какое-либо значение
print(colors) # {'green', 'blue','gray'}
#colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok --.discard - проверяет есть ли это значение в этом множестве
print(colors) # {'green', 'blue','gray'}
colors.clear() # { } # - удаление всех элементов множества
print(colors) # set()

#set() - позволяет создавать множество
#q = set()
'''
'''
#Операции со множествами в Python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} #  с=а.copy() - копирует элементы множества "a" в пременную "c"
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} # a.union(b) - объединяет множества "a" и "b"
i = a.intersection(b) # i = {8, 2, 5} # (пересечение) a.intersection(b) - находит элементы, которые есть в "a" и "b"
dl = a.difference(b) # dl = {1, 3}      # (различия) a.difference(b) - показывает какие элементы есть в "a", но отсутствуют в "b"
dr = b.difference(a) # dr = {13, 21}    # наоборот показывает какие элементы есть в "b", но отсутствуют в "a"
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} # Cлед. порядок:intersection, далее union, затем difference
'''


# a={1,8,6}
# b=frozenset(a) # - неизменное множество, тбе его нельзя изменять
# print(b)

a = {1, 2, 3}
b = {3, 4, 5}


q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} # Cлед. порядок:intersection, далее union, затем difference
print(q)