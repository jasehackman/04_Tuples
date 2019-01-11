
#1 Create a tuple named zoo that contains your favorite animals.
zoo = ("dog", "cat", "mouse", "rat", "bat")


#2 Find one of your animals using the .index(value) method on the tuple.
print(zoo.index("cat"))
#3 Determine if an animal is in your tuple by using value in tuple.
if "cat" in zoo:
  print("yep its here")
#4 Create a variable for each of the animals in your tuple with this cool feature of Python.
(dog, cat, mouse, rat, bat) = zoo
print(rat)
# example
# (lizard, fox, mammoth) = zoo
# print(lizard)


#5 Convert your tuple into a list.
(*dog,) = zoo
print(dog)

zoo = list(zoo)
print(zoo)
#6 Use extend() to add three more animals to your zoo.
zoo.extend(("cow", "sheep"))
#7 Convert the list back into a tuple.
zoo = tuple(zoo)
print(zoo)