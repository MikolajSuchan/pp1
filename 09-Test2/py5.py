import re
def f(first_letter,last_letter):
    pattern=r"\b"+first_letter+r"\w*"+last_letter+r"\b"
    file=open("test.txt",encoding="UTF-8")
    file_read=file.read()
    words=re.findall(pattern,file_read)
    return len(words)

print(f("w","d"))


