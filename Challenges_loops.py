# Create a function named divisible_by_ten() that takes a list of numbers
# named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
  final_numbers = []

  for num in nums:
    if num % 10 == 0:
      final_numbers.append(num)
      
  return len(final_numbers) 


print(divisible_by_ten([20, 25, 30, 35, 40]))

 # Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

def add_greetings(names):
  greetings = []

  for name in names:
    greetings.append("Hello, " + name)
  
  return greetings


print(add_greetings(["Owen", "Max", "Sophie"]))



# Write a function called delete_starting_evens() that has a parameter named lst.

# The function should remove elements from the front of lst until the front of
# the list is not even. The function should then return lst.

# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_
# starting_evens(lst) should return [11, 12, 15]

# Make sure your function works even if every element in the list is even!


def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst.pop(0)
    return lst


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Create a function named odd_indices() that has one parameter named lst.

# The function should create a new empty list and add every element from lst
# that has an odd index. The function should then return this new list.

# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].


def odd_indices(lst):
    new_list = []
    for index, value in enumerate(lst):
        if index % 2 != 0:
            new_list.append(value)

    return new_list


print(odd_indices([4, 3, 7, 10, 11, -2]))

# Create a function named exponents() that takes two lists as parameters named
# ases and powers. Return a new list containing every number in bases raised
# to every number in powers.


def exponents(bases, powers):
    new_bases = []
    for base in bases:
        for power in powers:
            new_bases.append(base ** power)
    return new_bases


# Create a function named larger_sum() that takes two lists of numbers as
# parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number.
# If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    sum_lst1 = sum(lst1)
    sum_lst2 = sum(lst2)

    if sum_lst1 > sum_lst2:
        return lst1
    elif sum_lst1 == sum_lst2:
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))