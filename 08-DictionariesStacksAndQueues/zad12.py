import json
movie={
    "title":"Avengers Infinity Wars",
    "year":2018,
    "Directed by":"Russo brothers",
    "earnings":678000000,
    "English language":True,
}
file=open("favourite.json","w")
file.write(json.dumps(movie,indent=4))
file.close()