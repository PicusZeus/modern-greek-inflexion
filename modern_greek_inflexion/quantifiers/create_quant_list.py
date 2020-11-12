from modern_greek_inflexion.adjective.create_adj_basic import create_all_basic_adj_forms
from modern_greek_accentuation.accentuation import count_syllables, remove_all_diacritics
from ..resources import greek_corpus


def create_quant_adj(quant, ordinal=False):
    """
    :param quant:
    :param ordinal:
    :return:
    """

    if ordinal:
        forms = create_all_basic_adj_forms(quant)
        adverb = ''
        adverb_ordinal = quant[:-1] + 'ν'
        if adverb_ordinal in greek_corpus:
            if forms['adverb'] == 'πρώτα':
                adverb = 'πρώτα,πρώτον'
            else:
                adverb = adverb_ordinal
        elif quant[-4:] != 'στός':
            adverb = forms['adverb']
        forms['adverb'] = adverb
    else:
        if quant[-5:] in ['κόσια', 'χίλια']:
            masc = quant[:-1] + 'οι'
            fem = quant[:-1] + 'ες'
            neut = quant
        elif quant[-4:] == 'τρία':
            masc = fem = quant[:-4] + 'τρείς'
            if count_syllables(masc) == 1:
                masc = fem = remove_all_diacritics(masc)
            neut = quant
        elif quant[-7:] == 'τέσσερα':
            masc = fem = quant[:-1] + 'ις'
            neut = quant

        else:
            masc = fem = neut = quant
        forms = {'adj': masc + '/' + fem + '/' + neut}

    return forms





