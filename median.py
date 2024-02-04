def median(a): #1,2,3,4,5,6   6/2=3 ==4  -1=3
    sorted_num=sorted(a)
    length=len(a)
    if length%2==0:
        mid_1=sorted_num[length//2]
        mid_2=sorted_num[length//2-1]
        median_val=(mid_1+mid_2)'/2
    else:
        median_val=sorted_num[length//2]

    return median_val

a=[1,3,4,5,8,2]

print(median(a))
