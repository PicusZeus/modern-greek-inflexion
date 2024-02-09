from __future__ import annotations

import unicodedata

from copy import deepcopy
from modern_greek_accentuation.resources import vowels, diphtongs
from modern_greek_accentuation.syllabify import count_syllables
from modern_greek_accentuation.accentuation import put_accent_on_syllable, DIAERESIS, put_accent_on_the_antepenultimate, \
    where_is_accent
from modern_greek_inflexion.resources import greek_corpus, IMP, MODAL


def dict_of_dicts_merge(x: dict | set | str, y: dict | set | str) -> dict | set:
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
    new_dict = {}
    for key, item in verb_temp.items():
        if isinstance(item, set):
            new_set = set()
            for form in item:
                if count_syllables(form) == 1 and not where_is_accent(form):
                    form = put_accent_on_syllable(form)

                if form[0] in vowels:
                    if prefix[1][-1] + form[0] in diphtongs:
                        vowel_with_diaeresis = unicodedata.normalize("NFC", form[0] + DIAERESIS)
                        form = vowel_with_diaeresis + form[1:]

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


def merging_all_dictionaries(*dicts) -> dict | list[dict]:
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
    :param perf_root:
    :return:
    """
    if perf_root.startswith('εξ') and len(perf_root) > 5:
        perf_root = perf_root[2:]
    first_person = perf_root + 'ω'
    third_person = perf_root + 'ει'

    return first_person in greek_corpus or third_person in greek_corpus


def active_subjunctive_sigmatic_exists(perf_root) -> bool:
    if perf_root.startswith('εξ') and len(perf_root) > 5:
        perf_root = perf_root[2:]
    first_person = perf_root + 'ω'
    third_person = perf_root + 'ει'
    imperative = perf_root + 'ου'
    return first_person in greek_corpus or third_person in greek_corpus or imperative in greek_corpus


def compound_alternative_forms(forms: None | dict, sec_pos: str, forms_ind_or_con: dict,
                               forms_imp: dict | None) -> dict:
    """
    compound all alternative forms into a set
    :return:
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
    return first_p in greek_corpus or third_p in greek_corpus
