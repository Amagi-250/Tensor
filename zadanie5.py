import re

print('---------')
print('Задание 1')
print('---------')

try:
    password = input('Введите пароль: ')
except NameError:
    print('Не найдено переменной с таким именем!')
except TimeoutError:
    print('Закончилось время ожидания!')
except TypeError:
    print('Объект не соответствующего типа!')
except ValueError:
    print('Правильный тип, но не корректное значение!')
finally:
    pass


""" Функция проверки пароля на количество символов большее или равно 6 """
def symbols(password):
    if len(password) >= 6:
        return True


""" Функция проверки на то, что пароль содержит хотя бы одну цифру """
def num(password):
    if re.search(r'\d', password):
        return True


""" Функция проверки на то, что пароль содержит символы и верхнего и нижного регистров """
def reg(password):
    if not (password.upper() == password or password.lower() == password):
        return True


"""" Функция проверки на то, что пароль не состоит только из цифр """ 
def numbers(password):
    if not password.isdecimal():
        return True


""" Функция окончательной проверки на соответствия пароля всем условиям """
def pwd(password):
    if symbols(password) 
        and num(password) 
        and reg(password) 
        and numbers(password):
        print('--------------------------------------------')
        print('Пароль удовлетворяет всем условиям проверки!')
    else:
        print('-----------------------------------------------')
        print('Пароль не удовлетворяет всем условиям проверки!')


pwd(password)

print('\n---------')
print('Задание 2')
print('---------')

""" Функция для принятия любого количества переменных"""
def znach(*num):

    sum = 0
    for n in num:
        sum += n
    print("Сумма =", sum)

znach(0)
znach(1, 2)
znach(1, 2, 3)
znach(1, 2, 3, 4)
znach(1, 2, 3, 4, 5)

print('\n---------')
print('Задание 3')
print('---------')


# Рекурсивная функция возвращающая заданное число Фибоначчи
def fibonacci(n):
    """ Числа 1 и 2, это соответственно первый 
        и второй элементы ряда Фибоначчи """
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


el = int(input("Введите индекс элемента ряда Фибоначчи: "))
print(f"Число Фибоначчи под индексом {el} равно: {fibonacci(el)}")
