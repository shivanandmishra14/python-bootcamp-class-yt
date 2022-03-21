from turtle import pos


letter = ''' dear post,
I am unable to come to office today. 
Due to N reason
regards
yours
name'''

post = input("post name")
reason = input("reason")
name = input("Name of the employee")
letter = letter.replace("post", post)
letter = letter.replace("N",reason)
letter = letter.replace("name", name)
print(letter)