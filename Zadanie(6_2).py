print('---------')
print('Задание 3')
print('---------')


# Функция шифрования по методу XOR
""" letter - сообщение для шифрования 
    keyy - ключ для шифрования """
def xor_cipher(strg, key):
    encript_str = ""
    for letter in strg:
        for keyy in key:
            encript_str += chr(ord(letter) ^ ord(keyy))
            break
    return encript_str


try:
    inp = open('Input1.txt', 'r', encoding='utf-8')
except RuntimeError:
    print('Ошибка чтения файла Input1.txt')

try:
    out = open('Output1.txt', 'w')
except RuntimeError:
    print('Ошибка чтения файла Output1.txt')
    
strg = inp.readline()
key = input('Введите ключ: ')

encr_strg = xor_cipher(strg, key)

try:
    out.write(f'Original: {strg}')
except SyntaxError:
    print('Синтаксическая ошибка')
except RuntimeError:
    print('Ошибка записи Original в файл')

try:
    out.write(f'\nEncode: {encr_strg}')
except SyntaxError:
    print('Синтаксическая ошибка')
except RuntimeError:
    print('Ошибка записи Encode в файл')

try: 
    out.write(f'\nDecode: {xor_cipher(encr_strg, key)}')
except SyntaxError:
    print('Синтаксическая ошибка')
except RuntimeError:
    print('Ошибка записи Decode в файл')
finally:
    inp.close()
    out.close()
    print('Файл Output1.txt был изменён')


