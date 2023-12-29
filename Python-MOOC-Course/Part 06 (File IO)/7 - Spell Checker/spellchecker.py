def spellchecker():
    text = input("Write text: ")
    copy_text = text.split()
    with open("wordlist.txt") as new_file:
        file_contents = new_file.read().splitlines()
        for i in range(len(copy_text)):
            if copy_text[i].lower() in file_contents:
                continue
            else:
                text = text.replace(copy_text[i], "*"+copy_text[i]+"*")
    print(text)

spellchecker()

