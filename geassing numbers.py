import random
a=random.randint(0,9)
b=int(input("enter your geassing nu: "))
if(a==b):
    print("your guessing is correct")
    print("good guess")
elif(a<b):
    print("your guessing is high")
    print(b,"greater than",a)
elif(a>b):
    print("your guessing is lower")
    print(b,"lower than",a)
print("the random number is",a)
