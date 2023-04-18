class Parrot:
    
    #class atribute
    
    name = ""
    age = 0
    
# create Parrot object

parrot1 = Parrot()
parrot1.name = "parrot1"
parrot1.age = 1

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "parrot2"
parrot2.age = 2

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")