addressNameString = ''
isAskingForNames = False

while isAskingForNames == False:
    tempInput = input('Enter addresses string names followed by the addresses. q to quit: ')

    if tempInput == 'q':
        isAskingForNames = True
        print("\n") #Skip lines for formatting
        break
    else:
        addressNameString += tempInput
        print() #Add the empty line for formatting

# Clean up the string
addressNameString = addressNameString.strip() #Removes whitespace before and after the string
addressNameList = addressNameString.split(' ')

# Add to a dict
# Every other entry in the list is the person's name
# Each entry + 1 is that person's email
contactInfo = {}
for person in range(0,len(addressNameList), 2):
    contactInfo[addressNameList[person]] = addressNameList[person+1]

# While isRunning is False, keep asking to look up names
isRunning = False

while isRunning == False:
    tempInput = input('Enter name to query, q to quit: ')
    if tempInput == 'q':
        isRunning = True
        break
    else:
        email = contactInfo.get(tempInput)
        if email != None: # Only print if email is found
            print(email + "\n")
