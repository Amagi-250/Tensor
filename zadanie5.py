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


#Функция проверки пароля на количество символов большее или равно 6
def symbols(password):
    if len(password) >= 6:
        return True


#Функция проверки на то, что пароль содержит хотя бы одну цифру
def num(password):
    if re.search(r'\d', password):
        return True


#Функция проверки на то, что пароль содержит символы и верхнего и нижного регистров
def reg(password):
    if not (password.upper() == password or password.lower() == password):
        return True


#Функция проверки на то, что пароль не состоит только из цифр
def numbers(password):
    if not password.isdecimal():
        return True


#Функция окончательной проверки на соответствия пароля всем условиям
def pwd(password):
    if symbols(password) and num(password) and reg(password) and numbers(password) == True:
        print('--------------------------------------------')
        print('Пароль удовлетворяет всем условиям проверки!')
    else:
        print('-----------------------------------------------')
        print('Пароль не удовлетворяет всем условиям проверки!')


pwd(password)

print('---------')
print('Задание 2')
print('---------')


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

print('---------')
print('Задание 3')
print('---------')

fib1 = fib2 = 1

try:
    n = int(input("Задайте колличество чисел в ряду Фибоначчи: "))
except NameError:
    print("Не найдено переменной с таким именем")
except TypeError:
    print("Применение к объекту несоответствующего типа")
except RuntimeError:
    print("Исключение")
finally:
    pass

print("Ряд Фибоначчи:")
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

fib1 = fib2 = 1

n = int(input("\nВведите номер элемента ряда Фибоначчи: "))
n = int(n) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print("Значение этого элемента:", fib2)
