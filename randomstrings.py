from random import randint

strings = []
length = int(input("How long do you want your strings to be? "))

temp = str(randint(1, 9))
for i in range(length-2):
    temp += str(randint(0, 9))
temp += str(randint(1, 9))

strings.append(temp)
print(temp)

print()

temp = ""
for i in range(length-1):
    temp += str(9-int(strings[0][len(temp)]))
temp += str(10-int(strings[0][len(temp)]))
print(temp)
