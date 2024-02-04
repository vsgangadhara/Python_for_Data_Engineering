def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

def fact2(n):
    if n==0 or n==1:
        return 1
    else:
        result=1
        for i in range(2,n+1):
            result =result*i
        return result

#print(fact(5))

print(fact2(5))