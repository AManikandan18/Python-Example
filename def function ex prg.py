print("Enter any one: \n","1","2","3","4")
x=int(input("enter the value: "))
a=int(input("enter the first number: "))
b=int(input("enter second number: "))
if(x==1):
    def add_fun(a,b):
        c=a+b
        print(c)
        add_fun(a,b)
elif(x==2):
    def sub():
        c=a-b
        print(c)
sub()
def mul_fun():
    c=a*b
    print(c)
mul_fun()
def div_fun():
    c=a%b
    print(c)
div_fun()    
