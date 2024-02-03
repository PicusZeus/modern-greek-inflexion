from .create.forms import create_all_imperfect_personal_forms, create_all_perf_non_past_personal_forms, \
    create_all_past_personal_forms
from .. import adjective
from modern_greek_inflexion.adjective.all.create_all_adj import create_all_adj_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries

from modern_greek_inflexion.verb.create.forms.basic.create_basic_all_forms import create_all_basic_forms
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..resources.resources import PRI, SEC, SG, PL, AORIST, ACTIVE, PASSIVE, IMP, CONJUNCTIVE, MODAL, IND, ADJ, PERF, \
    IMPERF
import re

greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)


def create_all_forms(verb: str, para: bool = False) -> dict:
    """
    :param para: how to treat prefix para
    :param verb: self explanatory
    :return:
    """
    verb = convert_to_monotonic(verb, one_syllable_rule=False)
    basic_forms = create_all_basic_forms(verb, para)

    all_forms = {}

    modal = basic_forms[MODAL]

    "present"
    present = {}
    active_pres_con_ind = passive_pres_con_ind = None
    if 'error' in basic_forms:
        return {"error": f"verb {verb} is incorrect, probably doesnt exist in the corpus"}
    present_basic_forms = basic_forms['present']

    if ACTIVE in present_basic_forms:
        # only here, because we have lemma situation, all possible conjugation are also created
        # (that is if you have τηλεφωνώ (άω), also forms from the τηλεφωνώ type are added
        pres_act_forms, active_pres_con_ind = create_all_imperfect_personal_forms(present_basic_forms[ACTIVE], ACTIVE)

        present[ACTIVE] = pres_act_forms
    if PASSIVE in present_basic_forms:
        # here you can have more possible forms
        pres_passive_forms, passive_pres_con_ind = create_all_imperfect_personal_forms(present_basic_forms[PASSIVE], PASSIVE)

        present[PASSIVE] = pres_passive_forms

        if ACTIVE not in present_basic_forms:
            deponens = True

    all_forms['present'] = present
    # CONJUNCTIVE
    if CONJUNCTIVE in basic_forms:
        conjunctive_basic_forms = basic_forms[CONJUNCTIVE]
        conjunctive = {}
        active_roots = None

        if ACTIVE in conjunctive_basic_forms:
            con_active_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms[ACTIVE], ACTIVE)

            active_roots = [x[:-1] for x in conjunctive_basic_forms[ACTIVE]]

            conjunctive[ACTIVE] = con_active_forms

        if PASSIVE in conjunctive_basic_forms:

            con_passive_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms[PASSIVE], PASSIVE,
                                                                        active_root_for_imp=active_roots)

            if basic_forms[MODAL]:
                del con_passive_forms[IMP]
            conjunctive[PASSIVE] = con_passive_forms
        all_forms[CONJUNCTIVE] = conjunctive

    "aorist"
    if AORIST in basic_forms:
        aorist_basic_forms = basic_forms[AORIST]

        aorist = {}
        if ACTIVE in aorist_basic_forms:

            aor_active_forms = create_all_past_personal_forms(aorist_basic_forms[ACTIVE], verb, PERF, ACTIVE)
            if modal:
                aor_active_forms[IND].pop(PL, None)
                aor_active_forms[IND][SG].pop(PRI, None)
                aor_active_forms[IND][SG].pop(SEC, None)
            aorist[ACTIVE] = aor_active_forms
        if PASSIVE in aorist_basic_forms:
            aor_passive_forms = create_all_past_personal_forms(aorist_basic_forms[PASSIVE], verb, PERF, PASSIVE)
            aorist[PASSIVE] = aor_passive_forms

        all_forms[AORIST] = aorist

    # "paratatikos"
    if 'paratatikos' in basic_forms:
        paratatikos_basic_forms = basic_forms['paratatikos']
        paratatikos = {}

        if ACTIVE in paratatikos_basic_forms:
            paratatikos_active_forms = create_all_past_personal_forms(paratatikos_basic_forms[ACTIVE], verb, IMPERF,
                                                                      ACTIVE, active_pres_con_ind)
            paratatikos[ACTIVE] = paratatikos_active_forms
        if PASSIVE in paratatikos_basic_forms:

            paratatikos_passive_forms = create_all_past_personal_forms(paratatikos_basic_forms[PASSIVE], verb,
                                                                       IMPERF, PASSIVE, passive_pres_con_ind)
            paratatikos[PASSIVE] = paratatikos_passive_forms
        all_forms['paratatikos'] = paratatikos

    # "act_pres_participle"
    if "act_pres_participle" in basic_forms:
        all_forms['act_pres_participle'] = basic_forms['act_pres_participle']

    # arch_act_pres_participle
    for participle_type in ['arch_act_pres_participle', 'active_aorist_participle', 'passive_aorist_participle']:
        if participle_type in basic_forms:
            all_possible_infl_forms = []


            if participle_type == 'arch_act_pres_participle':

                for participle in basic_forms[participle_type]:
                    res = create_all_adj_forms(participle)

                    all_possible_infl_forms.append(res[0])
            else:
                for participle in basic_forms[participle_type]:
                    res = create_all_adj_forms(participle)
                    if res[1]:
                        res = merging_all_dictionaries(res[0], res[1])
                    else:
                        res = res[0]
                    all_possible_infl_forms.append(res)


            all_forms[participle_type] = merging_all_dictionaries(*all_possible_infl_forms)

    # pass_pres_participle

    for participle_type in ['pass_pres_participle', 'passive_perfect_participle']:
        if participle_type in basic_forms:
            all_possible_infl_forms = []
            for participle in basic_forms[participle_type]:
                res = adjective.create_all(participle)[ADJ]
                all_possible_infl_forms.append(res)
            all_forms[participle_type] = merging_all_dictionaries(*all_possible_infl_forms)

    return all_forms
