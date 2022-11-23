import random

def guess_num(n=0, a=random.randint(0, 100), i=10):
    if n != a and i > 0:
        n = int(input('Введите число: '))
        i -= 1
        if n > a:
            print(f'Загаданное число меньше, осталось {i} попыток')
        elif n < a:
            print(f'Загаданное число больше, осталось {i} попыток')
        return guess_num(n, a, i)
    elif n == a:
        return 'Вы угадали!'
    else:
        return f'Ваши попытки исчерпаны. Загаданное число: {a}'


print(guess_num())
