import math
print('Калькулятор')
print()
print ('Доступные функции для вычисления: "сложение", "вычитание", "умножение", "деление", "степень", "логарифм", "округление "+"", "округление "-"".')
print ()
x = input('Введите функцию: ')
while x not in ('сложение','вычитание','умножение','деление','степень','логарифм','округление "+"','округление "-"'):
    x = input('Функции не существует, введите функцию из списка: "сложение", "вычитание", "умножение", "деление", "степень", "логарифм", "округление "+"", "округление "-"" ')

if x == ('сложение'):
    a = input('Введите первый элемент: ')
    while a.isdigit() == False:
        a = input('Введенный элемент не является числом, введите первый элемент: ')
    a = int(a)
    b = input('Введите второй элемент: ')
    while b.isdigit() == False:
        b = input('Введенный элемент не является числом, введите второй элемент: ')
    b = int(b)
    print('Ответ:', a+b)

if x == ('вычитание'):
    a = input('Введите первый элемент: ')
    while a.isdigit() == False:
        a = input('Введенный элемент не является числом, введите первый элемент: ')
    a = int(a)
    b = input('Введите второй элемент: ')
    while b.isdigit() == False:
        b = input('Введенный элемент не является числом, введите второй элемент: ')
    b = int(b)
    print('Ответ:', a-b)

if x == ('умножение'):
    a = input('Введите первый элемент: ')
    while a.isdigit() == False:
        a = input('Введенный элемент не является числом, введите первый элемент: ')
    a = int(a)
    b = input('Введите второй элемент: ')
    while b.isdigit() == False:
        b = input('Введенный элемент не является числом, введите второй элемент: ')
    b = int(b)
    print('Ответ:', a*b)

if x == ('деление'):
    a = input('Введите первый элемент: ')
    while a.isdigit() == False:
        a = input('Введенный элемент не является числом, введите первый элемент: ')
    a = int(a)
    b = input('Введите второй элемент: ')
    while b.isdigit() == False:
        b = input('Введенный элемент не является числом, введите второй элемент: ')
    b = int(b)
    print('Ответ:', a/b)

if x == 'округление "+"':
    a = float(input('Введите число: '))
    a = float(a)
    print ('Ответ:', math.ceil(a))

if x == 'округление "-"':
    a = float(input('Введите число: '))
    a = float(a)
    print ('Ответ:', math.floor(a))

if x == 'логарифм':
    a = input('Введите первый элемент: ')
    while a.isdigit() == False:
        a = input('Введенный элемент не является числом, введите первый элемент: ')
    a = int(a)
    b = input('Введите второй элемент: ')
    while b.isdigit() == False:
        b = input('Введенный элемент не является числом, введите второй элемент: ')
    b = int(b)
    print('Ответ: ', math.log(a,b))

if x == 'степень':
    a = input('Введите первый элемент: ')
    while a.isdigit() == False:
        a = input('Введенный элемент не является числом, введите первый элемент: ')
    a = int(a)
    b = input('Введите второй элемент: ')
    while b.isdigit() == False:
        b = input('Введенный элемент не является числом, введите второй элемент: ')
    b = int(b)
    print('Ответ: ', a**b)

    #Мы написали код, который частично выполняет функции калькулятора.
    #Он вычисляет сумму, разность, произведение, частное, число, возведённое в степень, логарифм числа.
    #Округляет десятичную дробь в большую или меньшую сторону.
    #Оповещает потенциального пользователя об ошибках.

