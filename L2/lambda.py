people = [{"name": "harry", "house": "griffindor"}, 
          {"name": "cho", "house": "Ravenclaw"},
          {"name": "draco", "house": "slytherin"}]

people.sort(key=lambda person: person["name"])
print(people)