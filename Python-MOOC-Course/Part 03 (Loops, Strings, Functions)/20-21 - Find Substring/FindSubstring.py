#Find Substring
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = word.find(character)
if index!=-1 and len(word)>=index+3:
    print(string[index:index+3])

#Find All Substrings
word2 = input("Please type in a word: ")
character2 = input("Please type in a character: ")
 
while True:    
    index2 = word2.find(character)
    if index2!=-1 and len(word2)>=index2+3:
        print(word2[index2:index2+3])
        word2 = word2[index2+1:]
    else: 
        break 