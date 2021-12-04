
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
    print('Файл Output1.txt был изменён')


