people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]


def f(person):
    return person["house"]


people.sort(key=f)
print(people)

# For avoiding to create a function f, we can use lambda
# lambda is an anonymous function
# lambda person: person["name"] is equivalent to f(person)
people.sort(key=lambda person: person["name"])
