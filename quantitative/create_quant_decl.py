import copy
from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate

from adjective.create_adj_decl import create_all_adj_forms


def creat_all_quant_adj_forms(quant_base_forms):
    """

    :param quant_base_forms:
    :return:
    """
    all_forms = create_all_adj_forms(quant_base_forms)

    return all_forms


# card_basic = {
#                     'masc':{
#                         'nom': '',
#                         'gen': '',
#                         'acc': '',
#                         'voc': ''
#                     },
#                     'fem':{
#                         'nom': '',
#                         'gen': '',
#                         'acc': '',
#                         'voc': ''},
#                     'neut':{
#                         'nom': '',
#                         'gen': '',
#                         'acc': '',
#                         'voc': ''}
#                     }
#
#
#
# def create_card_decl(quantifier):
#     # quantifier  {'fem': 'μία', 'masc': 'ένας', 'neut': 'ένα'}
#     fem = quantifier['fem']
#     masc = quantifier['masc']
#     neut = quantifier['neut']
#
#     forms = copy.deepcopy(card_basic)
#
#     # 1
#     if masc == 'ένας':
#         forms['masc']['nom'] = 'ένας,είς'
#         forms['masc']['gen'] = 'ενός'
#         forms['masc']['acc'] = 'ένα,έναν'
#         forms['masc']['voc'] = 'ένα'
#         forms['fem']['nom'] = 'μια,μία'
#         forms['fem']['gen'] = 'μίας,μιας'
#         forms['fem']['acc'] = 'μια,μιαν,μία,μίαν'
#         forms['fem']['voc'] = 'μια,μία'
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = 'ενός'
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#     elif masc == 'ενάμισης':
#         forms['masc']['nom'] = masc
#         forms['masc']['gen'] = masc[:-1]
#         forms['masc']['acc'] = masc[:-1]
#         forms['masc']['voc'] = masc[:-1]
#         forms['fem']['nom'] = fem
#         forms['fem']['gen'] = fem + 'ς'
#         forms['fem']['acc'] = fem
#         forms['fem']['voc'] = fem
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = neut
#         forms['neut']['voc'] = neut
#         forms['neut']['acc'] = neut
#     elif neut[-4:] == 'τρία':
#         forms['masc']['nom'] = masc
#         forms['masc']['gen'] = neut[:-4] + 'τριών'
#         forms['masc']['acc'] = masc
#         forms['masc']['voc'] = masc
#         forms['fem']['nom'] = fem
#         forms['fem']['gen'] = neut[:-4] + 'τριών'
#         forms['fem']['acc'] = fem
#         forms['fem']['voc'] = fem
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = neut[:-4] + 'τριών'
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#     elif neut[-8:] == 'τέσσερα':
#         forms['masc']['nom'] = masc
#         forms['masc']['gen'] = neut[:-8] + 'τεσσάρων'
#         forms['masc']['acc'] = masc
#         forms['masc']['voc'] = masc
#         forms['fem']['nom'] = fem
#         forms['fem']['gen'] = neut[:-8] + 'τεσσάρων'
#         forms['fem']['acc'] = fem
#         forms['fem']['voc'] = fem
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = neut[:-8] + 'τεσσάρων'
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#     elif neut[-4:] == 'εφτά':
#         alt = neut[:-4] + 'επτά'
#         forms['masc']['nom'] = masc + ',' + alt
#         forms['masc']['gen'] = masc + ',' + alt
#         forms['masc']['acc'] = masc + ',' + alt
#         forms['masc']['voc'] = masc + ',' + alt
#         forms['fem']['nom'] = masc + ',' + alt
#         forms['fem']['gen'] = masc + ',' + alt
#         forms['fem']['acc'] = masc + ',' + alt
#         forms['fem']['voc'] = masc + ',' + alt
#         forms['neut']['nom'] = masc + ',' + alt
#         forms['neut']['gen'] = masc + ',' + alt
#         forms['neut']['acc'] = masc + ',' + alt
#         forms['neut']['voc'] = masc + ',' + alt
#     elif neut[-4:] == 'οχτώ':
#         alt = neut[:-4] + 'οκτώ'
#         forms['masc']['nom'] = masc + ',' + alt
#         forms['masc']['gen'] = masc + ',' + alt
#         forms['masc']['acc'] = masc + ',' + alt
#         forms['masc']['voc'] = masc + ',' + alt
#         forms['fem']['nom'] = masc + ',' + alt
#         forms['fem']['gen'] = masc + ',' + alt
#         forms['fem']['acc'] = masc + ',' + alt
#         forms['fem']['voc'] = masc + ',' + alt
#         forms['neut']['nom'] = masc + ',' + alt
#         forms['neut']['gen'] = masc + ',' + alt
#         forms['neut']['acc'] = masc + ',' + alt
#         forms['neut']['voc'] = masc + ',' + alt
#     elif neut[-5:] == 'εννιά':
#         alt = neut[:-5] + 'εννέα'
#         forms['masc']['nom'] = masc + ',' + alt
#         forms['masc']['gen'] = masc + ',' + alt
#         forms['masc']['acc'] = masc + ',' + alt
#         forms['masc']['voc'] = masc + ',' + alt
#         forms['fem']['nom'] = masc + ',' + alt
#         forms['fem']['gen'] = masc + ',' + alt
#         forms['fem']['acc'] = masc + ',' + alt
#         forms['fem']['voc'] = masc + ',' + alt
#         forms['neut']['nom'] = masc + ',' + alt
#         forms['neut']['gen'] = masc + ',' + alt
#         forms['neut']['acc'] = masc + ',' + alt
#         forms['neut']['voc'] = masc + ',' + alt
#     elif neut == 'μηδέν':
#
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = neut
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#
#     elif neut == 'δεκαέξι':
#         alt = 'δεκάξι'
#         forms['masc']['nom'] = masc + ',' + alt
#         forms['masc']['gen'] = masc + ',' + alt
#         forms['masc']['acc'] = masc + ',' + alt
#         forms['masc']['voc'] = masc + ',' + alt
#         forms['fem']['nom'] = masc + ',' + alt
#         forms['fem']['gen'] = masc + ',' + alt
#         forms['fem']['acc'] = masc + ',' + alt
#         forms['fem']['voc'] = masc + ',' + alt
#         forms['neut']['nom'] = masc + ',' + alt
#         forms['neut']['gen'] = masc + ',' + alt
#         forms['neut']['acc'] = masc + ',' + alt
#         forms['neut']['voc'] = masc + ',' + alt
#
#     elif masc[-2:] == 'οι':
#         forms['masc']['nom'] = masc
#         forms['masc']['gen'] = masc[:-2] + 'ων' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ων', true_syllabification=False)
#         forms['masc']['acc'] = masc[:-2] + 'ους' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ους', true_syllabification=False)
#         forms['masc']['voc'] = masc
#         forms['fem']['nom'] = fem
#         forms['fem']['gen'] = masc[:-2] + 'ων' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ων', true_syllabification=False)
#         forms['fem']['acc'] = fem
#         forms['fem']['voc'] = fem
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = masc[:-2] + 'ων' + ',' + put_accent_on_the_penultimate(masc[:-2] + 'ων', true_syllabification=False)
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#
#         if masc[:4] == 'οχτα':
#             alt = 'οκτα'
#             for gender in forms:
#                 for case in forms[gender]:
#                     forms[gender][case] += ',' + forms[gender][case].replace(masc[:4], alt)
#         elif masc[:4] == 'εφτα':
#             alt = 'επτα'
#             for gender in forms:
#                 for case in forms[gender]:
#                     forms[gender][case] += ',' + forms[gender][case].replace(masc[:4], alt)
#         elif masc[:5] == 'εννια':
#             alt = 'εννεα'
#             for gender in forms:
#                 for case in forms[gender]:
#                     forms[gender][case] += ',' + forms[gender][case].replace(masc[:5], alt)
#
#     else:
#         forms['masc']['nom'] = masc
#         forms['masc']['gen'] = masc
#         forms['masc']['acc'] = masc
#         forms['masc']['voc'] = masc
#         forms['fem']['nom'] = fem
#         forms['fem']['gen'] = fem
#         forms['fem']['acc'] = fem
#         forms['fem']['voc'] = fem
#         forms['neut']['nom'] = neut
#         forms['neut']['gen'] = neut
#         forms['neut']['acc'] = neut
#         forms['neut']['voc'] = neut
#
#     return forms