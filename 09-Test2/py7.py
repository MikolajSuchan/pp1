import re
tekst="nioero nio nio nio nio nio i co"
wrzorzec=r"\bn"+r"\w*"+r"o\b"
hmm=re.findall(wrzorzec,tekst)
print(len(hmm))