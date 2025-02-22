
def sumar(a,b,c=0,d=0):
    if c!= 0 and d!=0 :
        return a+b+c+d
    if c!= 0 and d==0:
        return a+b+c
    if d!=0 and c==0:
        return a+b+d
    else:
        return a+b
print(sumar(1,2,3,4,5))
