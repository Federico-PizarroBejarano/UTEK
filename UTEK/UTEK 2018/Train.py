alph = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R','S', 'T', 'U','V','W','X','Y','Z']

def build_semantic_descriptors(words):
    d = {}
    for i in range(len(alph)):
        d[alph[i]] = words.count(alph[i])
        for j in range(len(alph)):
            d[alph[i]+alph[j]] = words.count(alph[i] + alph[j])
            for k in range(len(alph)):
                d[alph[i]+alph[j]+alph[k]] = words.count(alph[i] + alph[j]+alph[k])
    
    words = words.split()
    
    
    for i in range(len(words)):
        if len(words[i])>3:
            indx_master = 4
            counter = 0
            while(indx_master <= 7):
                indx = indx_master
                while (indx <= len(words[i])):
                    n_gram = words[i][counter:indx]
                    if n_gram not in d:
                        d[n_gram] = 1
                    else:
                        d[n_gram] += 1
                    counter += 1
                    indx += 1
                counter = 0
                indx_master += 1
    
    dictionary = ''
    for key in d:
        dictionary += key +' '+ str(d[key])
        dictionary += '\n'
    
    dic_file = 'dictionary.txt'
    dicf = open(dic_file, 'w')
    dicf.write(dictionary)
    dicf.close()


filename = 'dataset-2.txt'

words_file = open(filename, 'r', encoding = 'latin1')
words = words_file.read()

words = words.replace('\n', ' ')

for i in ["'", "!","N","<unk>","!","@","#","$","%","^","&", "*", "(", ")", "_", "-", ",", ".", "\\", "/", ":", ";", "<", "[", "]", "{", "}", "|",'0','1','2','3','4','5','6','7','8','9']:
    words = words.replace(i, '')

words = words.upper()

words_file.close()


build_semantic_descriptors(words)

        
 

    
