toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 2
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?


cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, char in cool_beasts.items():
    print("{} have {}".format(beast, char))

    wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
    for clothing, colours in wardrobe.items():
        for colour in colours:
            print("{} {}".format(colour, clothing))