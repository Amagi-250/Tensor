print('---------')
print('Задание 1')
print('---------')

str1 = 'Привет'
str2 = 'это'
str3 = 'программа'

try:
    str_ = str1 + ', ' + str2 + ', ' + str3

    def encode(str):
        return str.encode('utf-8')

    def decode(str):
        return str.decode('utf-8')

    enc = encode(str_)
    print('Список байт кодов: ', enc)

    dec = decode(enc)
    print('Список строк: ', dec)

except Exception:
    print('Ошибка преобразования')
except ArithmeticError:
    print('Арифметическая ошибка')

finally:
    pass

print('\n---------')
print('Задание 2')
print('---------')

input = open('Input.txt', 'r')
output = open('Output.txt', 'w')

try:
    '''Обращение к первому элементу в файле, взятие значения для молекулы C'''
    C = int(input.read(1))
    '''Обращение к второму элементу в файле, взятие значения молекулы H'''
    H = int(input.read(2))
    '''Обращение к третьему элементу в файле, взятие значения молекулы O'''
    O = int(input.read(3))
    '''Расчёт числа молекул в формуле спирта'''
    rezult = C*2+H*6+O
    output.write(f'The maximum possible number of alcohol molecules: {str(rezult)}')

except ZeroDivisionError:
    print('Была произведена попытка деления на ноль')
except Exception:
    print('Ошибка взятия чисел из файла')
except EOFError:
    print('Функция наткнулась на конец файла и не смогла прочитать то, что хотела')
except SyntaxError:
    print('Синтаксическая ошибка')
except RuntimeError:
    print('Неизвестная ошибка')

finally:
    input.close()
    output.close()
    print('Файл Output.txt был изменён')

print('\n---------')
print('Задание 3')
print('---------')

def xor_cipher(strg, key):
    encript_str = ""
    for letter in strg:
        for keyy in key:
            encript_str += chr(ord(letter) ^ ord(keyy))
            break
    return encript_str

inp = open('Input1.txt', 'r', encoding='utf-8')
out = open('Output1.txt', 'w')

try:
    strg = inp.readline()
    key = input('Введите ключ: ')

    encr_strg = xor_cipher(strg, key)

    out.write(f'Original: {strg}')
    out.write(f'\nEncode: {encr_strg}')
    out.write(f'\nDecode: {xor_cipher(encr_strg, key)}')

except ArithmeticError:
    print('Арифметическая ошибка')
except EOFError:
    print('Функция наткнулась на конец файла и не смогла прочитать то, что хотела')
except SyntaxError:
    print('Синтаксическая ошибка')
except RuntimeError:
    print('Неизвестная ошибка')

finally:
    inp.close()
    out.close()
    print('Файл Output.txt был изменён')