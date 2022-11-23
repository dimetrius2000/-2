def ascii_code(i=31, k=0):
    if i < 127:
        k += 1
        i += 1
        if k % 10 == 1:
            return f'\n {str(i)} - {chr(i)} {ascii_code(i, k)}'
        else:
            return f'{str(i)} - {chr(i)} {ascii_code(i,k)}'



        
print(ascii_code())
