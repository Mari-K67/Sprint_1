def digital_root(num):
    while num > 9:
        sum_num = 0 
        while num > 0:
            last_num = num % 10
            sum_num += last_num
            num = num // 10
        num = sum_num
    return num 

print(digital_root(4851))