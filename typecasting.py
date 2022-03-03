a = "3456"
a = int(a)
print(type(a))
print(a+5)

# but cannot change everything in typecasting 

b = "a1b2c3"
b = int(b)
print(b+5)

# ValueError: invalid literal for int() with base 10: 'a1b2c3'
