people = [
    {"name": "Ali", "house": "Pookan"},
    {"name": "Samira", "house": "Shadman♥"},
    {"name": "Parviz", "house": "Chitgar"}
]

"""def f(person):
    return person["name"]
"""
people.sort(key=lambda person: person["name"])

print(people)