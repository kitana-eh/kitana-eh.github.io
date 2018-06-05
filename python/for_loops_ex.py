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
