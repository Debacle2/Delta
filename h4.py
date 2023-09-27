cypherTextHex = "37001e00070f001a1c0601071b01035d55371b1a500f1418114f03081918110b50131d0b54091909140254373f35552d1c0e1c0b1000130a51473a00541b1f47170713081515550f1a0b5005101a000a024701061d01171454"
cypherTextByte = bytes.fromhex(cypherTextHex)

with open("hWords1.txt", "r") as file:
    for line in file:
        key = line.strip().encode()
        decrypted = bytearray()
#        print(line.strip())

        for i in range(len(cypherTextByte)):
            decrypted.append(cypherTextByte[i] ^ key[i % len(key)])
        
        if all(32 <= byte <= 126 for byte in decrypted):
            print("Trying: " + line)
            print("Decrypted (ASCII):", decrypted.decode())


#byteList = [cypherTextHex[i:i+2] for i in range(0, len(cypherTextHex), 2)]
#formatByte = [f'0x{byte}' for byte in byteList]
#print (formatByte)