# Задача 5_1 Ввести число n (номер последней строки). Напечатать треугольник Паскаля
n = int(input('Введите число: '))
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
    C = 1
    for j in range(1, i+1):
        print(' ', C, sep='', end='')
        C = C * (i - j) // j
    print()


# Задача 5_2 Ввести число. Напечатать все его делители
numb = int(input("Введите целое число: "))
print("Результат:", end = " ")
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        print(i, end = " ")


# Задача 5_3 Числа Фибоначчи
fib1 = 1 # значения двух первых элементов ряда
fib2 = 1
n = input('Номер элемента ряда Фибоначчи: ')
n = int(n)
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print('Значение этого элемента: ', fib2)
