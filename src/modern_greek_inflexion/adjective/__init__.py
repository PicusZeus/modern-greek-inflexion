
from .create_adj_basic import create_all_basic_adj_forms
from .create_adj_decl import create_all_adj_forms
from ..exceptions import NotInGreekException
from ..helping_functions import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..resources import ADJ, ADVERB, COMP, COMP_ADV, ADV, COMPARATIVE, ADVERB_COMPARATIVE, SUPERL, SUPERL_ADV
import re

greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)



def create_all_basic_forms(adj):
    return create_all_basic_adj_forms(adj)


def create_all(adj, aklito=False):
    """
    :param aklito: boolean
    :param adj: masc sg nom form
    :return: dictionary with keys:
    'adj': array with dictionaries of forms and alternative forms
    'comp'. array with dictionaries of all comparative forms and alternative forms (if exists monolektik type)
    'superl': array with dictionaries of all superlative forms and alternative forms (if exists)
    'adv': array of all possible adverbs
    'comp_adv': array of all possible comparative adverbs (if exists)
    'comp_superl': array of all possible superlative adverbs (if exists)

    """
    adj = convert_to_monotonic(adj, one_syllable_rule=False)
    if not greek_pattern.match(adj):

        raise NotInGreekException

    forms = []
    comp_forms = []
    super_forms = []
    adverbs = []
    comp_adv = []
    super_adv = []

    all_basic_adj_forms = create_all_basic_adj_forms(adj, aklito=aklito)

    all_adj_infl_forms = create_all_adj_forms(all_basic_adj_forms[ADJ])

    forms.append(all_adj_infl_forms[0])

    if all_adj_infl_forms[1]:
        forms.append(all_adj_infl_forms[1])

    basic_compar = all_basic_adj_forms[COMPARATIVE]
    if basic_compar:
        compars, superlatives = basic_compar.split('/')
        if compars != '-':
            for compar in compars.split(','):
                base = create_all_basic_adj_forms(compar)
                all_inf_comp_forms, alternatives = create_all_adj_forms(base[ADJ])

                if all_inf_comp_forms:
                    comp_forms.append(all_inf_comp_forms)
                if alternatives:
                    comp_forms.append(alternatives)
        if superlatives and superlatives != '-':
            for superlative in superlatives.split(','):
                base = create_all_basic_adj_forms(superlative)
                all_inf_superl_forms, alternatives = create_all_adj_forms(base[ADJ])
                if all_inf_superl_forms:
                    super_forms.append(all_inf_superl_forms)
                if alternatives:
                    super_forms.append(alternatives)

    if all_basic_adj_forms[ADVERB]:
        for adverb in all_basic_adj_forms[ADVERB].split(','):
            adverbs.append(adverb)

    if all_basic_adj_forms[ADVERB_COMPARATIVE]:
        adv_comparatives, adv_superlatives = all_basic_adj_forms[ADVERB_COMPARATIVE].split('/')
        if adv_comparatives != '-':
            for adv_comparative in adv_comparatives.split(','):
                comp_adv.append(adv_comparative)
        if adv_superlatives != '-':
            for adv_superlative in adv_superlatives.split(','):
                super_adv.append(adv_superlative)
    result = {}

    forms = merging_all_dictionaries(*forms)
    result[ADJ] = forms
    if comp_forms:

        comp_forms = merging_all_dictionaries(*comp_forms)
        if not comp_forms:
            raise ValueError
        result[COMP] = comp_forms
    if super_forms:
        super_forms = merging_all_dictionaries(*super_forms)
        result[SUPERL] = super_forms
    if adverbs:
        adverbs = set(adverbs)
        result[ADV] = adverbs
    if comp_adv:
        comp_adv = set(comp_adv)
        result[COMP_ADV] = comp_adv
    if super_adv:
        super_adv = set(super_adv)
        result[SUPERL_ADV] = super_adv

    return result
