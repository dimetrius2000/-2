
def determine(a,count_1=0,count_2=0):
    if a !=0:
        if (a % 10) % 2 == 0:
            count_1 +=1
        else:
            count_2 +=1
        return determine(a // 10,count_1,count_2)

    print(f'Количество четных и нечетных цифр в числе равно: ({count_1}, {count_2})')

a = int(input('Введите число: '))
determine(a)



