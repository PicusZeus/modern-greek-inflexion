from .create_adj_basic import create_all_basic_adj_forms
from .create_adj_decl import create_all_adj_forms

def create_all(adj):
    """
    :param adj: masc sg nom form
    :return: dictionary with keys:
    'adj': array with dictionaries of forms and alternative forms
    'comp'. array with dictionaries of all comparative forms and alternative forms (if exists monolektik type)
    'superl': array with dictionaries of all superlative forms and alternative forms (if exists)
    'adv': array of all possible adverbs
    'comp_adv': array of all possible comparative adverbs (if exists)
    'comp_superl': array of all possible superlative adverbs (if exists)

    """
    forms = []
    comp_forms = []
    super_forms = []
    adverbs = []
    comp_adv = []
    super_adv = []

    all_basic_adj_forms = create_all_basic_adj_forms(adj)
    # 'adj': masc, fem, neut forms as a string divided with / ('ωραίος/ωραία/ωραίο') if alternatives, they are added and
    # separated with a coma
    # 'comparative': if exists in form parathetiko + ',' + alt_parathetiko + '/' + uperthetiko + ',' + alt_uperthetiko with
    # form only in masc sing nom
    # 'adverb': adverb form, if alternatives, then separated with coma
    # 'adverb_comparative': if exists, adverb_parathetiko + ',' + alt_adverb_parathetiko + '/' + adverb_uperthetiko + ',' + alt_adverb_uperthetiko

    all_adj_infl_forms = create_all_adj_forms(all_basic_adj_forms['adj'])
    forms.append(all_adj_infl_forms[0])
    if all_adj_infl_forms[1]:
        forms.append(all_adj_infl_forms[1])

    basic_compar = all_basic_adj_forms['comparative']
    if basic_compar:
        compars, superlatives = basic_compar.split('/')
        if compars != '-':
            for compar in compars.split(','):
                base = create_all_basic_adj_forms(compar)
                all_inf_comp_forms, alternatives = create_all_adj_forms(base['adj'])

                if all_inf_comp_forms:
                    comp_forms.append(all_inf_comp_forms)
                if alternatives:
                    comp_forms.append(alternatives)
        if superlatives:
            for superlative in superlatives.split(','):
                base = create_all_basic_adj_forms(superlative)
                all_inf_superl_forms, alternatives = create_all_adj_forms(base['adj'])
                if all_inf_superl_forms:
                    super_forms.append(all_inf_superl_forms)
                if alternatives:
                    super_forms.append(alternatives)

    if all_basic_adj_forms['adverb']:
        for adverb in all_basic_adj_forms['adverb'].split(','):
            adverbs.append(adverb)

    if all_basic_adj_forms['adverb_comparative']:
        adv_comparatives, adv_superlatives = all_basic_adj_forms['adverb_comparative'].split('/')
        if adv_comparatives != '-':
            for adv_comparative in adv_comparatives.split(','):
                comp_adv.append(adv_comparative)
        if adv_superlatives != '-':
            for adv_superlative in adv_superlatives.split(','):
                super_adv.append(adv_superlative)

    result = {'adj': forms, 'comp': comp_forms,
              'superl': super_forms, 'adv': adverbs,
              'comp_adv': comp_adv, 'superl_adv': super_adv}

    return result