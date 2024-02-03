from __future__ import annotations

import sys
from modern_greek_accentuation.accentuation import put_accent_on_the_antepenultimate, remove_all_diacritics, \
    put_accent_on_the_penultimate, put_accent
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.syllabify import count_syllables

from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.variables import *
from modern_greek_inflexion.resources.verb import conjugations, irregular_imperative_forms
from modern_greek_inflexion.verb.create.forms.all.persons.create_imp_pass import create_imp_pass


def add_alternative_endings(forms: dict, con_name: str, root: str, accent_name: str | None) -> dict:
    endings = conjugations[con_name]
    for number in endings:
        for person in endings[number]:
            for ending in endings[number][person]:
                if accent_name:
                    form = put_accent(root + ending, accent_name, False)
                else:
                    form = root + ending
                forms[number][person].append(form)

    return forms


def create_all_pers_forms(conjugation_name: str, root: str, active_root: str | None = None,
                          deaugmented_root: str | None = None, simple_aor: bool = False) -> dict:
    """
    :param conjugation_name: conjugation name
    :param root: verb root
    :param active_root: if pass, for imp, should be given if it's a special case, should be an array
    :param deaugmented_root: root without augment
    :param simple_aor: sigmatic aorist
    :return:
    """

    forms = {}

    if not conjugation_name or conjugation_name in [MODAL, CON1_PASS_MODAL, CON2_PASS_MODAL]:
        return MODAL
    endings = conjugations[conjugation_name]

    if simple_aor:
        for number in endings.keys():
            forms[number] = {}
            for person in endings[number].keys():
                forms[number][person] = []
                for ending in endings[number][person]:

                    if deaugmented_root and count_syllables(ending) > 1:
                        form = put_accent_on_the_antepenultimate(deaugmented_root + ending, true_syllabification=False)

                        forms[number][person].append(form)
                        not_deaugmented_form = put_accent_on_the_antepenultimate(root + ending,
                                                                                 true_syllabification=False)
                        if not_deaugmented_form in greek_corpus:
                            forms[number][person].append(form)
                    else:
                        form = put_accent_on_the_antepenultimate(root + ending, true_syllabification=False)

                        forms[number][person].append(form)

                    if conjugation_name == ARCH_PASS_AOR and number == SG:
                        forms[number][person][0] = put_accent_on_the_penultimate(forms[number][person][0],
                                                                                 true_syllabification=False)

                    form_i_non_syllable = put_accent_on_the_antepenultimate(form)
                    if form_i_non_syllable != form and put_accent_on_the_antepenultimate(form) in greek_corpus:
                        forms[number][person].append(form_i_non_syllable)

    else:
        for number in endings.keys():
            forms[number] = {}
            for person in endings[number].keys():
                forms[number][person] = []
                for ending in endings[number][person]:
                    form = root + ending
                    if count_syllables(ending) == 2 and ending == remove_all_diacritics(ending):
                        form = put_accent_on_the_antepenultimate(form, true_syllabification=False)
                    elif count_syllables(form, true_syllabification=False) == 1:
                        form = remove_all_diacritics(form)
                    if ending == 'ει' and person == SEC:
                        form = put_accent_on_the_penultimate(form, true_syllabification=False)
                    forms[number][person].append(form)

    if conjugation_name == CON1_ACT:
        if root == 'θέλ':
            forms[SG][SEC].append('θες')
        elif root == 'ξέρ':
            forms[SG][SEC].append('ξες')
    elif conjugation_name == PARAT1_PASS:
        forms[PL][TER][0] = put_accent_on_the_antepenultimate(forms[PL][TER][0], true_syllabification=False)
        augmented_3_s = add_augment(root + 'ετο')
        augmented_3_s = [f for f in augmented_3_s if f in greek_corpus]
        forms[SG][TER].extend(augmented_3_s)
        augmented_3_p = add_augment(root + 'οντο')
        augmented_3_p = [f for f in augmented_3_p if f in greek_corpus]
        forms[PL][TER].extend(augmented_3_p)
    elif conjugation_name == PARAT2D_PASS:
        augmented_3_s = add_augment(forms[SG][TER][0])
        augmented_3_s = [f for f in augmented_3_s if f in greek_corpus]
        forms[SG][TER].extend(augmented_3_s)
        augmented_3_p = add_augment(forms[PL][TER][0])
        augmented_3_p = [f for f in augmented_3_p if f in greek_corpus]
        forms[PL][TER].extend(augmented_3_p)
    elif conjugation_name == PARAT2F_PASS:
        augmented_3_s = add_augment(root + 'ούτο')
        augmented_3_s = [f for f in augmented_3_s if f in greek_corpus]
        forms[SG][TER].extend(augmented_3_s)
        augmented_3_p = add_augment(root + 'ούντο')
        augmented_3_p = [f for f in augmented_3_p if f in greek_corpus]
        forms[PL][TER].extend(augmented_3_p)
    elif conjugation_name == PARAT2B_PASS:
        augmented_3_s = add_augment(root + 'είτο')
        augmented_3_s = [f for f in augmented_3_s if f in greek_corpus]
        forms[SG][TER].extend(augmented_3_s)
        augmented_3_p = add_augment(root + 'ούντο')
        augmented_3_p = [f for f in augmented_3_p if f in greek_corpus]
        forms[PL][TER].extend(augmented_3_p)
    elif conjugation_name == PARAT2A_PASS:
        augmented_3_s = add_augment(root + 'άτο')
        augmented_3_s = [f for f in augmented_3_s if f in greek_corpus]
        forms[SG][TER].extend(augmented_3_s)
        augmented_3_p = add_augment(root + 'ώντο')
        augmented_3_p = [f for f in augmented_3_p if f in greek_corpus]
        forms[PL][TER].extend(augmented_3_p)

    elif conjugation_name == CON1_PASS:
        forms[PL][PRI][0] = put_accent_on_the_antepenultimate(forms[PL][PRI][0])
        forms[PL][SEC][1] = put_accent_on_the_antepenultimate(forms[PL][SEC][1])
        if remove_all_diacritics(root) + 'όμεθα' in greek_corpus:
            forms = add_alternative_endings(forms, CON1_PASS_ARCHAIC, root, ANTEPENULTIMATE)

    elif conjugation_name == CON2A_PASS and root + 'ιούμαι' in greek_corpus:
        forms[SG][PRI].append(root + 'ιούμαι')

    elif conjugation_name == CON2B_PASS:
        if root + 'ούμεθα' in greek_corpus:
            forms = add_alternative_endings(forms, CON2B_PASS_ARCHAIC, root, None)


    # check if a verb in 2nd conjugation active has alternative endings belonging to other type of the 2nd con

    elif conjugation_name == CON2A_ACT:
        if root + 'είς' in greek_corpus and root + 'εί' in greek_corpus:
            forms = add_alternative_endings(forms, CON2B_ACT, root, None)

    elif conjugation_name == IMPER_ACT_CONT_2A:
        if root + 'είς' in greek_corpus and root + 'εί' in greek_corpus:
            forms = add_alternative_endings(forms, IMPER_ACT_CONT_2B, root, PENULTIMATE)

    elif conjugation_name == IMPER_PASS_AOR_A:
        if active_root and [ar for ar in active_root if ar[-1] in ['σ', 'ψ', 'ξ']]:
            forms[SG][SEC] = [x + "ου" for x in active_root if x[-1] in ['σ', 'ψ', 'ξ']]
        else:
            passive_aorist_recreated = create_imp_pass(root)

            forms[SG][SEC][0] = passive_aorist_recreated

    elif conjugation_name == CON2E_PASS:
        forms[PL][PRI][0] = put_accent_on_the_antepenultimate(forms[PL][PRI][0])
        forms[PL][PRI][1] = put_accent_on_the_antepenultimate(forms[PL][PRI][1])

    elif conjugation_name == CON2D_PASS:
        for number in forms.keys():
            for person in forms[number]:
                for index, form in enumerate(forms[number][person]):
                    forms[number][person][index] = put_accent_on_the_antepenultimate(form)


    if conjugation_name in [CON2B_ACT, CON2C_ACT, IMPER_ACT_AOR_C]:
        for number in forms.keys():
            for person in forms[number]:
                for index, form in enumerate(forms[number][person]):
                    if count_syllables(form, true_syllabification=False) == 1:
                        forms[number][person][index] = remove_all_diacritics(form)

    elif conjugation_name in [IMPER_ACT_CONT_1, IMPER_ACT_CONT_2C, IMPER_ACT_AOR_A, IMPER_ACT_AOR_B]:
        imper_2sg = put_accent_on_the_antepenultimate(forms[SG][SEC][0], true_syllabification=False)
        forms[SG][SEC][0] = imper_2sg
        form_i_non_syllable = put_accent_on_the_antepenultimate(imper_2sg)
        if imper_2sg != form_i_non_syllable and form_i_non_syllable in greek_corpus:
            forms[SG][SEC].append(form_i_non_syllable)

        if conjugation_name == IMPER_ACT_AOR_A:
            sec_pl = forms[PL][SEC][0]
            if sec_pl[-3:] not in ['στε', 'ψτε', 'ξτε']:
                if sec_pl not in greek_corpus:
                    forms[PL][SEC][0] = sec_pl[:-2] + 'ετε'



    elif conjugation_name in [IMPER_ACT_CONT_2A]:
        forms[SG][SEC][0] = put_accent_on_the_penultimate(forms[SG][SEC][0])
        if put_accent_on_the_antepenultimate(forms[SG][SEC][1]) in greek_corpus:

            forms[SG][SEC][1] = put_accent_on_the_antepenultimate(forms[SG][SEC][1])
        else:
            del forms[SG][SEC][1]
        if len(forms[SG][SEC]) == 3:
            forms[SG][SEC][2] = put_accent_on_the_penultimate(forms[SG][SEC][2])
        # accent
        if forms[SG][SEC][0] != put_accent_on_the_penultimate(forms[SG][SEC][0], true_syllabification=False):
            forms[SG][SEC].append(put_accent_on_the_penultimate(forms[SG][SEC][0], true_syllabification=False))


    elif conjugation_name in [IMPER_ACT_AOR_CA, IMPER_ACT_CONT_2B]:
        if root == 'ζ':
            forms[SG][TER] = ['ζήτω']
        forms[SG][SEC][0] = put_accent_on_the_penultimate(forms[SG][SEC][0], true_syllabification=False)
        if len(forms[SG][SEC]) == 3:
            forms[SG][SEC][1] = put_accent_on_the_penultimate(forms[SG][SEC][1])
            forms[SG][SEC][2] = put_accent_on_the_antepenultimate(forms[SG][SEC][2])

    #### irregular imperatives
    if conjugation_name.startswith('imper'):

        if root in irregular_imperative_forms:
            for number in irregular_imperative_forms[root]:
                for person in irregular_imperative_forms[root][number]:
                    irregular_form = irregular_imperative_forms[root][number][person]
                    try:
                        forms[number][person].append(irregular_form)
                        if root == 'πά':
                            # a sketchy way to deal with pao, but no other way I see
                            forms[number][person] = [irregular_form]
                        # in this case check validity of all imperative forms
                        forms[number][person] = [form for form in forms[number][person] if form in greek_corpus]
                    except:
                        print(sys.exc_info()[0])
                        raise Exception

    return forms
