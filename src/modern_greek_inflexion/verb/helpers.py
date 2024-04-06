from __future__ import annotations

import unicodedata

from copy import deepcopy
from modern_greek_accentuation.resources import vowels, diphtongs
from modern_greek_accentuation.syllabify import count_syllables
from modern_greek_accentuation.accentuation import put_accent_on_syllable, DIAERESIS, put_accent_on_the_antepenultimate, \
    where_is_accent
from modern_greek_inflexion.resources import greek_corpus, IMP, MODAL, PRES_CONJUGATION


def dict_of_dicts_merge(x: dict | set | str, y: dict | set | str) -> dict | set:
    """
    Helping function for merging two values of two dictionaries into another dictionary or a set
    :param x: dictionary or set or str
    :param y: dictionary or set or str
    :return: dictionary or set
    """
    z = {}
    if isinstance(x, set):
        if isinstance(y, set):
            x.update(y)
            return x
        elif isinstance(y, str):
            y = set(y.split(','))
            x.update(y)
        return x
    elif isinstance(x, str):
        x = set(x.split(','))
        if isinstance(y, str):
            y = set(y.split(','))
        x.update(y)
        return x
    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        z[key] = dict_of_dicts_merge(x[key], y[key])
    for key in x.keys() - overlapping_keys:
        z[key] = deepcopy(x[key])
    for key in y.keys() - overlapping_keys:
        z[key] = deepcopy(y[key])
    if not z:
        raise ValueError
    return z


def update_forms_with_prefix(verb_temp: dict, prefix: [str, str]) -> dict:
    """
    Helping function for adding previously detached prefix to inflected forms
    :param verb_temp: a dictionary with basic forms
    :param prefix: a list with first element a prefix before consonant and second before vowel
    :return: a dictionary with basic forms
    """
    new_dict = {}
    for key, item in verb_temp.items():
        if key == PRES_CONJUGATION:
            new_dict[PRES_CONJUGATION] = verb_temp[PRES_CONJUGATION]
        elif isinstance(item, set):
            new_set = set()
            for form in item:
                if count_syllables(form) == 1 and not where_is_accent(form):
                    form = put_accent_on_syllable(form)

                if form[0] in vowels:
                    if prefix[1][-1] + form[0] in diphtongs:
                        vowel_with_diaeresis = unicodedata.normalize("NFC", form[0] + DIAERESIS)
                        form = '/'.join(vowel_with_diaeresis + f[1:] for f in form.split('/'))

                    new_form = '/'.join([prefix[1] + f for f in form.split('/')])
                else:
                    new_form = '/'.join([prefix[0] + f for f in form.split('/')])

                new_set.add(new_form)

            new_dict[key] = new_set
        elif isinstance(item, dict):

            new_dict[key] = update_forms_with_prefix(item, prefix)
        elif isinstance(item, str):
            # 'ων/ούσα/ον'
            new_dict[key] = '/'.join([prefix + f for f in item.split('/')])
        else:
            new_dict[key] = item
    return new_dict


def merging_all_dictionaries(*dicts: dict) -> dict | list[dict]:
    """
    A helping function for merging two or more dictionaries of the same structure into one dictionary
    :param dicts: dictionaries of the same structure
    :return: a dictionary with merged values
    """
    if len(dicts) > 2:
        first = dicts[0]
        second = dicts[1]
        rest = dicts[2:]
        merged = dict_of_dicts_merge(first, second)
        return merging_all_dictionaries(merged, *rest)

    else:
        if len(dicts) == 2:

            merged = dict_of_dicts_merge(*dicts)
            result = dict_of_dicts_merge(merged, merged)
            if not result:
                raise ValueError

            # merging_all_dictionaries(res)
        else:

            result = merging_all_dictionaries(dicts[0], dicts[0])
            if not result:
                raise ValueError

        return result


def passive_subjunctive_exists(perf_root: str) -> bool:
    """
    Helping function for checking if a supposed perfect root actually exists in the language corpus
    :param perf_root: a perfect passive root (without any ending), like "ετοιμαστ"
    :return: True or False
    """
    first_person = perf_root + 'ώ'
    third_person = perf_root + 'εί'
    first_person_aor = put_accent_on_the_antepenultimate(perf_root + 'ηκα')
    perf_past_participle = perf_root[:-1] + 'μένος'
    if perf_root[-2] not in vowels and perf_root.endswith('θ'):
        perf_past_participle = perf_root + 'μένος'
    return (first_person in greek_corpus or
            third_person in greek_corpus or
            perf_past_participle in greek_corpus or
            first_person_aor in greek_corpus)


def aorist_exists(aorist: str) -> bool:
    """
    Helping function that checks if a supposed aorist form actually exists in the language corpus
    :param aorist: first person sg of an aorist form
    :return: True or False
    """
    f_pers = aorist
    s_pers = aorist[:-1] + 'ες'
    th_pers = aorist[:-1] + 'ε'
    if not aorist.endswith('ηκα'):
        th_pers = aorist[:-1] + 'αν'
    if f_pers.endswith('η'):
        f_pers = aorist + 'ν'
        s_pers = aorist
        th_pers = aorist
    return f_pers in greek_corpus or s_pers in greek_corpus or (th_pers in greek_corpus and count_syllables(th_pers) > 2)


def active_subjunctive_exists(perf_root: str) -> bool:
    """
    Helping function for checking if a supposed active root actually exists in the language corpus
    :param perf_root: an aorist/perfect stem (like 'κατεβ')
    :return: True or False
    """
    if perf_root.startswith('εξ') and len(perf_root) > 5:
        perf_root = perf_root[2:]
    first_person = perf_root + 'ω'
    third_person = perf_root + 'ει'

    return first_person in greek_corpus or third_person in greek_corpus


def active_subjunctive_sigmatic_exists(perf_root, pres_form) -> bool:
    """
    Helping function for checking if a supposed active root actually exists in the language corpus applicable only
    for sigmatic stems
    :param perf_root: an aorist/perfect stem (like 'αγοράσ')
    :return: True or False
    """
    if perf_root.startswith('εξ') and len(perf_root) > 5:
        perf_root = perf_root[2:]
    first_person = perf_root + 'ω'
    third_person = perf_root + 'ει'
    if pres_form.endswith('μαι'):
        imperative = perf_root + 'ου'
    else:
        imperative = first_person
    return first_person in greek_corpus or third_person in greek_corpus or imperative in greek_corpus


def compound_alternative_forms(forms: None | dict, sec_pos: str, forms_ind_or_con: dict,
                               forms_imp: dict | None) -> dict:

    """
    A helping function for merging with a dictionary of forms of a single tense alternative forms supplied as
    forms_ind_or_con and forms_imp. If the main forms is actually None, it merges into a dictionary of forms
    indicative and imperative forms
    :param forms: A dictionary with forms of a single tense with indicative/conjunctive forms
    and imperative forms if they exist
    :param sec_pos: A str with a value indicating a tense
    :param forms_ind_or_con: A dictionary with indicative or conjunctive forms
    :param forms_imp: A dictionary with imperative forms if exists
    :return: A merged dictionary
    """

    if not forms:
        if forms_imp:
            forms = {sec_pos: forms_ind_or_con, IMP: forms_imp}
        else:
            forms = {sec_pos: forms_ind_or_con}
    else:
        if forms_imp:
            new_forms = {sec_pos: forms_ind_or_con, IMP: forms_imp}
        else:
            new_forms = {sec_pos: forms_ind_or_con}
        for pos in forms:
            for number in forms[pos]:
                for person in forms[pos][number]:
                    old = forms[pos][number][person]
                    try:
                        new = new_forms[pos][number][person]
                    except KeyError:
                        new = []

                    new.extend(old)
                    forms[pos][number][person] = new

    if forms_ind_or_con == MODAL:
        return forms

    for pos in forms:
        for number in forms[pos]:
            for person in forms[pos][number]:
                old = forms[pos][number][person]
                new = set(old)
                forms[pos][number][person] = new

    return forms


def check_personal_forms(first_p: str, third_p: str) -> bool:
    """
    A helping function that checks if first or third person sg exist in the language corpus
    :param first_p: First person sg of a verb
    :param third_p: Third person sg of a verb
    :return: True or False
    """
    return first_p in greek_corpus or third_p in greek_corpus
