promise = "I will not chew gum in class"

for i in range(5):
    print(promise)


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)


dog_breeds_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print("They have the dog I want!")
        break


ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age < 21:
        continue
    else:
        print(age)


all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)
  
print(students_in_poetry)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
    for sales in location:
        scoops_sold += sales
        print(scoops_sold)


# it returns the sum of all the squares of numbers between 0 and x (not
# included). Remember that you can use the range(x) function to generate a
# sequence of numbers from 0 to x (not included).


def square(n):
    return n*n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


# In math, the factorial of a number is defined as the product of an integer
# and all the integers below it. For example, the factorial of four (4!) is
# equal to 1*2*3*4=24. Fill in the blanks to make the factorial function
# return the right number.


def factorial(n):
    result = 1
    for i in range(1,n):
        result += result*i
    return result


print(factorial(4))
# should return 24
print(factorial(5))
# should return 120
