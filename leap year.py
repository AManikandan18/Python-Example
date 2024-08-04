a=int(input("enter your year: "))
if(a%100==0):
    if(a%400==0):
        print("{} is leap year".format(a))
    else:
        (a,"is not a leap year")
elif(a%4==0):
    print("{} is leap year".format(a))
#elif(a>=0):
    #prin>("{} is not leap year".format(a))
else:
    print("enter a correct year")
