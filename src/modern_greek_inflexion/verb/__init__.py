from icecream import ic

from .create.forms import create_all_imperfect_personal_forms, create_all_perf_non_past_personal_forms, \
    create_all_past_personal_forms
from modern_greek_inflexion.adjective.all.create_all_adj import create_all_adj_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries, dict_of_dicts_merge

from modern_greek_inflexion.verb.create.forms.basic.create_basic_all_forms import create_all_basic_forms
from modern_greek_accentuation.accentuation import convert_to_monotonic
from modern_greek_inflexion import adjective
from ..resources import PRES_CONJUGATION, ACT_PRES_PARTICIPLE, ARCH_ACT_PRES_PARTICIPLE, ACTIVE_AORIST_PARTICIPLE, \
    PASSIVE_AORIST_PARTICIPLE, PASS_PRES_PARTICIPLE, PASSIVE_PERFECT_PARTICIPLE, PARATATIKOS, PRESENT
from ..resources.resources import PRI, SEC, SG, PL, AORIST, ACTIVE, PASSIVE, IMP, CONJUNCTIVE, MODAL, IND, ADJ, PERF, \
    IMPERF
from modern_greek_inflexion.resources import greek_pattern
from modern_greek_inflexion._exceptions import NotInGreekException
import re


class Verb:

    def __init__(self, verb: str, para: bool = False, basic_forms: dict = None):
        if not greek_pattern.match(verb):
            raise NotInGreekException
        verb = convert_to_monotonic(verb, one_syllable_rule=False)
        self.verb = verb
        if not basic_forms:
            self.basic_forms = create_all_basic_forms(verb, para)
        else:
            self.basic_forms = basic_forms

        if 'error' in self.basic_forms:
            raise Exception(f"verb {self.verb} is incorrect, probably doesnt exist in the corpus")
        self.modal = self.basic_forms[MODAL]

    def create_imperfect_forms(self):
        result = {}
        active_pres_con_ind = passive_pres_con_ind = None
        present_basic_forms = self.basic_forms[PRESENT]
        present = {}

        if ACTIVE in present_basic_forms:
            # only here, because we have lemma situation, all possible conjugation are also created
            # (that is if you have τηλεφωνώ (άω), also forms from the τηλεφωνώ type are added
            pres_act_forms, active_pres_con_ind = create_all_imperfect_personal_forms(present_basic_forms[ACTIVE],
                                                                                      ACTIVE)
            present[ACTIVE] = pres_act_forms

        if PASSIVE in present_basic_forms:
            # here you can have more possible forms
            pres_passive_forms, passive_pres_con_ind = create_all_imperfect_personal_forms(present_basic_forms[PASSIVE],
                                                                                           PASSIVE)

            present[PASSIVE] = pres_passive_forms

            if ACTIVE not in present_basic_forms:
                deponens = True
        result[PRESENT] = present

        if PARATATIKOS in self.basic_forms:
            if self.verb == 'ανιώ':
                ic(result)
            pres_conjugation = self.basic_forms[PRES_CONJUGATION]
            paratatikos_basic_forms = self.basic_forms[PARATATIKOS]
            paratatikos = {}

            if ACTIVE in paratatikos_basic_forms:
                paratatikos_active_forms = create_all_past_personal_forms(paratatikos_basic_forms[ACTIVE], self.verb,
                                                                          IMPERF,
                                                                          ACTIVE, active_pres_con_ind)
                paratatikos[ACTIVE] = paratatikos_active_forms
            if PASSIVE in paratatikos_basic_forms:
                paratatikos_passive_forms = create_all_past_personal_forms(paratatikos_basic_forms[PASSIVE], self.verb,
                                                                           IMPERF, PASSIVE, passive_pres_con_ind)
                paratatikos[PASSIVE] = paratatikos_passive_forms
            result[PARATATIKOS] = paratatikos

        return result

    def create_conjunctive(self):

        # CONJUNCTIVE
        if CONJUNCTIVE in self.basic_forms:
            conjunctive_basic_forms = self.basic_forms[CONJUNCTIVE]
            conjunctive = {}
            active_roots = None

            if ACTIVE in conjunctive_basic_forms:
                con_active_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms[ACTIVE], ACTIVE)

                active_roots = [x[:-1] for x in conjunctive_basic_forms[ACTIVE]]

                conjunctive[ACTIVE] = con_active_forms

            if PASSIVE in conjunctive_basic_forms:

                con_passive_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms[PASSIVE], PASSIVE,
                                                                            active_root_for_imp=active_roots)

                if self.basic_forms[MODAL]:
                    del con_passive_forms[IMP]
                conjunctive[PASSIVE] = con_passive_forms

            return conjunctive
        else:
            return {}

    def create_aorist(self):
        if AORIST in self.basic_forms:
            aorist_basic_forms = self.basic_forms[AORIST]

            aorist = {}
            if ACTIVE in aorist_basic_forms:

                aor_active_forms = create_all_past_personal_forms(aorist_basic_forms[ACTIVE], self.verb, PERF, ACTIVE)
                if self.basic_forms[MODAL]:
                    aor_active_forms[IND].pop(PL, None)
                    aor_active_forms[IND][SG].pop(PRI, None)
                    aor_active_forms[IND][SG].pop(SEC, None)
                aorist[ACTIVE] = aor_active_forms
            if PASSIVE in aorist_basic_forms:
                aor_passive_forms = create_all_past_personal_forms(aorist_basic_forms[PASSIVE], self.verb, PERF,
                                                                   PASSIVE)
                aorist[PASSIVE] = aor_passive_forms

            return aorist
        else:
            return {}

    def create_participles(self):
        participles = {}
        if ACT_PRES_PARTICIPLE in self.basic_forms:
            participles[ACT_PRES_PARTICIPLE] = self.basic_forms[ACT_PRES_PARTICIPLE]

        # arch_act_pres_participle
        for participle_type in [PASSIVE_PERFECT_PARTICIPLE, PASS_PRES_PARTICIPLE,
                                ]:
            if participle_type in self.basic_forms:
                participles_of_type = []

                for participle in self.basic_forms[participle_type]:
                    # if self.verb == 'εγγράφω':
                    #     ic(participle_type, participle)
                    res = adjective.Adjective(participle).all()[ADJ]
                    participles_of_type.append(res)

                    participles[participle_type] = merging_all_dictionaries(*participles_of_type)
        for participle_type in [ARCH_ACT_PRES_PARTICIPLE, ACTIVE_AORIST_PARTICIPLE, PASSIVE_AORIST_PARTICIPLE, ]:
            if participle_type in self.basic_forms:
                participles_of_type = []
                for participle in self.basic_forms[participle_type]:
                    res = create_all_adj_forms(participle)

                    if participle_type != ARCH_ACT_PRES_PARTICIPLE and res[1]:
                        res = merging_all_dictionaries(res[0], res[1])
                    else:
                        res = merging_all_dictionaries(res[0], res[0])
                    participles_of_type.append(res)

                participles[participle_type] = merging_all_dictionaries(*participles_of_type)
        return participles

    def all(self):
        result = self.create_imperfect_forms()
        conjunctive = self.create_conjunctive()
        result[CONJUNCTIVE] = conjunctive
        aorist = self.create_aorist()
        result[AORIST] = aorist
        participles = self.create_participles()
        result.update(participles)
        return result


# def create_all_forms(verb: str, para: bool = False) -> dict:
#     """
#     **Create all verb forms in a dictionary form**
#
#     :param para: This flag is designed to deal with compound verbs with prefix "παρα" that can be two different verbs which differ only in perfective tenses and in a way they deal with augment (παραβλέπω - παράβλεψα != παραβλέπω - παραείδα)
#     :param verb: A verb should be put in first person sg present time active voice, if given in middle-passive voice, it will be treated as deponens. If given in 3rd person sg, it will be treated as a modal verb.
#     :return: a dictionary with all recognized forms
#
#     Usage:
#
#         .. code-block::
#
#                 from modern_greek_inflexion.verb import create_all_forms as verb_all
#                 from pprint import pprint
#
#                 pprint(verb_all('ξέρω')
#                 {'act_pres_participle': {'ξέροντας'},
#                  'aorist': {},
#                  'conjunctive': {},
#                  'paratatikos': {'active': {'ind': {'pl': {'pri': {'ξέραμε'},
#                                                            'sec': {'ξέρατε'},
#                                                            'ter': {'ξέρανε', 'ήξεραν'}},
#                                                     'sg': {'pri': {'ήξερα'},
#                                                            'sec': {'ήξερες'},
#                                                            'ter': {'ήξερε'}}}}},
#                  'present': {'active': {'imp': {'pl': {'sec': {'ξέρετε'}},
#                                                 'sg': {'sec': {'ξέρε'}}},
#                                         'ind': {'pl': {'pri': {'ξέρομε', 'ξέρουμε'},
#                                                        'sec': {'ξέρετε'},
#                                                        'ter': {'ξέρουν', 'ξέρουνε'}},
#                                                 'sg': {'pri': {'ξέρω'},
#                                                        'sec': {'ξέρεις', 'ξες'},
#                                                        'ter': {'ξέρει'}}}}}}
#
#
#
#
#
#     """
#     verb = convert_to_monotonic(verb, one_syllable_rule=False)
#     basic_forms = create_all_basic_forms(verb, para)
#
#     all_forms = {}
#
#     modal = basic_forms[MODAL]
#
#     "present"
#     present = {}
#     active_pres_con_ind = passive_pres_con_ind = None
#     if 'error' in basic_forms:
#         return {"error": f"verb {verb} is incorrect, probably doesnt exist in the corpus"}
#     present_basic_forms = basic_forms['present']
#
#     if ACTIVE in present_basic_forms:
#         # only here, because we have lemma situation, all possible conjugation are also created
#         # (that is if you have τηλεφωνώ (άω), also forms from the τηλεφωνώ type are added
#         pres_act_forms, active_pres_con_ind = create_all_imperfect_personal_forms(present_basic_forms[ACTIVE], ACTIVE)
#
#         present[ACTIVE] = pres_act_forms
#     if PASSIVE in present_basic_forms:
#         # here you can have more possible forms
#         pres_passive_forms, passive_pres_con_ind = create_all_imperfect_personal_forms(present_basic_forms[PASSIVE],
#                                                                                        PASSIVE)
#
#         present[PASSIVE] = pres_passive_forms
#
#         if ACTIVE not in present_basic_forms:
#             deponens = True
#
#     all_forms['present'] = present
#     # CONJUNCTIVE
#     if CONJUNCTIVE in basic_forms:
#         conjunctive_basic_forms = basic_forms[CONJUNCTIVE]
#         conjunctive = {}
#         active_roots = None
#
#         if ACTIVE in conjunctive_basic_forms:
#             con_active_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms[ACTIVE], ACTIVE)
#
#             active_roots = [x[:-1] for x in conjunctive_basic_forms[ACTIVE]]
#
#             conjunctive[ACTIVE] = con_active_forms
#
#         if PASSIVE in conjunctive_basic_forms:
#
#             con_passive_forms = create_all_perf_non_past_personal_forms(conjunctive_basic_forms[PASSIVE], PASSIVE,
#                                                                         active_root_for_imp=active_roots)
#
#             if basic_forms[MODAL]:
#                 del con_passive_forms[IMP]
#             conjunctive[PASSIVE] = con_passive_forms
#         all_forms[CONJUNCTIVE] = conjunctive
#
#     "aorist"
#     if AORIST in basic_forms:
#         aorist_basic_forms = basic_forms[AORIST]
#
#         aorist = {}
#         if ACTIVE in aorist_basic_forms:
#
#             aor_active_forms = create_all_past_personal_forms(aorist_basic_forms[ACTIVE], verb, PERF, ACTIVE)
#             if modal:
#                 aor_active_forms[IND].pop(PL, None)
#                 aor_active_forms[IND][SG].pop(PRI, None)
#                 aor_active_forms[IND][SG].pop(SEC, None)
#             aorist[ACTIVE] = aor_active_forms
#         if PASSIVE in aorist_basic_forms:
#             aor_passive_forms = create_all_past_personal_forms(aorist_basic_forms[PASSIVE], verb, PERF, PASSIVE)
#             aorist[PASSIVE] = aor_passive_forms
#
#         all_forms[AORIST] = aorist
#
#     # "paratatikos"
#     if 'paratatikos' in basic_forms:
#         paratatikos_basic_forms = basic_forms['paratatikos']
#         paratatikos = {}
#
#         if ACTIVE in paratatikos_basic_forms:
#             paratatikos_active_forms = create_all_past_personal_forms(paratatikos_basic_forms[ACTIVE], verb, IMPERF,
#                                                                       ACTIVE, active_pres_con_ind)
#             paratatikos[ACTIVE] = paratatikos_active_forms
#         if PASSIVE in paratatikos_basic_forms:
#             paratatikos_passive_forms = create_all_past_personal_forms(paratatikos_basic_forms[PASSIVE], verb,
#                                                                        IMPERF, PASSIVE, passive_pres_con_ind)
#             paratatikos[PASSIVE] = paratatikos_passive_forms
#         all_forms['paratatikos'] = paratatikos
#
#     # "act_pres_participle"
#     if "act_pres_participle" in basic_forms:
#         all_forms['act_pres_participle'] = basic_forms['act_pres_participle']
#
#     # arch_act_pres_participle
#     for participle_type in ['arch_act_pres_participle', 'active_aorist_participle', 'passive_aorist_participle']:
#         if participle_type in basic_forms:
#             all_possible_infl_forms = []
#
#             if participle_type == 'arch_act_pres_participle':
#
#                 for participle in basic_forms[participle_type]:
#                     res = create_all_adj_forms(participle)
#
#                     all_possible_infl_forms.append(res[0])
#                     # if verb == 'λέω':
#                     #     ic(all_possible_infl_forms)
#             else:
#                 for participle in basic_forms[participle_type]:
#                     res = create_all_adj_forms(participle)
#                     if res[1]:
#                         res = merging_all_dictionaries(res[0], res[1])
#                     else:
#                         res = res[0]
#                     all_possible_infl_forms.append(res)
#
#             all_forms[participle_type] = merging_all_dictionaries(*all_possible_infl_forms)
#
#     # pass_pres_participle
#
#     for participle_type in ['pass_pres_participle', 'passive_perfect_participle']:
#         if participle_type in basic_forms:
#             all_possible_infl_forms = []
#             for participle in basic_forms[participle_type]:
#                 # ic(participle)
#                 res = adjective.Adjective(participle).all()[ADJ]
#                 all_possible_infl_forms.append(res)
#             all_forms[participle_type] = merging_all_dictionaries(*all_possible_infl_forms)
#
#     return all_forms
