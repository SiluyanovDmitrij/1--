print('Числа Фибоначчи')
print()
print()
fib = lambda n: 0 if n < 1 else 1 if n == 1 else fib(n-1) + fib(n-2)
x = int(input('Введите число: '))
n = 0
while x > fib(n):
    n += 1
if fib(n) == x:
    print('Число является числом Фибоначчи')
else:
    print('Число не является числом Фибоначчи')

    #Мы написали код, который определяет принадлежность числа к числам Фибоначчи.


