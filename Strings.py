def double_word(word):
    a = word + word
    b = len(a)
    return a + str(b)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

word = "supercalifragilisticexpialidocious"
letter_x = word.index("x")
print(letter_x)


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

def student_grade(name, grade):
	message = "{} received {}% on the exam".format(name, grade)
	return message

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


def username_generator(first_name, last_name):
  if (len(first_name) < 3) or (len(last_name) < 4):
    username = first_name + last_name
  else: 
    username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  password = ""
  for i in range(0, len(username)):
    password += username[i-1] 
  return password