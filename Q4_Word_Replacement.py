isInputLoopRunning = True
replacement_dictionary = {}
while isInputLoopRunning == True:
    word_pairs = input('Enter pairs of words and replacement on one line. q to Quit: ')
    if (word_pairs != 'q'):
        word_pairs = word_pairs.strip()
        # [original, replacement, original, replacement, ...]
        word_list = word_pairs.split(' ')
        
        # Check if pairs exist otherwise exit
        if len(word_list)%2 == 0:
            for i in range(0, len(word_list), 2):
                replacement_dictionary[word_list[i]] = word_list[i+1]
    else:
        isInput = False
        break

isSentenceLoopRunning = True
while isSentenceLoopRunning == True:
    sentence = input('Enter a sentence. q to quit: ')
    for key in replacement_dictionary.keys():
        sentence = sentence.replace(key, replacement_dictionary.get(key))
    print(sentence)