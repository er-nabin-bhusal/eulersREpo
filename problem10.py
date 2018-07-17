def prime_number(num):
    ''' prime num generator '''
    sums = 2
    j = 0
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        if j == i-1:
            sums = sums+i 
    return sums