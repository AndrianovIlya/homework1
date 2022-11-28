import random
T = 'y'
while T == 'y' or T == 'Y':
    print('1. Задача 1.')
    print('1. Задача 2.')
    print('1. Задача 3.')
    print('1. Задача 4.')
    n = int(input('Введите номер задачи: '))
    if n == 1:
        k = 'y'
        print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
        while k == 'y' or k == 'Y':

            num1, num2 = input('Введите число:').split('.')
            summa1 = 0
            summa2 = 0
            num1 = int(num1)
            num2 = int(num2)
            while num1 != 0:
                digit = num1 % 10
                summa1 += digit
                num1 = num1 // 10
            while num2 != 0:
                digit = num2 % 10
                summa2 += digit
                num2 = num2 // 10
            print(f'Сумма цифр равна: {int(summa1 + summa2)}')
            k = input('Нажмите y или Y? чтобы повторить: ')
        T = input('Вернуться в меню? У или у: ')
    elif n == 2:
        print('Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.')
        k = 'y'
        while k == 'y' or k == 'Y':
            n = int(input('Введите длину последовательности: '))
            my_list = []
            summa = 0
            for i in range(1, n + 1):
                k = float((1 + 1 / i) ** i)
                summa += k
                my_list.append(format(k,',.2f'))
            print(f'Ваш список выглядит так:\n{my_list}\nСумма чисел в списке равна:')
            print(format(summa, ',.2f'))
            k = input('Нажмите y или Y? чтобы повторить: ')
        T = input('Вернуться в меню? У или у: ')

    elif n==3:
        print('Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод')
        k = 'y'
        while k == 'y' or k == 'Y':
            my_list = input('Введите числа через пробел:').split()
            print(f'Изначальный список выглядит так: \n{my_list}')

            new_list = []
            final_list = []

            while len(new_list) < len(my_list):
                k = random.randint(0, len(my_list) - 1)
                if k not in new_list:
                    new_list.append(k)

            for i in new_list:
                final_list.append(my_list[i])
            print(f'Перемешанный список выглядит так:\n{final_list}')
            k = input('Нажмите y или Y? чтобы повторить: ')
        T = input('Вернуться в меню? У или у: ')
