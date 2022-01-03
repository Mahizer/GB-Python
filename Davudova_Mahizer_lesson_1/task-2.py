'''
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`. 
Внимание: использовать только арифметические операции!
b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых 
делится нацело на 7.
*c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо создайте доп. функцию, либо
перепишите существующую sum_list_2)
ВНИМАНИЕ! Используйте стартовый код для своей реализации:
'''


def sum_list_1(dataset: list) -> int:
    new_list = []
    num_sum = 0
    for i in dataset:
        for j in list(str(i)):
            num_sum += int(j)
        if num_sum % 7 == 0:
            new_list.append(i)
    return sum(new_list)



def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
        сумма цифр которых делится нацело на 7"""
    new_list = []
    for i in dataset:
        num_sum = 0
        i += 17
        for j in list(str(i)):
            num_sum += int(j)
        if num_sum % 7 == 0:
            new_list.append(i - 17)
    return  sum(new_list)


def sum_list_3(dataset: list) -> int:
    for inx, el in enumerate(dataset):
        num_sum = 0
        el += 17
        for j in list(str(el)):
            num_sum += int(j)
        if num_sum % 7 != 0:
            dataset[inx] = 0
    return sum(dataset)


my_list = [i ** 3 for i in range(1, 1000, 2)]
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)