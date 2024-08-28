def add(a,b):
    return a+b

res=add(1,2)
print(res)

def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * facto(x-1)
