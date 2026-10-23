def keyword_cipher(msg, keyword):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = letters.lower()
    keyword = keyword.lower()
    msg = msg.lower()

    # Clearing repeats in the keyword
    key = ""
    for i in keyword: 
        if i in key and i != " ":  key.replace(i, "") 
        else: key = key + i

    print(key)

    # Clearing repeats in the alphabet vs keyword

    for x in letters:
        if x in key: letters.replace(x, "")
        else: key = key + x

    print(key)
    # Creating the ciphered message

    cipher = ""
    for c in msg:
        if c.isalpha():
            index = ((ord(c) - 97) % 26)
            cipher += key[index]
        else:
            cipher += c
    msg = cipher

    return msg

print(keyword_cipher("Welcome home","secret"))
print("wwteilcclojmte dhlojmte") #wticljt dljt
