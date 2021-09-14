class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input('Enter your name: ')
age = input('Enter your age: ')

p1 = Person(name, age)

# del p1.age
# del p1

print(p1.name)
print(p1.age)

class Country:
    pass