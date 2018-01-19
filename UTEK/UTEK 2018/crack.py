from random import randint
from math import ceil

alph = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R','S', 'T', 'U','V','W','X','Y','Z']

def decrypt(key, message):
    if 1<=len(key)<=2:
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
    return(new_mess)

def crackA(message):
    decrypts = []
    probabilities = []
    for i in range(26):
        probabilities.append(0)
        
        decrypt_message = decrypt(str(i), message)
        decrypts.append(decrypt_message)
        
        for i in ["'", "!","N","<unk>","!","@","#","$","%","^","&", "*", "(", ")", "_", "-", ",", ".", "\\", "/", ":", ";", "<", "[", "]", "{", "}", "|",'0','1','2','3','4','5','6','7','8','9']:
            decrypt_message = decrypt_message.replace(i, '')
        decrypt_message = decrypt_message.split()
        
        for i in range(len(decrypt_message)):
            probabilities[-1] += probability(decrypt_message[i]) 
        
    max_prob = max(probabilities)
    decrypted_final = decrypts[probabilities.index(max_prob)]
    return decrypted_final

def crackB(num_key, message):
    population = []
    for i in range(1000):
        individual = []
        for key in range(num_key):
            individual.append(randint(0, 25))
        population.append([0, individual])
    gen = 0
    
    selection(population, num_key, message, gen)
    
def selection(population, num_key, message, gen):
    for i in range(len(population)):
        population[i][0] = probability(decrypt(" ".join(map(str, population[i][1])), message))
    population = sorted(population)
    population.reverse()
    gen += 1
    if gen>100:
        print(population[0])
        key = " ".join(map(str, population[0][1]))
        print(decrypt(key, message))
        print(message)
    else:
        mating(population[0:100], num_key, message, gen)

def mating(population, num_key, message, gen):
    new_pop = []
    for i in range(1000):
        partition = randint(0, num_key-1)
        daddy = randint(0, 99)
        mommy = randint(0, 99)
        daughter = population[daddy][1][0:partition] +population[mommy][1][partition:]
        for i in range(randint(0, ceil(num_key/10))):
            loc = randint(0, num_key-1)
            mutation = randint(0, 25)
            daughter[loc] = mutation
        new_pop.append([0, daughter])
    
    selection(new_pop, num_key, message, gen)


def probability(word):
    prob = 0
    indx_master = 7
    counter = 0
    while(indx_master > 0):
        indx = indx_master
        while (indx <= len(word)):
            n_gram = word[counter:indx]
            if n_gram[0:-1] in d and n_gram in d:
                if d[n_gram[0:-1]] != 0:
                    prob += d[n_gram]/d[n_gram[:-1]]/indx_master
            counter += 1
            indx += 1
        counter = 0
        indx_master -= 1
    
    return prob

file = open('dictionary.txt', 'r')
words = file.read().split('\n')

d = {}

for i in range(len(words)):
    dic_line = words[i].split()
    d[dic_line[0]] = int(dic_line[1])

word_fake = input().split("|")
crackB(int(word_fake[0]), word_fake[1])