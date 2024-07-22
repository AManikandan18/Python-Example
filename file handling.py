##q=input("enter your value: ")
##e=open("filehabdle.txt","x")
##e.write(q)
##e.close()
##a=open("filehabdle.txt","r")
##print(a.read())


##import random
##for _ in range(100):
##    n=random.randint(9000000000,9999999999)
##    
##e=open("fi.txt","x")
##e.write(n)
##e.close()
##a=open("fi.txt","r")
##print(a.read())

##import random
##e=open("allllllll.txt","x")
##for _ in range(100):
##    n=random.randint(9000000000,9999999999)
##    e.write(str(n)+"\n")
##    
##e.close()
####a=open("hi.txt","r")
####print(a.read())

import requests
x=requests.post("https://www.w3schools.com")
print(x.text)
