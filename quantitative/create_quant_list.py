import pickle
from adjective.create_adj_basic import create_all_basic_adj_forms
from noun.create_noun_basic import create_all_basic_noun_forms

with open('el_GR.pickle', 'br') as file:
    greek_corpus = pickle.load(file)


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


