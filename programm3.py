import math
print('\n---------')
print('Задание 1')
print('---------')
x = 0
y = 0
vp = int(input('Введите количество шагов вперёд: '))
nz = int(input('Введите количество шагов назад: '))
vr = int(input('Введите количество шагов вправо: '))
vl = int(input('Введите количество шагов влево: '))
x = x + vr - vl
y = y + vp - nz
print(f'Вы находитесь на координатах: ({x},{y})')
print('Программа завершена!')

print('\n---------')
print('Задание 2')
print('---------')
f = 1
x = 0
y = 0
while True:
    if f == 1:
        vp = int(input('Введите количество шагов вперёд: '))
        nz = int(input('Введите количество шагов назад: '))
        vr = int(input('Введите количество шагов вправо: '))
        vl = int(input('Введите количество шагов влево: '))
        x = x + vr - vl
        y = y + vp - nz
        print(f'Вы находитесь на координатах: ({x},{y})')
        print('------------------------------------------------------------------------------')
        f = int(input('Для продолжения перемещния нажмите - 1, для выхода из программы нажмите - 0: '))
        print('------------------------------------------------------------------------------')
    else:
        print('Программа завершена!')
        break

print('\n-------------')
print('Задание 3 и 4')
print('-------------')
a = int(input('Введите коэффициент a: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))
print (f'Ваше уравнение: ({a})x^2 + ({b})x + ({c}) = 0')
D = b**2 - 4 * a * c
t = math.sqrt(abs(D) / 2 / a)
r1 = r2 = -b / 2 * a
print(f'Дискриминант: {D}')
if (D > 0):
    x1 = ((-(b) + math.sqrt(D))) / (2 * a)
    x2 = ((-(b) - math.sqrt(D))) / (2 * a)
    print('------------')
    print(f'Корни равны: \nx1 = {x1}' + '\n'+ f'x2 = {x2}')
elif (D == 0):
    x = -(b) / (2 * a)
    print('-----------------------------------')
    print(f'Единственный корень равен: x = {x}')
else:
    com1 = com2 = int(t)
    print('-------------')
    print(f'Корни равны: \nx1 = {r1} + {com1}i\nx2 = {r2} - {com2}i')


