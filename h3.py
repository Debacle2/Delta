originalText = "MikePapaTango"
encryptionKey = "ABC"

print ("Phase I:", originalText)

#print ("Phase II:")
printedString = []
for position, letter in enumerate(originalText):
    x = encryptionKey[position % len(encryptionKey)]
    printedString.append(x)
#    print (x, end='')
print ("Phase II:", printedString)

print ()

encryptedValues = []

for pos, val in enumerate(originalText):
    keyVal = encryptionKey[position % len(encryptionKey)]
    encryptedByte = ord(val) ^ ord(keyVal)
    encryptedValues.append(encryptedByte)

print ("Phase III:", encryptedValues)

printedString1 = []
for item in encryptedValues:
    printedString1.append(hex(item)) 
#    print (hex(item)+ " ", end="")
print ("Phase IV:", printedString1)

print ()
printedString2 = []
for item in encryptedValues:
    printedString2.append(format(item, "x"))
#    print(format(item, "x") + " ", end="")
print ("Phase V:", printedString2)