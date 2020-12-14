promise = "I will not chew gum in class"

for i in range(5):
    print(promise)


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)


dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', '    poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print("They have the dog I want!")
        break
