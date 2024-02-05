from __future__ import annotations

from modern_greek_accentuation.accentuation import (put_accent_on_the_penultimate,
                                                    put_accent_on_the_antepenultimate)
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.resources import vowels
from modern_greek_accentuation.syllabify import count_syllables

from modern_greek_inflexion.resources import CON1_ACT, CON2A_ACT, CON2AK_ACT, CON2B_ACT, CON2D_ACT, CON2C_ACT, \
    EIMAI, greek_corpus
from modern_greek_inflexion.resources.verb import irregular_active_paratatikos, prefixes_before_augment


def active_paratatikos_exists(f_p: str) -> bool:
    th_pl = f_p[:-1] + 'αν'
    sec_sg = f_p[:-1] + 'ες'

    return f_p in greek_corpus or th_pl in greek_corpus or sec_sg in greek_corpus


def create_basic_paratatikos_active(pres_form: str, root: str, pres_conjugation: str,
                                    modal: bool = False) -> str | None:

    act_par = []
    if pres_form in irregular_active_paratatikos:
        return irregular_active_paratatikos[pres_form]

    for ir_verb in irregular_active_paratatikos:
        length_ir_verb = len(ir_verb)
        if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
            prefix = pres_form[:-length_ir_verb]
            act_par.extend(add_augment(prefix + irregular_active_paratatikos[ir_verb]))

    if not modal:
        if pres_conjugation == CON1_ACT:
            not_augmented_par = put_accent_on_the_antepenultimate(root + 'α')

            augmented_par = (add_augment(not_augmented_par))
            if pres_form.endswith('ρω'):
                act_par.append(pres_form[:-1] + 'ιζα')

            augmented_par = [f for f in augmented_par if not (count_syllables(
                f, true_syllabification=False) == 2 and f[0] not in vowels)]
            act_par.extend(augmented_par)

        elif pres_conjugation == CON2A_ACT:
            act_par.append(root + 'ούσα')
            par_ga = put_accent_on_the_antepenultimate(root + 'αγα')
            if count_syllables(par_ga, true_syllabification=False) > 2:
                act_par.append(par_ga)

        elif pres_conjugation in [CON2B_ACT, CON2D_ACT, CON2AK_ACT]:
            act_par.append(root + 'ούσα')

        elif pres_conjugation == CON2C_ACT:
            augmented_par = add_augment(root + 'γα')
            act_par.extend(augmented_par)

        elif pres_conjugation == EIMAI:
            act_par = [root + 'ήμουν']

        act_par_all = [f for f in act_par if active_paratatikos_exists(f)]

        if pres_form.endswith('άρω'):
            act_par_all.append(put_accent_on_the_antepenultimate(root + 'α'))

        if not act_par_all:

            if pres_conjugation == CON1_ACT:
                if pres_form.endswith('βαίνω') and pres_form[:-5] in prefixes_before_augment:
                    act_par_all.append(prefixes_before_augment[pres_form[:-5]] + 'έβαινα')
                elif count_syllables(root) == 1 and not root[0] in ['έ', 'ά', 'ε', 'α']:
                    act_par_all.append(put_accent_on_the_antepenultimate('έ' + root + 'α'))
                elif pres_form.endswith('έχω') and pres_form[:-3] in prefixes_before_augment or pres_form[:-3] in [
                    'ισαπ']:
                    # συνέθετα του έχω
                    act_par_all.append(pres_form[:-3] + 'είχα')
                else:
                    act_par_all.append(put_accent_on_the_antepenultimate(root + 'α'))
            elif pres_conjugation in [CON2A_ACT, CON2B_ACT, CON2AK_ACT, CON2D_ACT]:
                act_par_all.append(put_accent_on_the_penultimate(root + 'ούσα'))

            elif not act_par_all and pres_conjugation == CON2C_ACT:
                if count_syllables(root) > 1 and root[0] not in vowels:
                    act_par_all.append(put_accent_on_the_antepenultimate(root + 'γα'))
                else:
                    act_par_all.append(put_accent_on_the_antepenultimate('ε' + root + 'γα'))
            elif pres_conjugation == EIMAI:
                act_par_all = [root + 'ήμουν']

    else:
        # if modal
        if pres_form[-3:] == 'άει':
            act_par.append(pres_form[:-3] + 'ούσε')
            act_par.append(put_accent_on_the_antepenultimate(pres_form[:-3] + 'αγε'))

        elif pres_form[-3:] == 'ά':
            act_par.append(pres_form[:-1] + 'ούσε')
        elif pres_form.endswith('ει'):
            act_par.extend(add_augment(pres_form[:-2] + 'ε'))
        elif pres_form[-2:] == 'εί':
            act_par.append(pres_form[:-2] + 'ούσε')

        act_par_all = [f for f in act_par if f in greek_corpus]

    if act_par_all:
        return ','.join(act_par_all)
