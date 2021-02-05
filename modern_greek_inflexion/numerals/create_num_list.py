from modern_greek_inflexion.adjective.create_adj_basic import create_all_basic_adj_forms
from modern_greek_accentuation.accentuation import count_syllables, remove_all_diacritics
from ..resources import greek_corpus


def create_num_adj(numeral, ordinal=False):
    """
    :param numeral:
    :param ordinal:
    :return:
    """

    if ordinal:
        forms = create_all_basic_adj_forms(numeral)
        adverb = ''
        adverb_ordinal = numeral[:-1] + 'ν'
        if adverb_ordinal in greek_corpus:
            if forms['adverb'] == 'πρώτα':
                adverb = 'πρώτα,πρώτον'
            else:
                adverb = adverb_ordinal
        elif numeral[-4:] != 'στός':
            adverb = forms['adverb']
        forms['adverb'] = adverb
    else:
        if numeral[-5:] in ['κόσια', 'χίλια']:
            masc = numeral[:-1] + 'οι'
            fem = numeral[:-1] + 'ες'
            neut = numeral
        elif numeral[-4:] == 'τρία':
            masc = fem = numeral[:-4] + 'τρείς'
            if count_syllables(masc) == 1:
                masc = fem = remove_all_diacritics(masc)
            neut = numeral
        elif numeral[-7:] == 'τέσσερα':
            masc = fem = numeral[:-1] + 'ις'
            neut = numeral
        elif numeral == 'ένα':
            masc = 'ένας'
            fem = 'μία'
            neut = 'ένα'
        elif numeral == 'ενάμισι':
            masc = 'ενάμισης'
            fem = 'μιάμιση'
            neut = 'ενάμισι'

        else:
            masc = fem = neut = numeral
        forms = {'adj': masc + '/' + fem + '/' + neut}
    return forms





