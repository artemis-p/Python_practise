class Flower:
    color = 'unknown'


rose = Flower()

rose.color = "red"
violet = Flower()

violet.color = "blue"

this_pun_is_for_you = "Darling, sweet I love you"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)


class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Luke") 
# Call the greeting method
print(some_person.greeting())