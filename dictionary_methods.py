mydict = {
    "name": "shivanand",
    "age": 30,
    "marks": [5, 67, 89],
    "anotherdict": {"name": "shivanand"},
    1:2
}
print(mydict.items())
print(list(mydict.items()))

print(mydict.keys())
print(list(mydict.keys()))

print(mydict.values())
print(list(mydict.values()))

newAge = {
    "age": 36,
}
mydict.update(newAge)
print(mydict)


print(mydict.get("age"))
print(mydict.get("name"))
print(mydict.get("marks"))
print(mydict.get("anotherdict"))
print(mydict.get(1))


