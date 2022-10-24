def letterFrequency(text,letter):
    count=0
    for x in text:
        if x == letter:
            count += 1
    return count
text="You never get a second chance to make a first impression"
print(letterFrequency(text,"e"))