import numpy as np
import random
tabby = open('garfield.txt', encoding='utf8').read()

corpus = tabby.split()
names = ['Garfield: ', 'Jon: ', 'Liz: ']

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
def chainLine(corpus):
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
     
    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [names[random.randint(0,2)],first_word]


    check = False
    while check == False:
        if chain[-1].endswith("."):
            check = True
            break
        if chain[-1].endswith("!"):
            check = True
            break
        if chain[-1].endswith("?"):
            check = True
            break
        else:
            chain.append(np.random.choice(word_dict[chain[-1]]))
            ' '.join(chain)
    return chain

def sentence(chain):
    n = len(chain)
    i = 0
    lineString = " "
    for i in range(n):
        lineString = lineString+chain[i]+" "
    return lineString
    
def stripGen(x,corpus):
    j = 0
    strip = " "
    for j in range(x):
        strip = strip + sentence(chainLine(corpus))+"\n"
    return strip
     

    

