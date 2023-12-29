#A Framed Word

word = input("Word: ")
 
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)
 
input_string = "presumptious"


