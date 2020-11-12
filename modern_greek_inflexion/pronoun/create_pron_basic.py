
from modern_greek_accentuation.accentuation import put_accent_on_the_ultimate, where_is_accent, put_accent
from modern_greek_inflexion.adjective import adjective


def create_basic_forms(pron):
    """
    :param pron: pronoun in nom sg masc, if declination applies
    :return: as in adj masc/fem/neut
    """

    #pronoun = {gender:{number}}


    if pron[-2:] in ['ος', 'ός'] or pron[-3:] in ['πας'] and pron != 'τίνος':
        # like poios
        bas_forms = adjective.create_all_basic_adj_forms(pron)['adj']
    elif pron[-2:] in ['οι', 'οί']:
        accent = where_is_accent(pron)
        fem = put_accent(pron[:-2] + 'ες', accent, true_syllabification=False)
        neut = put_accent(pron[:-2] + 'α', accent, true_syllabification=False)
        bas_forms = pron + '/' + fem + '/' + neut
    elif 'δήποτε' in pron:
        suffix = 'δήποτε'
        pron_r = pron[:-6]

        if pron_r[-2:] == 'οσ':
            bas_forms_r = adjective.create_all_basic_adj_forms(pron_r[:-1] + 'ς')['adj']
            fem = bas_forms_r.split('/')[1]
            neut = bas_forms_r.split('/')[2]
            bas_forms = pron + '/' + fem + suffix+ '/' + neut+ suffix
        else:
            bas_forms = pron + '/' + pron  + '/' + pron

    elif pron[-4:] == 'ένας' or pron[-3:] == 'είς':
        # all the pron like kathenas
        masc_length = 4
        if pron[-3:] == 'είς':
            masc_length = 3
        masc = pron
        fem = pron[:-masc_length] + 'εμία'
        if len(pron) > 4 and pron[-(masc_length+1)] == 'ν':
            fem = pron[:-(masc_length+1)] + 'μία'
        if pron == 'ένας':
            fem = 'μία'

        neut = pron[:-masc_length] + 'ένα'

        fem = fem + ',' + put_accent_on_the_ultimate(fem)

        bas_forms = masc + '/' + fem + '/' + neut

    elif pron == 'τις':

        bas_forms = 'τις/τις/τι'
    elif pron == 'όστις':

        bas_forms = 'όστις/ήτις/ότι'

    elif pron == 'όσπερ':

        bas_forms = 'όσπερ/ήπερ/όπερ'

    elif pron[-1] in ['η', 'ὴ'] or pron in ['μηδεμία', 'μερικοί', 'μου', 'πάσα', 'παν', 'όσο',  'τίνος']:
        # there are some random fem nine forms in the list, should be filter out
        #     return None # also random forms of personal and other forms pron have to be filter out
        #     #     return Non
        return None

    else:
        bas_forms = pron + '/' + pron + '/' + pron

    return bas_forms



