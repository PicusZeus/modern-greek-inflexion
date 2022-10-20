from .. import adjective
from ..resources import irregular_adv


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
    if adverb in irregular_adv:
        result = {'adv': {adverb}}
        comp_adv, superl_adv = irregular_adv[adverb]['comp_adv'].split('/')
        result['comp_adv'] = {comp_adv}
        result['superl_adv'] = {superl_adv}
        if 'comp' in irregular_adv[adverb]:
            comp_base, superl_base = irregular_adv[adverb]['comp'].split('/')
            comp = adjective.create_all(comp_base)['adj']
            superl = adjective.create_all(superl_base)['adj']
            result['comp'] = comp
            result['superl'] = superl

        return result
    else:

        return {'adv': {adverb}}
