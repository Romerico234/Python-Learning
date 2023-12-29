from string import ascii_letters, punctuation
 
def separate_characters(my_string: str):
    letters = ""
    special_characters = ""
    other_characters = ""
 
    for character in my_string:
        if character in ascii_letters:
            letters += character
        elif character in punctuation:
            special_characters += character
        else:
            other_characters += character
 
    return (letters, special_characters, other_characters)