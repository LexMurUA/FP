# Завдання 5
# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.
import math

#1
# my_list = [1,2,4,45,6,56,4,76,76,453,46,4534,3,5,7]

# def quadro(list):
#     return [i**2 for i in list if i % 2 != 0]
# print(quadro(my_list))  

            
#2           
My_list = [1, 2, 4, 45, 6, 56, 4, 76, 76, 453, 46, 4534, 3, 5, 7]

def k(my_list):
    odd_numbers = []
    for num in my_list:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

def l(my_list):
    return list(map(lambda x: x**2, my_list))

my_list = k(My_list)
result = l(my_list)
print(result)
