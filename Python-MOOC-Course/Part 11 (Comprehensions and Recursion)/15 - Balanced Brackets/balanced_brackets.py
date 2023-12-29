def balanced_brackets(my_string: str):
    # string is empty, so it is ok
    if len(my_string) == 0:
        return True
 
    # if first character is not any bracket, let's eat it away
    if not my_string[0] in "()[]":
        return balanced_brackets(my_string[1:])
 
    # if last is not any bracket, let's eat it away
    if not my_string[-1] in "()[]":
        return balanced_brackets(my_string[:-1])
    
    # now is known that first and last characters are brackets
    # check if they are a pair
    if my_string[0]=="(" and my_string[-1]==")":
        return balanced_brackets(my_string[1:-1])
    if my_string[0]=="[" and my_string[-1]=="]":
        return balanced_brackets(my_string[1:-1])
 
    # were not, so this string is not ok
    return False
 
 
    # remove first and last character


if __name__ == "__main__":
    ok = balanced_brackets("(((())))")
    print(ok)

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)