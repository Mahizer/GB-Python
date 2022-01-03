'''
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
* до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

'''


def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    seconds = duration % 60
    minutes = duration // 60
    hours = minutes // 60
    days = hours // 24
    if duration < 60:
        result = f'{seconds} сек'
    elif duration >= 60 and duration < 3600:
        result = f'{minutes} мин {seconds} сек'
    elif duration >= 3600 and duration < 86400:
        result = f'{hours} час {minutes - (hours * 60)} мин {seconds} сек'
    else:
        result = f'{days} д {hours - (days * 24)} час {minutes - (hours * 60)} мин {seconds} сек'

    return result


duration = 3601
result = convert_time(duration)
print(result)