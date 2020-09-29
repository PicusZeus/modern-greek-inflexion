from .create_quant_decl import creat_all_quant_adj_forms
from modern_greek_inflexion.adjective import adjective
from .create_quant_list import create_quant_adj
from modern_greek_inflexion.noun import noun

def create_all_adj_quant(base_form):

    # ordinal or not, it should be assumed, as I don't know about any exception, that ordinals and alike have bese_form
    # that ends on os
    if base_form[-2:] in ['ος', 'ός']:
        # true ordinals
        if base_form in ['δεύτερος', 'τρίτος', 'τέταρτος', 'πέμπτος', 'έκτος', 'έβδομος', 'όγδοος', 'ένατος', 'δέκατος'] or base_form[-4:] == 'στός':
            base_adj = create_quant_adj(base_form, ordinal=True)
            print(base_adj)
            forms_adj = [creat_all_quant_adj_forms(base_adj['adj'], ordinal=True)]
            adverbs = [adv for adv in base_adj['adverb'].split(',')]
            forms = {'adj': forms_adj, 'adverb': adverbs}
        else:
            # they can be treated as common adjectives otherwise, special case is protos
            forms = adjective.create_all(base_form)

            if base_form == 'πρώτος':
                forms['adverb'] = ['πρώτον', 'πρώτα']
            print(forms)
    else:
        base_adj = create_quant_adj(base_form)

        forms_adj = creat_all_quant_adj_forms(base_adj['adj'])
        forms = {'adj': [forms_adj]}

    return forms

def create_all_noun_quant(base_form):
    """
    There is no real difference between noun and quant noun, so noun logic employed
    :param base_form:
    :return:
    """
    return noun.create_all(base_form)
