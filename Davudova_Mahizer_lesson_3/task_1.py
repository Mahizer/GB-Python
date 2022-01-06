'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:

$ num_translate("one")
"один"
$ num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, 
в теле функции или снаружи.
'''

def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    number = {'one': 'один', 'two': 'два','three': 'три','four': 'четыре','five': 'пять',
            'six': 'шесть','seven': 'семь','eight': 'восемь','nine': 'девять'}
    str_out = ''

    for i in number.keys():
        if i == value:
           str_out = number[i]
    return str_out


print(num_translate("one"))
print(num_translate("eight"))