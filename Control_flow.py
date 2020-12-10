def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"

    if (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."

    if not (gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."

    if not (gpa >= 2.0) and not (credits >= 120):
        return "You do not meet either requirement to graduate!"


def grade_converter(gpa):
    grade = ""
    if (gpa >= 4.0):
        grade = "A"
    elif (gpa >= 3.0):
        grade = "B"
    elif (gpa >= 2.0):
        grade = "C"
    elif (gpa >= 1.0):
        grade = "D"
    elif (gpa >= 0.0):
        grade = "F"

  return grade

def raises_value_error():
  raise ValueError

try:
  raises_value_error()
except:
  print("You raised a ValueError!")