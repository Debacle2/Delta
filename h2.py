encryptedText = ['0x11', '0x03', '0x10', '0x17', '0x12']
encryptionKey = "PASSW"

encryptedValues = []

for item in encryptedText:
    encryptedValues.append(int(item, 16))
print ("Phase I:", encryptedValues)

decryptedValues = []

for pos, val in enumerate(encryptedValues):
    decryptedValue = val ^ ord(encryptionKey[pos])
    decryptedValues.append(decryptedValue)

print ("Phase II: ", decryptedValues)

print ()

print ("Phase III:")
for item in decryptedValues:
    print (chr(item), end="")
