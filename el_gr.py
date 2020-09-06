import pickle
"create a list of all Greek words in a pickled set"

import re

# there are sometimes flags on the words i dont understand, and probably I dont need them




file = open('el_GR.dic.txt', 'r')

file2 = open('el_GR.dic', 'r')

list_of_words = list(file.read().splitlines())

set_of_words = set(word.split('/')[0].lower() for word in list_of_words)

list_of_words_2 = list(file2.read().splitlines())

set_of_words_2 = set(word.split('/')[0].lower() for word in list_of_words_2)

set_of_words = set_of_words.union(set_of_words_2)

print(len(set_of_words))

file.close()

file = open('el_GR.pickle', 'bw')

pickle.dump(set_of_words, file)

file.close()
