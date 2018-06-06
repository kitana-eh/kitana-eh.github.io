def add (x, y):
  print (x + y)

number = 4
add(3, number)
# result should be 7

def say_hello(name):
  print("Hi my name is " + name)

say_hello("Kitana")
# result should be -- Hi my name is Kitana

names = ["Brandon", "Tony", "Ethan", "Maple"]

for name in names:
  say_hello(name)
#result should be:
# Hi my name is Brandon
# Hi my name is Tony
# Hi my name is Ethan
# Hi my name is Maple

def grocery_list(veggies):
    print(veggies)

veggies = ["broccoli", "carrots", "cauliflower", "brussels sprouts", "onions"]
for vegetable in veggies:
    grocery_list(vegetable)
#results should look like:
# broccoli
# carrots
# cauliflower
# brussels sprouts
# onions

# Exercise on page 43
# Easier to use a dictionary with a for loop than to try to combine two lists
authors = {
"Charles Dickens" : "1870",
"William Thackeray" : "1863",
"Anthony Trollope" : "1882",
"Gerard Manley Hopkins" : "1889"
}
for author, year in authors.items():
    print(author + " kicked the bucket in " + year + ".")

# To do the above with two lists, need to use a counter to line up each
# len refers to the length of the list
counter = 0
while counter <len(names):
    print(names[counter] + dates[counter])
    counter = counter + 1

# Exercise on page 46
year_of_origin = 2000
if year_of_origin < 1900:
    print("Welcome to the future, time traveler!")
elif year_of_origin >= 1900 and year_of_origin <= 2020:
    print("Welcome to the present, time traveler!")
else:
    print("Welcome to the past, time traveler!")
