# Take inputs for filename and both bounds
from typing import List


filename = input('Enter file name: ')
# TODO Get rid of test
filename = 'tests/input-words.txt'
lower_bound = input('Bound 1: ')
upper_bound = input('Bound 2: ')

# Open the file stream
file_content = open(filename)
# Readlines returns the value of each line of the file
word_list:list[str]  = file_content.readlines()

# Remove any trailing or leading whitespace/line breaks
for word in range(len(word_list)):
    word_list[word] = word_list[word].strip()

# Make sure list is sorted alphabetically
word_list.sort()
print(word_list)

# Lower index
lower_index = 0
for index in range(len(word_list)):
    if word_list[index] >= lower_bound:
        lower_index = index
        break
print(lower_index)

upper_index = 0
for index in range(lower_index, len(word_list)):
    if word_list[index] <= upper_bound:
        upper_index = index+1

outputList = []
for index in range(lower_index,upper_index):
    outputList.append(word_list[index])
print(upper_index)
print(outputList)