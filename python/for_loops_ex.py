fruits = ["kiwi", "strawberry", "plum"]
results = []
for item in fruits:
    results.append(item)

print(results)

numbers = [1, 2, 3, 4, 5]
results =[]

for item in numbers:
    results.append(item + 5)

print(results)

# Exercise 1 on page 16 of Python Programming Concepts II slides: Given a list of 5 numbers
# a for loop to create a new list named "data" that consists of the original numbers with 10 subtracted
numbers = [10, 20, 30, 40, 50]
data = []

for item in numbers:
        data.append(item - 10)

print(data)

# Exercise 2 on page 16 of Python Programming Concepts II slides: Do the same thing as above but
# simplify your code so that it uses a list comprehension
numbers = [60, 70, 80, 90, 100]
data = []

data = [item - 10 for item in numbers]

print(data)

# Create a list of four places you would like to visit
# Print out each of those places using a loop

places_to_visit = ["Malaysia", "Singapore", "South Africa", "Peru", "Brazil"]

for item in places_to_visit:
    print("I would like to visit " + item + ".")

# On page 19 - Conditional - do something if a condition is true
for fruit in fruits:
    if fruit == "plum":
        print(fruit)

# Exercise on page 20: Create a list named hilt_class
hilt_class = ["Kitana", "Leslie"]
for name in hilt_class:
    if name == "Kitana":
        print(name)

hilt_class = ["Kitana", "Leslie"]
for name in hilt_class:
    if name == hilt_class[0]:
        print(name)

# On page 22 - for loops in dictionaries
states = {"VA": "Virginia", "MD": "Maryland"}
for code, state in states.items():
    print(code + " is code for " + state)
# result should be the following--:
# VA is code for Virginia
# MD is code for Maryland

# On page 23 - range
for i in range(10):
    print("I'm at number " + str(i))
# using str(i) to convert the integer to a string to add text before it (or python would be confused)
# result should be the following--:
# I'm at number 0
# I'm at number 1
# I'm at number 2
# I'm at number 3
# I'm at number 4
# I'm at number 5
# I'm at number 6
# I'm at number 7
# I'm at number 8
# I'm at number 9

for i in range(5, 10):
    print("I'm at number " + str(i))
# result should be the following--:
# I'm at number 5
# I'm at number 6
# I'm at number 7
# I'm at number 8
# I'm at number 9

for i in range(0, 10, 2):
    print("I'm at number " + str(i))
# result should be the following--:
# I'm at number 0
# I'm at number 2
# I'm at number 4
# I'm at number 6
# I'm at number 8

# Branching - do something only under certain circumstances
# Exercise on page 26
if fruits[0] == "apple":
    print("Yum!")
elif fruits[0] == "cardboard" or fruits[0] == "sand":
    print("Yuck!")
else:
    print("Not bad.")
#elif means "else if"

# More examples of branching on page 27
if "apple" not in fruits[0]:
    print("Yuck")

age = 5
if age > 0 and age <= 2:
    print("baby")
elif age > 2 and age < 18:
    print("child")
else:
    print("adult")

# Example of while loop on page 28
# continues while a condition is true
# like a for loop with an if
counter = 0

while counter < 5:
    print(counter)
    counter += 1
# += is shorthand for counter = counter + 1

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet[1]
# 'b' - item in 1st position
alphabet[2:7]
# 'cdefg' - everything between 2nd up to 7th item in the list
alphabet[-2:]
# 'yz' - goes from second item to the end and everything to the end

list = ["a", "b", "c", "d", "e"]
list[:-1]
# ['a', 'b', 'c', 'd'] - from the beginning until one item before the end
