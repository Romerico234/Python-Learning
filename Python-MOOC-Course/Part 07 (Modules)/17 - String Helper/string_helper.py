from string import ascii_letters, digits
 
def change_case(orig_string: str):
    new_string = ""
    for character in orig_string:
        if character.isupper():
            new_string += character.lower()
        elif character.islower():
            new_string += character.upper()
        else:
            new_string += character
 
    return new_string
 
def split_in_half(orig_string: str):
    return orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:]
 
def remove_special_characters(orig_string: str):
    allowed = ascii_letters + digits + ' '
    new_string = ""
    for character in orig_string:
        if character in allowed:
            new_string += character
 
    return new_string