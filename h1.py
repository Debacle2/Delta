userWord = input('Provide the desired word to be encypted: ')
userKey = input('Provide the key for encyption: ')

encryptedWord = []

#asciiOutput = ord(userWord) ^ ord(userKey)
#hexConversion = hex(asciiOutput)
#hexDecryption = int(hexConversion, 16) ^ ord(userKey)


for characterPosition, currentCharacter in enumerate(userWord):
    print (characterPosition, currentCharacter)
    print (characterPosition, userKey[characterPosition])
    print ("Phase I is complete.")
    encryptionProcess = ord(currentCharacter) ^ ord(userKey[characterPosition])

    encryptedWord.append(encryptionProcess)

print ("Phase II completed; the following is the result:")
print (encryptedWord)

print ("Phase III commencing...")

for item in encryptedWord:
    print (hex(item) + " ", end='')

print()

print ("Phase IV commencing...")

for item in encryptedWord:
    print (format(item, 'x') + " ", end='')