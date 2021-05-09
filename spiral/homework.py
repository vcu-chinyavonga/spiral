def spiralize(number):
    n = 1 
    count = 0 
    gap = 2
    return_value = 0

    while n <= number ** 2:
        return_value += n
        n += gap
        count += 1
        if count == 4:
            gap = 2
            count = 0
    
    return return_value
