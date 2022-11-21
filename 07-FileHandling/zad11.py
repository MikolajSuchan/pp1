film_titles=[1,2,3,4,5]
file=open('filmy.txt','w')
for i in film_titles:
    file.write(f"{i}\n")
file.close()