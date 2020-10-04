import pickle
import sys
"create a list of all Greek words in a pickled set"

# there are sometimes flags on the words i dont understand, and probably I dont need them

def create_picle_el_gr(files):

    lists_of_words = [open(l, 'r').read().splitlines() for l in files]
    all_words = []
    for list_of_words in lists_of_words:
        words = [word.split('/')[0].lower() for word in list_of_words]
        all_words.extend(words)
    all_words = set(all_words)
    file = open('el_GR.pickle', 'bw')
    pickle.dump(all_words, file)
    file.close()
    print('list created')


if __name__ == "__main__":
    print(sys.argv[1:])
    create_picle_el_gr(sys.argv[1:])


