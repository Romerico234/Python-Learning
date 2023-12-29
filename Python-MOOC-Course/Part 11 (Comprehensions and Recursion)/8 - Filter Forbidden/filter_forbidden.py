def filter_forbidden(string: str, forbidden: str):
    new_string = "".join([character for character in string if character not in forbidden])
    return new_string

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)