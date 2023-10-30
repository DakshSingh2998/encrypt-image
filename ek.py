from os import urandom
import copy

def getKey(length):
    return bytearray(urandom(length))

def encrypt():
    try:
        path = input('Enter path of Image : ')
        fin = open(path, 'rb')
         
        image = fin.read()
        fin.close()         
        image = bytearray(image)
        
        keyArray = getKey(len(image))
        imageCopy = copy.deepcopy(image)
        for index, values in enumerate(imageCopy):
            keyIndexToUse = (index + 2 if (index % 2 == 0) else index + 1) % len(image)
            image[len(image) - index - 1] = values ^ keyArray[keyIndexToUse]
        path = path.split(".")[0]
        fk = open(path + ".dd", 'wb')
        fk.write(keyArray)
        fk.close()
        
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Done...')
    except Exception as e:
        print('Error caught: ' + e)

def decrypt():
    try:
        path = input('Enter path of Image : ')
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        fk = open(path + ".dd", 'rb')
        keyArray = fk.read()
        fk.close()
        image = bytearray(image)
        imageCopy = copy.deepcopy(image)
        for index, values in enumerate(imageCopy):
            keyIndexToUse = len(image) - index - 1
            keyIndexToUse =  (keyIndexToUse + 2 if (keyIndexToUse % 2 == 0) else keyIndexToUse + 1) % len(image)
            image[len(image) - index - 1] = values ^ keyArray[keyIndexToUse]
     
        fin = open(path + ".jpg", 'wb')
         
        fin.write(image)
        fin.close()
        print('Done...')
    except Exception as e:
        print('Error caught: ' + e)

inputt = bool(int(input("Enter 0 for decrypting and 1 for encrypting: ")))
if inputt == True:
    encrypt()
else:
    decrypt()
