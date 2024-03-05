def pair_sum(list,target):
    pair=[]
    seen=set()
    for num in list:
        compliment=target-num
        if compliment in seen:
            pair.append((num,compliment))
        seen.add(num)
    return pair

my_list=[1,2,3,4,5,5,6,7,8]
target=6

result=pair_sum(my_list,target)
print(result)