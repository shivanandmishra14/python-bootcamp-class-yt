a = {1,2,3,5}
print(a)
print(type(a))

# suppose there two numbers which repates 
a = {1,2,3,5,2}
print(a)


# Empty set
b = set()
print(type(b))
b.add(4)
b.add(5)
b.add(5)   
print(b)                                     


# b.add([4,7,6,])   list cannot be keep inside set 
b.add((4,7,6,))   #tuple 
print(b)   

b.add({4:5})
print(b)   
