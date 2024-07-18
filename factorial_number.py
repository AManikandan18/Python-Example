#for:
a=int(input("enter a number for factorial: "))
fact=1
##if a==0 or a<0:
##    print("enter the value is should be geater than 0")
    
for i in range(1,a+1):
    fact=fact*i
print("the give number",a,"in factorial number is",fact)



#while:
a=int(input("enter a number for factorial: "))
if a==0 or a<0:
    print("enter the value is should be geater than 0")
else:
    fact=1
    while(1<a):
        fact=fact*a
        a=a-1
    print("the give number",a,"in factorial number is",fact)
