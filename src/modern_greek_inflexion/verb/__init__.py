
from .. import adjective
from ..adjective.create_adj_decl import create_all_adj_forms
from ..helping_functions import merging_all_dictionaries
from .create_verb_forms import create_all_imperfect_personal_forms, create_all_perf_non_past_personal_forms, \
    create_all_past_personal_forms
from .create_verb_list import create_all_basic_forms
from modern_greek_accentuation.accentuation import convert_to_monotonic

import re
greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)


def create_basic_forms(verb):
    return create_all_basic_forms(verb)


def create_all_forms(verb):

    verb = convert_to_monotonic(verb, one_syllable_rule=False)
    basic_forms = create_all_basic_forms(verb)
    all_forms = {}

    modal = basic_forms['modal']

    "present"
    present = {}

    if 'error' in basic_forms:
        return {"error": f"verb {verb} is incorrect, probably doesnt exist in the corpus"}
    present_basic_forms = basic_forms['present']

    if 'active' in present_basic_forms:
        # only here, because we have lemma situation, all possible conjugation are also created
        # (that is if you have τηλεφωνώ (άω), also forms from the τηλεφωνώ type are added
        pres_act_forms = create_all_imperfect_personal_forms(present_basic_forms['active'], 'active')
        present['active'] = pres_act_forms
    if 'passive' in present_basic_forms:
        # here you can have more possible forms
        pres_passive_forms = create_all_imperfect_personal_forms(present_basic_forms['passive'], 'passive')

        present['passive'] = pres_passive_forms

        if 'active' not in present_basic_forms:
            deponens = True

    all_forms['present'] = present
    'conjunctive'
    if 'conjunctive' in basic_forms:
        conjunctive_basic_forms = basic_forms['conjunctive']
        conjunctive = {}
        active_root = None
        if 'active' in conjunctive_basic_forms:
            con_active_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms['active'], 'active')
            active_root = list(conjunctive_basic_forms['active'])[0][:-1]
            conjunctive['active'] = con_active_forms

        if 'passive' in conjunctive_basic_forms:

            con_passive_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms['passive'], 'passive',
                                                                        active_root_for_imp=active_root)
            if basic_forms['modal']:
                del con_passive_forms['imp']
            conjunctive['passive'] = con_passive_forms
        all_forms['conjunctive'] = conjunctive

    "aorist"
    if 'aorist' in basic_forms:
        aorist_basic_forms = basic_forms['aorist']

        aorist = {}
        if 'active' in aorist_basic_forms:

            aor_active_forms = create_all_past_personal_forms(aorist_basic_forms['active'], verb, 'perf', 'active')
            if modal:
                aor_active_forms['ind'].pop('pl', None)
                aor_active_forms['ind']['sg'].pop('pri', None)
                aor_active_forms['ind']['sg'].pop('sec', None)
            aorist['active'] = aor_active_forms
        if 'passive' in aorist_basic_forms:
            aor_passive_forms = create_all_past_personal_forms(aorist_basic_forms['passive'], verb, 'perf', 'passive')
            aorist['passive'] = aor_passive_forms

        all_forms['aorist'] = aorist

    # "paratatikos"
    if 'paratatikos' in basic_forms:
        paratatikos_basic_forms = basic_forms['paratatikos']
        paratatikos = {}
        if 'active' in paratatikos_basic_forms:
            paratatikos_active_forms = create_all_past_personal_forms(paratatikos_basic_forms['active'], verb, 'imperf',
                                                                      'active')
            paratatikos['active'] = paratatikos_active_forms
        if 'passive' in paratatikos_basic_forms:
            paratatikos_passive_forms = create_all_past_personal_forms(paratatikos_basic_forms['passive'], verb,
                                                                       'imperf', 'passive')
            paratatikos['passive'] = paratatikos_passive_forms
        all_forms['paratatikos'] = paratatikos

    # "act_pres_participle"
    if "act_pres_participle" in basic_forms:
        all_forms['act_pres_participle'] = basic_forms['act_pres_participle']

    arch_act_pres_participle = {}
    for participle_type in ['arch_act_pres_participle', 'active_aorist_participle', 'passive_aorist_participle']:
        if participle_type in basic_forms:

            all_possible_infl_forms = []
            for participle in basic_forms[participle_type]:
                res = create_all_adj_forms(participle)
                all_possible_infl_forms.append(res[0])

            all_forms[participle_type] = merging_all_dictionaries(*all_possible_infl_forms)

    pass_pres_participle = {}

    for participle_type in ['pass_pres_participle', 'passive_perfect_participle']:
        if participle_type in basic_forms:
            all_possible_infl_forms = []
            for participle in basic_forms[participle_type]:
                res = adjective.create_all(participle)['adj']
                all_possible_infl_forms.append(res)
            all_forms[participle_type] = merging_all_dictionaries(*all_possible_infl_forms)

    return all_forms
