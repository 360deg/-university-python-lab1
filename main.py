string = 'Словово'
my_dict = {i: string.count(i) for i in string}
print(my_dict)
newString = list(string)
for i in range(len(newString)):
    if i < len(newString)-1:
        newString[i] = newString[i]+newString[i+1]
newString.pop()
my_dict = {i: newString.count(i) for i in newString}
print(my_dict)
