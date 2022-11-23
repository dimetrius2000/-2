def flip_number(a):
    if len(a) == 1:
        return a
        
    else: 
        n = str(int(a) % 10)
        a = str(int(a) // 10)
        if n == '0':
            return n +flip_number(a)
        else:
            return flip_number(n) + a


a = (input('Введите число: '))
print(flip_number(a))    







       
        

    
    
