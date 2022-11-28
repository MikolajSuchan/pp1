person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print(person)
print(person.get("name"))
print(person.get("hobby"))
person.update({"surname":"Nowak"})
print(person)
person.update({"married": False})
print(person)
person["gender"]="male"
print(person)
person["hobby"].append("bicykle")
print(person)
person["phone"]["work"]="313131444"
print(person)
