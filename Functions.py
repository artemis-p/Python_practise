def sing_song():
    print("You may say I'm a dreamer")
    print("But I'm not the only one")
    print("I hope some day you'll join us")
    print("And the world will be as one")


sing_song()
sing_song()


def loading_screen():
    print("This page is loading...")


loading_screen()


def about_this_computer():
    print("This computer is running on version Everest Puma")


print("This is your desktop")

about_this_computer()


def mult_two_add_three():
    number = 5
    print(number*2 + 3)


mult_two_add_three()


def mult_two_add_three(number):
    print(number*2 + 3)


mult_two_add_three(1)
mult_two_add_three(5)
mult_two_add_three(-1)
mult_two_add_three(0)


def mult_x_add_y(number, x, y):
    print(number*x + y)


mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)


# keyword arguments, where we explicitly refer to what each argument is
# assigned to in the function call.

# Define create_spreadsheet():
def create_spreadsheet(title):
    print("Creating a spreadsheet called "+title)


# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")


# Define create_spreadsheet():
def create_spreadsheet(title, row_count=1000):
    print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")


# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)


def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target

    return low_limit, high_limit


low, high = get_boundaries(100, 20)


def repeat_stuff(stuff, num_repeats=10):
    return stuff*num_repeats


lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)