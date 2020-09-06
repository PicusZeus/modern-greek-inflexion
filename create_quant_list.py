import pickle
from .create_adj_list import create_all_basic_adj_forms
from .create_noun_list import create_all_basic_noun_forms



file = open('modern_greek_stemmer/el_GR.pickle', 'br')

greek_corpus = pickle.load(file)
file.close()



def create_quant_adj():
    all_quant_adj = []
    for qa in quant_adj:
        temp = create_all_basic_adj_forms(qa)
        adverb = qa[:-1] + 'ν'
        if adverb in greek_corpus:
            temp['adverb'] = adverb

        all_quant_adj.append(temp)

    return all_quant_adj

def create_quant_noun():
    all_quant_noun = []
    for qn in quant_noun:
        temp = create_all_basic_noun_forms(qn)
        all_quant_noun.append(temp)
    return all_quant_noun



