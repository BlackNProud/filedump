from random import randint

# Initialize.
strings = []
length = int(input("How long do you want your strings to be? "))


# First string - the first and last digit should be a number from 1 to 9, and every other digit should be from 0 to 9.
temp = str(randint(1, 9))
for i in range(length-2):
    temp += str(randint(0, 9))
temp += str(randint(1, 9))

# Add to the list and print..
strings.append(temp)
print(temp)

print()

# Second string - every digit until the last digit should be 9 minus the original string's digit, and the last digit should be 10 minus it.
temp = ""
for i in range(length-1):
    temp += str(9-int(strings[0][len(temp)]))
temp += str(10-int(strings[0][len(temp)]))
print(temp)
