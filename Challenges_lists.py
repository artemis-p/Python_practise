# Create a function called append_size that has one parameter named lst.

# The function should append the size of lst (inclusive) to the end of lst.
# The function should then return this new list.

# For example, if lst was [23, 42, 108], the function should return
# [23, 42, 108, 3] because the size of lst was originally 3.

def append_size(lst):
  lst_size = len(lst)
  lst.append(lst_size)
  return lst


print(append_size([23, 42, 108]))



# Write a function named append_sum that has one parameter — a list named
# named lst.

# The function should add the last two elements of lst together and append the
# result to lst. It should do this process three times and then return lst.

# For example, if lst started as [1, 1, 2], the final result should be
# [1, 1, 2, 3, 5, 8].


def append_sum(lst):
  lst.append(lst[-2] + lst[-1])
  lst.append(lst[-2] + lst[-1])
  lst.append(lst[-2] + lst[-1])
  return lst


print(append_sum([1, 1, 2]))