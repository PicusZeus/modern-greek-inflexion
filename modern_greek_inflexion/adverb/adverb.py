# add possible comparative adjectives if exists (νωρίτερος κτλ)
from modern_greek_inflexion.adjective import adjective

irregular_comp = {
'νωρίς': {'comp_adv': 'νωρίτερα/'}, 'άνω': {'comp_adv': 'ανώτερα/ανώτατα', 'comp': 'ανώτερος/ανώτατος'}, 'κάτω': {'comp_adv': 'κατώτεαρα/κατώτατα', 'comp': 'κατώτερος/κατώτατος'}}



def create_all(adverb):
    """
    :param adverb:
    :return: returns a dictionary:
    'adv' the same adverb
    'comp_adv' if exists is given in an array
    'superl_adv' if exists is given in an array
    'comp' if exists adj comp created from a given adverb, dictionary is given in an array
    'superl' if exists adj superl created from a given adverb, dictionary is given in an array

    """
    if adverb in irregular_comp:
        result = {'adv': {adverb}}
        comp_adv, superl_adv = irregular_comp[adverb]['comp_adv'].split('/')
        result['comp_adv'] = {comp_adv}
        result['superl_adv'] = {superl_adv}
        if 'comp' in irregular_comp[adverb]:
            comp_base, superl_base = irregular_comp[adverb]['comp'].split('/')
            comp = adjective.create_all(comp_base)['adj']
            superl = adjective.create_all(superl_base)['adj']
            result['comp'] = comp
            result['superl'] = superl

        return result
    else:

        return {'adv': {adverb}}
