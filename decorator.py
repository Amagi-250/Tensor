import time
import math
import logging


'''Декоратор для вывода времени выполнения функции'''
def time_of_function(func_):
    def wrapper(*args):
        start_time = time.perf_counter_ns()
        res = func_(*args)
        print(f"Время выполнения функции: {time.perf_counter_ns() - start_time} мс")
        return print(f"Корни(корень) уравнения равны(ен): {res}")
    return wrapper


'''Декоратор для записи логов'''
def logging_(func_):
    def wrapper(*args):
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info(func_(*args))
        return func_(*args)
    return wrapper


'''Декоратор для замедления выполнения кода и ограничение частоты вызова функции'''
def frequency(func_):
    def wrapper(*args):
        time_ = 0
        if time_ < 3:
            time.sleep(2)
            time_ += 1
            return func_(*args)
    return wrapper


'''Функция расчёта квадратного уравнения с комплексными числами'''
@time_of_function
@logging_
@frequency
def func(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = complex(b, math.sqrt(abs(D))) / (2 * a)
        x2 = complex(b, -math.sqrt(abs(D))) / (2 * a)
        return x1, x2


'''Вызов функции с разными значениями'''
func(1, 4, 3)
func(5, 10, 5)
func(4, 2, 10)
