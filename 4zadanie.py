print('введите n:')
n = int(input())
def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + (-0.5) ** (n-1)



print(f'(Введите количество элементов: {n}')
print(f'Количество элементов - {n}, их сумма - {sum(n)}')
