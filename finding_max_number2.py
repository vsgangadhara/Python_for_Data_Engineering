def max_num(list1):
    max=0
    for number in list1:
        if number>max:
            max=number
    return max

a=[10,20,30,60,10,30,40]
print(max_num(a))