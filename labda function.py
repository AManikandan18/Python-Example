"""multi=lambda a,b,c:a+b+c
print(multi(5,10,5))

multi=lambda a,b,c:a-b-c
print(multi(20,10,5))

multi=lambda a,b,c:a/b+c
print(multi(10,20,3))

multi=lambda a,b:a+b
print(multi(mani,kandan))

#lambda squreroot:
x=int(input("enter no: "))
print((lambda x:x**0.5)(x))"""

def fun(x,y):
    return lambda z:z+x+y
lamb=fun(5,10)
print(lamb(15))
    
