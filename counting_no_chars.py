def char_count(a:str):
    freq={}
    for key in a:
        if key in freq.keys():
            freq[key]+=1
        else:
            freq[key]=1
    return list(freq.values())

print(char_count("aaadbbbccc"))