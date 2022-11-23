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


num = int(input("Enter the number: ")) 
revr_num = 0    # initial value is 0. It will hold the reversed number 
def recur_reverse(num): 
    global revr_num   # We can use it out of the function 
    if (num > 0): 
        Reminder = num % 10 
        revr_num = (revr_num * 10) + Reminder 
        recur_reverse(num // 10) 
    return revr_num 
 
 
revr_num = recur_reverse(num) 
print("n Reverse of entered number is = %d" % revr_num) 




       
        

    
    
