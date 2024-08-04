#basic function:
def hi():
    print("hello world")
hi()    

#argument:
def hi(lname):
    print("hello",lname)
hi("mani")    

#keyword argument:
def hi(fname,lname):
    print("hello",fname,lname)
hi(fname="mani",lname="kandan")

#multiple argument:
def hi(fname,lname):
    print("hello",fname,lname)
hi("mani","kandan")    

#arbitrary argument:
def hi(*friends):
    print("hello",friends[2])
hi("mani","sasi","arul")

#arbitrary keyword argument: 
def hi(**great):
    print("hello",great["key2"])
hi(key1="arul",key2="jeeva",key3="asfak")

#default parameter value:
def hi(tname="crow"):
    print(tname)
hi("hen")
hi("dove")
hi("duck")
hi()

def func_ret(x):
    return x**x
print(func_ret(10))
