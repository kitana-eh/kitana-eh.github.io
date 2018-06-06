# there is a package called nltk which is the natural language toolkit. load it for this file
import nltk

# point the program to the filename that is going to be fed into this program
filename = "eyre.txt"

# given a file name, open it
with open(filename, 'r') as our_file:
    #takes the file and reads the text and stores it
    text = our_file.read()

# print the first 99 characters of the variable text
print(text[0:100])

# take a long string and break it into words
words = nltk.word_tokenize(text)
print(words[0:10])
