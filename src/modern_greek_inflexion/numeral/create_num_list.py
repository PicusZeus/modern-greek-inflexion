from modern_greek_accentuation.accentuation import count_syllables, remove_all_diacritics

from ..adjective import create_all_basic_forms
from ..resources.variables import ADJ, ADVERB
from ..resources import greek_corpus


def create_num_adj(numeral: str, cardinal: bool = False) -> dict[ADJ: str, ADVERB: str]:
    """
    :param numeral: numeral in nom masc
    :param cardinal: if it is a cardinal numeral set to True
    :return: a dictionary with two keys, ADJ, under which you get three basic forms (as string "masc/fem/neut"), and ADV
    """

    if cardinal:
        forms = create_all_basic_forms(numeral)
        adverb = ''
        adverb_ordinal = numeral[:-1] + 'ν'
        if adverb_ordinal in greek_corpus:
            if forms[ADVERB] == 'πρώτα':
                adverb = 'πρώτα,πρώτον'
            else:
                adverb = adverb_ordinal
        elif numeral[-4:] != 'στός':
            adverb = forms[ADVERB]
        forms[ADVERB] = adverb
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
        forms = {ADJ: masc + '/' + fem + '/' + neut}
    return forms
