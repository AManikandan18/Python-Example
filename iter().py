list_01=["hello","brother","greet","stefan"]
iter_01=iter(list_01)
print(next(iter_01))
print(next(iter_01))
print(iter_01.__next__())
print(iter_01.__next__())

#or called index slice:
print(next(iter(list_01)))
print(next(iter(list_01[1:2])))
print(next(iter(list_01[2:3])))
print(next(iter(list_01[3:4])))

#or index
print(list_01[0])
print(list_01[1])
print(list_01[2])
print(list_01[3])
