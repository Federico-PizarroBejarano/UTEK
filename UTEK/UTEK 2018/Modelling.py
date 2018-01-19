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
                    prob += d[n_gram]/d[n_gram[:-1]]
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

line = input().split('|')
line1 = line[0].split()
line2 = line[1].split()

prob1 = 0
prob2 = 0

for i in range(len(line1)):
    prob1 += probability(line1[i])

for i in range(len(line2)):
    prob2 += probability(line2[i])

prob1 = prob1/len(" ".join(line1))
prob2 = prob2/len(" ".join(line2))

if prob1 > prob2:
    print(1)
else:
    print(2)
    


            

