
def my_sum(n):
    if n == 1:
        return 1
    else:
        return my_sum(n-1) + n

n= int(input())
    
if n > 0:
    if my_sum(n) != n*(n+1)/2:
        (print('выражения неравны'))
    else:
        (print('равны'))
            







           
        

