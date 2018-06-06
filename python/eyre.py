# # there is a package called nltk which is the natural language toolkit. load it for this file
# import nltk
#
# # point the program to the filename that is going to be fed into this program
# filename = "eyre.txt"
#
# # given a file name, open it
# with open(filename, 'r') as our_file:
#     #takes the file and reads the text and stores it
#     text = our_file.read()
#
# # print the first 99 characters of the variable text
# print(text[0:100])
#
# # take a long string and break it into words
# words = nltk.word_tokenize(text)
# print(words[0:10])
#
# # lowercase matters! computers are stupid
# if "The" != "the":
#     print("Does case matter?")
#
# # create an empty list called clean_words
# clean_words = []
#
# #loop over every word item in the words list
# for word in words:
#         # make each word lowercase and append it to the new list
#     clean_words.append(word.lower())
# print(clean_words[0:30])

# redoing the above with methods
# there is a package called nltk which is the natural language toolkit. load it for this file
import nltk

def open_file_and_get_text(filename):
    # given a file name, open it
    with open(filename, 'r') as our_file:
        #takes the file and reads the text and stores it
        text = our_file.read()
    return text

def clean_tokens(words):
    # given some tokens, make them all lowercase
    # create an empty list called clean_words
    clean_words = []

    #loop over every word item in the words list
    for word in words:
            # make each word lowercase and append it to the new list
        clean_words.append(word.lower())
    return clean_words

# set a variable file name for where our file is
filename = "eyre.txt"

text = open_file_and_get_text(filename)
# take a long string and break it into words
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)
# print out first 30 words of our clean tokens
# print(clean_words[0:30])
# #
# word_counts = nltk.FreqDist(clean_words)
# print(word_counts.most_common(10))
# print(word_counts['jane'])
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])
