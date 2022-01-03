'''
Реализовать склонение слова процент во фразе N процентов. 
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''


def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    # место для Вашего кода
    result = ''
    if number % 10 == 1 and number != 11:
        result = f'{number} процент'
    elif (21 < number or number < 5) and (number % 10 == 2 or number % 10 == 3 or number % 10 == 4):
        result = f'{number} процента'
    else:
        result = f'{number} процентов'

    return result


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))