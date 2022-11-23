def operation(a=0, b=0):
    try:
        operator = input('Введите арифметический оператор или 0 для выхода: ')
        if operator != '0':
            try:
                a, b = list(map(float, input('Введите два числа ').split()))
            except ValueError:
                print('Числа не распознаны')
            if operator == '+':
                print(f'Сумма чисел {a} и {b} равна {a + b}')
                operation(a, b)
            elif operator == '-':
                print(f'Разность чисел {a} и {b} равна {a - b}')
                operation(a, b)
            elif operator == '*':
                print(f'Произведение чисел {a} и {b} равно {a * b}')
                operation(a, b)
            elif operator == '/':
                if b != 0:
                    print(f'Частное от деления чисел {a} и {b} равно {a / b}')
                    operation(a, b)
                else:
                    print('На ноль делить нельзя ')
                    operation(a, b)
            else:
                print('Оператор не распознан, попробуйте еще раз')
                operation(a, b)
        else:
            print('Завершение работы')
    except ValueError:
        print('Введите +, -, * или /')
        operation(a, b)


operation()
