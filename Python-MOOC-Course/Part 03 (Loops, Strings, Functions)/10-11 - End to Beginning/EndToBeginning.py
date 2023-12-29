#End to Beginning

word = input("Please type in a string:")
length = -1
while length >= -len(word):
    print(word[length])
    length -= 1


#Beginning to End

phrase = input("Please type in a string: ")
count = len(phrase) - 1
while count >= 0:
    print(phrase[count:])
    count -= 1

