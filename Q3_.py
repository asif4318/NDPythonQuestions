filename = input('Please provide a file name: ')

file_content = open(filename)

# Next create list out of the file_content
file_as_list:list[str] = file_content.readlines()

#Get rid of any excess spaces or lines
for word in range(len(file_as_list)):
    file_as_list[word] = file_as_list[word].strip()
    file_as_list[word] = file_as_list[word].replace('\n', '')

# Create dictionary from oringal order
tv_dictionary = {}
for x in range(0, len(file_as_list), 2):
    tv_dictionary[file_as_list[x]] = file_as_list[x+1]

#sort keys in order
sorted_keys = []
for i in sorted(tv_dictionary.keys()):
    sorted_keys.append(i)

# Create dictionary from the sorted order
dictionary_key_sort = {}
for key in sorted_keys:
    dictionary_key_sort[key] = tv_dictionary.get(key)

# Write keys to output file
key_sort_output = open('output_keys.txt', 'w')
for key in dictionary_key_sort:
    key_sort_output.write(key + '\n')
    key_sort_output.write(dictionary_key_sort.get(key)+"\n")


# Sort by Value
sorted_values = []
for value in (tv_dictionary.items()):
    sorted_values.append(value)
sorted_values.sort(key=lambda x:x[1])

# Write to file
value_sort_output = open('output_titles.txt', 'w')
for touple in sorted_values:
    # [0] = Key, [1] = Movie Name
    value_sort_output.write(touple[1]+'\n')
    value_sort_output.write(touple[0]+'\n')