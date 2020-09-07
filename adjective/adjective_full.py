from .create_adj_basic import create_all_basic_adj_forms
from .create_adj_decl import all_adj_forms

def create_all_forms(adj):
    """

    :param adj: masc sg nom form
    :return: tuple with 1: array with dictionaries of forms and alternatives, array with dictionaries of all comparative
     forms and alternatives, array with dictionaries of all superlative forms and alternatives, array with comparative adverbs,
     array with superlative adverbs
    """
    forms = []
    comp_forms = []
    super_forms = []
    comp_adv = []
    super_adv = []

    all_basic_adj_forms = create_all_basic_adj_forms(adj)

    all_adj_infl_forms = all_adj_forms(all_basic_adj_forms[0])
    forms.append(all_adj_infl_forms[0])
    if all_adj_infl_forms[1]:
        forms.append(all_adj_infl_forms[1])

    all_basic_comp_forms = create_all_basic_adj_forms()
