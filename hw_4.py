# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# from random import randint
# first = [randint(1,10) for _ in range(int(input('Кол-во элементов первого списка: ')))]
# second = [randint(1,10) for _ in range(int(input('Кол-во элементов второго списка: ')))]
# a = list(set.intersection(set(first), set(second)))
# a.sort()
# print(first)
# print(second)
# print(*a)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# bushes = [randint(5,10) for _ in range(15)]
# print(bushes)
# last = len(bushes)-1
# bushes = dict(enumerate(bushes))
# total = 0
# N = int(input('Введите номер куста: '))
# if N > last:
#     print('Куста под этим номером нет!')
# elif N == last:
#     total = bushes[N]+bushes[N-1]+bushes[0]
# elif N == 0:
#     total = bushes[N]+bushes[last]+bushes[N+1]
# else: total = bushes[N]+bushes[N-1]+bushes[N+1]

# print(bushes)
# print(total)

# задача RLE необязательная. Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
# например декодирование

# my_str ='aaaaasssdddffgghh' 
# def RLE_encoding(my_str):
#     working_list = []
#     working_list.extend(my_str)    
#     result_list = []
#     i = 0
#     while i < len(working_list):
#         count = 1
#         while i+1 < len(working_list) and working_list[i] == working_list[i+1]:
#             count += 1
#             i +=1
#         result_list.append(working_list[i] + str(count))
#         i +=1
#     return result_list

# result = ''.join(RLE_encoding(my_str))
# print(result)

# def RLE_decoding(my_str):
#     result_str = ''       
#     for i in range(len(my_str)):
#         if my_str[i].isdigit():
#             result_str += my_str[i-1] * int(my_str[i])
#     return result_str

# print(RLE_decoding(result))    