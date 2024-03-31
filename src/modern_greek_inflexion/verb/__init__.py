
from .create.forms import create_all_present_personal_forms, create_all_subjunctive_personal_forms, \
    create_all_past_personal_forms
from modern_greek_inflexion.adjective.all.create_all_adj import create_all_adj_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries, dict_of_dicts_merge

from modern_greek_inflexion.verb.create.forms.basic.create_basic_all_forms import create_all_basic_forms
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..resources.typing import basic_forms_type, voice_forms_imp_type, voice_forms_type, participles_type, \
    genders_declensions_type
from ..resources.variables import *
from modern_greek_inflexion.resources import greek_pattern
from modern_greek_inflexion.exceptions import NotInGreekException


class Verb:
    """
    This class can be used to generate all or certain groups of inflected verbal forms

    :param verb: It has to be a lemma like form, that is the first person singular of present tense, or, if it's a modal verb, the third person singular.
    :type verb: str
    :param para: there is a problem with prefix 'παρα', which can mean two very different things and so a verb prefixed with it, which can also influence the inflected forms a given verb generates. Generally speaking when 'παρα' has a rough meaning of "too much", or "in very high frequency" a verb with such prefix tends to be fully detachable (that is the prefix does not influence inflexion". But if 'παρα' derives its meaning from the ancient preposition πάρα, that rougly meansy "from above" or "from some distance" a verb can behave differently in regards of the augment and perfect forms (vide παραβλέπω - overlook and παραβλέπω - meet someone/ see sth too often). As the program is unable to predict which verb to conjugate, you can tell it by setting this flag to True, if the prefix para is detachable (that is its meaning is roughly "too much"). It defaults to False.
    :type para: bool, optional
    :param basic_forms: If you have already generated basic verb forms, you can supply them. These have to be of the following shape: ``{ACT_PRES_PARTICIPLE: set[str], ACTIVE_AORIST_PARTICIPLE: set[str], AORIST: dict[ACTIVE: set[str],  PASSIVE: set[str]], ARCH_ACT_PRES_PARTICIPLE: set[str], CONJUNCTIVE: dict[ACTIVE: set[str], PASSIVE: set[str]], PRES_CONJUGATION: str, PARATATIKOS: dict[ACTIVE: set[str], PASSIVE: set[str]], PASSIVE_AORIST_PARTICIPLE: set[str], PASSIVE_PERFECT_PARTICIPLE: set[str], PRESENT: dict[ACTIVE: set[str], PASSIVE: set[str]]}``
    :type basic_forms: dict, optional
    """

    def __init__(self, verb: str, para: bool = False, basic_forms: basic_forms_type = None):

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

    def create_imperfect_forms(self) -> {PRESENT: voice_forms_imp_type, PARATATIKOS: voice_forms_type}:
        """
        This method can be used to create imperfect tenses, that is present tense and paratatiko inflected forms.

        :return: A dictionary of the following shape ``{PRESENT: ACTIVE: {IND: personal_forms_type, IMP: personal_forms_type}, PASSIVE: {IND: personal_forms_type, IMP: personal_forms_type}, PARATATIKOS: ACTIVE: {IND: personal_forms_type}, PASSIVE: {IND: personal_forms_type}}``
        :rtype: dict
        """
        result = {}
        active_pres_con_ind = passive_pres_con_ind = None
        present_basic_forms = self.basic_forms[PRESENT]
        present = {}

        if ACTIVE in present_basic_forms:
            # only here, because we have lemma situation, all possible conjugation are also created
            # (that is if you have τηλεφωνώ (άω), also forms from the τηλεφωνώ type are added
            pres_act_forms, active_pres_con_ind = create_all_present_personal_forms(present_basic_forms[ACTIVE],
                                                                                    ACTIVE)
            present[ACTIVE] = pres_act_forms

        if PASSIVE in present_basic_forms:
            # here you can have more possible forms
            pres_passive_forms, passive_pres_con_ind = create_all_present_personal_forms(present_basic_forms[PASSIVE],
                                                                                         PASSIVE)

            present[PASSIVE] = pres_passive_forms

            if ACTIVE not in present_basic_forms:
                deponens = True
        result[PRESENT] = present

        if PARATATIKOS in self.basic_forms:

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

    def create_conjunctive(self) -> voice_forms_imp_type:
        """
        This method can be used to generate subjunctive forms and simple imperative

        :return: A dictionary of the following shape ``{ACTIVE: {IND: personal_forms_type, IMP: personal_forms_type}, PASSIVE: {IND: personal_forms_type, IMP: personal_forms_type}``
        :rtype: dict
        """

        # CONJUNCTIVE
        if CONJUNCTIVE in self.basic_forms:
            conjunctive_basic_forms = self.basic_forms[CONJUNCTIVE]
            conjunctive = {}
            active_roots = None

            if ACTIVE in conjunctive_basic_forms:
                con_active_forms = create_all_subjunctive_personal_forms(conjunctive_basic_forms[ACTIVE], ACTIVE)

                active_roots = [x[:-1] for x in conjunctive_basic_forms[ACTIVE]]

                conjunctive[ACTIVE] = con_active_forms

            if PASSIVE in conjunctive_basic_forms:

                con_passive_forms = create_all_subjunctive_personal_forms(conjunctive_basic_forms[PASSIVE], PASSIVE,
                                                                          active_root_for_imp=active_roots)

                if self.basic_forms[MODAL]:
                    del con_passive_forms[IMP]
                conjunctive[PASSIVE] = con_passive_forms

            return conjunctive
        else:
            return {}

    def create_aorist(self) -> voice_forms_type:
        """
        This method can be used to generate aorist forms.

        :return: A dictionary with the following shape: ``{ACTIVE: {IND: personal_forms_type}, PASSIVE: {IND: personal_forms_type}``
        :rtype: dict
        """
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

    def create_participles(self) -> participles_type:
        """
        this method creates all participle types (if a given verb actually does create them)

        :return: A dictionary with the following keys ``ACT_PRES_PARTICIPLE, ARCH_ACT_PRES_PARTICIPLE, PASSIVE_PERFECT_PARTICIPLE, PASS_PRES_PARTICIPLE, ACTIVE_AORIST_PARTICIPLE, PASSIVE_AORIST_PARTICIPLE``. The present active participle is adverbial, so under this key you will find only a single form, the rest participles create adjectival forms, and so they are of the following shape ``{SG: {MASC: {NOM: set(forms), ...}, ...}, ...}``.
        :rtype: dict
        """
        participles = {}
        if ACT_PRES_PARTICIPLE in self.basic_forms:
            participles[ACT_PRES_PARTICIPLE] = self.basic_forms[ACT_PRES_PARTICIPLE]

        for participle_type in [ARCH_ACT_PRES_PARTICIPLE, PASSIVE_PERFECT_PARTICIPLE, PASS_PRES_PARTICIPLE,
                                ACTIVE_AORIST_PARTICIPLE, PASSIVE_AORIST_PARTICIPLE]:
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

    def all(self) -> {PRESENT: voice_forms_imp_type, CONJUNCTIVE: voice_forms_imp_type, PARATATIKOS: voice_forms_type, AORIST: voice_forms_type, ARCH_ACT_PRES_PARTICIPLE: genders_declensions_type, PASSIVE_PERFECT_PARTICIPLE: genders_declensions_type, PASS_PRES_PARTICIPLE: genders_declensions_type, ACTIVE_AORIST_PARTICIPLE: genders_declensions_type, PASSIVE_AORIST_PARTICIPLE: genders_declensions_type, ACT_PRES_PARTICIPLE: set[str]}:
        """
        This method will create all inflected forms

        :return: A dictionary with personal forms and with participles
        :rtype: dict
        """
        result = self.create_imperfect_forms()
        conjunctive = self.create_conjunctive()
        result[CONJUNCTIVE] = conjunctive
        aorist = self.create_aorist()
        result[AORIST] = aorist
        participles = self.create_participles()
        result.update(participles)
        return result
