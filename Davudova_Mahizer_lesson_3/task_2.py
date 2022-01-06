'''
*(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv(): 
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже 
должен быть с заглавной.
'''

def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    number = {'one': 'один', 'two': 'два','three': 'три','four': 'четыре','five': 'пять',
            'six': 'шесть','seven': 'семь','eight': 'восемь','nine': 'девять'}
    str_out = ''

    for i in number.keys():
        if i == value:
           str_out = number[i]
        elif i.title() == value:
            str_out = number[i].title()

    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("eight"))