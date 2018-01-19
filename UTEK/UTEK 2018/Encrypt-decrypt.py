alph = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R','S', 'T', 'U','V','W','X','Y','Z']

def encrypt(key, message):
    if len(key) == 1:
        new_mess = ''
        for i in range(len(message)):
            if message[i] not in alph:
                new_mess += message[i]
            else:
                new_mess += alph[(alph.index(message[i])+int(key))%26]
    elif ' ' in key:
        new_mess = ''
        key = key.split()
        counter = 0
        for i in range(len(message)):
            if message[i] not in alph:
                new_mess += message[i]
            else:
                new_mess += alph[(alph.index(message[i])+int(key[counter%len(key)]))%26]
                counter += 1
    else:
        new_mess = ''
        for i in range(len(message)):
            if message[i] not in alph:
                new_mess += message[i]
            else:
                new_mess += key[(alph.index(message[i]))]
    print(new_mess)
  
  
    
def decrypt(key, message):
    if not key.isalpha() and " " not in key:
        new_mess = ''
        for i in range(len(message)):
            if message[i] not in alph:
                new_mess += message[i]
            else:
                new_mess += alph[(alph.index(message[i])-int(key))%26]
    elif ' ' in key:
        new_mess = ''
        key = key.split()
        counter = 0
        for i in range(len(message)):
            if message[i] not in alph:
                new_mess += message[i]
            else:
                new_mess += alph[(alph.index(message[i])-int(key[counter%len(key)]))%26]
                counter += 1
    else:
        new_mess = ''
        for i in range(len(message)):
            if message[i] not in alph:
                new_mess += message[i]
            else:
                new_mess += alph[(key.index(message[i]))]
    print(new_mess)
    

inp = input().split('|')
if inp[0] == 'ENCRYPT':
    encrypt(inp[1], inp[2])
else:
    decrypt(inp[1], inp[2])

            
        