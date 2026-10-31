def spin_words(sentence):
    s = [ ] 
    for x in sentence.split():
        if len(x) >= 5: 
            s.append("".join(reversed(x)))
        else: 
            s.append(x)
        
    return " ".join(s)

print(spin_words("Hello world"))

#someone elses solution
# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])