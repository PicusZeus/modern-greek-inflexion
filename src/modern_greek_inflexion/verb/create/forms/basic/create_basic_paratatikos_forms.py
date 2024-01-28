from __future__ import annotations

from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, put_accent_on_the_antepenultimate, \
    remove_all_diacritics
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.resources import vowels, prefixes_before_augment
from modern_greek_accentuation.syllabify import count_syllables

from modern_greek_inflexion.resources import CON1_ACT, CON2A_ACT, CON2A_ACT_LOGIA, CON2B_ACT, CON2D_ACT, CON2C_ACT, \
    EIMAI, greek_corpus, CON2E_PASS, CON2D_PASS, CON2B_PASS, CON2A_PASS, CON1_PASS, CON2C_PASS, CON2AB_PASS, CON2SA_PASS
from modern_greek_inflexion.resources.verb import irregular_active_paratatikos, irregular_passive_paratatikos


def create_basic_paratatikos_forms(pres_form: str, root: str, pres_conjugation: str, deponens: bool = False,
                                   not_deponens: bool = True, modal_act: bool = False,
                                   modal_med: bool = False, has_passive: bool = True,
                                   alternative: bool = False) -> str | None:
    paratatikos_basic_forms = None

    if not_deponens:
        act_par, pass_par = [], []

        for ir_verb in irregular_active_paratatikos:
            length_ir_verb = len(ir_verb)
            if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
                act_par.extend(add_augment(pres_form[:-length_ir_verb] + irregular_active_paratatikos[ir_verb]))

        if pres_form == 'πάω':
            pass
        elif pres_conjugation == CON1_ACT:
            not_augmented_par = put_accent_on_the_antepenultimate(root + 'α')

            if not alternative:
                act_par.extend(add_augment(not_augmented_par))

            act_par = [f for f in act_par if not (count_syllables(
                f, true_syllabification=False) == 2 and f[0] not in vowels)]

            pass_par = [put_accent_on_the_penultimate(root + 'όμουν')]

        elif pres_conjugation == CON2A_ACT:
            act_par = [root + 'ούσα']
            par_ga = put_accent_on_the_antepenultimate(root + 'αγα')
            if count_syllables(par_ga, true_syllabification=False) > 2:
                act_par.append(par_ga)

            pass_par = [root + 'ιόμουν']
            if root + 'όμην' in greek_corpus:
                pass_par.append(root + 'όμην')

        elif pres_conjugation == CON2A_ACT_LOGIA:
            act_par = [root + 'ούσα']
            pass_par = [root + 'όμουν']
            if root + 'άμην' in greek_corpus or root + 'άτο' in greek_corpus:
                pass_par.append(root + 'άμην')


        elif pres_conjugation in [CON2B_ACT, CON2D_ACT]:
            act_par = [root + 'ούσα']
            pass_par = [root + 'ούμουν']
            if pres_conjugation == CON2B_ACT and root[-1] == 'ι':
                if root + 'ούμουν' in greek_corpus:
                    pass_par.append(root + 'όμουν')
                elif has_passive:
                    pass_par = [root + 'όμουν']

        elif pres_conjugation == CON2C_ACT:
            not_augmented_par = root + 'γα'
            act_par = add_augment(not_augmented_par)
            pass_par = [put_accent_on_the_penultimate(root + 'γόμουν')]

        elif pres_conjugation == EIMAI:
            act_par = [root + 'ήμουν']

        act_par_all = [f for f in act_par if f in greek_corpus]

        if pres_conjugation == EIMAI:
            act_par_all = [root + 'ήμουν']
        if not act_par_all:

            act_par_all_3rd = [f for f in act_par if f[:-1] + 'ε' in greek_corpus]
            if act_par_all_3rd:
                act_par_all = [f[:-1] + 'α' for f in act_par_all_3rd]
        if not act_par_all and pres_conjugation == CON1_ACT:
            if pres_form.endswith('βαίνω') and pres_form[:-5] in prefixes_before_augment:
                act_par_all.append(prefixes_before_augment[pres_form[:-5]] + 'έβαινα')
            elif count_syllables(root) == 1 and not root[0] in ['έ', 'ά', 'ε', 'α']:
                act_par_all.append(put_accent_on_the_antepenultimate('έ' + root + 'α'))
            elif pres_form.endswith('έχω') and pres_form[:-3] in prefixes_before_augment.keys() or pres_form[:-3] in [
                'ισαπ']:
                # συνέθετα του έχω
                act_par_all.append(pres_form[:-3] + 'είχα')
            else:
                act_par_all.append(put_accent_on_the_antepenultimate(root + 'α'))
        elif not act_par_all and pres_conjugation in [CON2A_ACT, CON2B_ACT, CON2A_ACT_LOGIA, CON2D_ACT]:
            act_par_all.append(put_accent_on_the_penultimate(root + 'ούσα'))

        elif not act_par_all and pres_conjugation == CON2C_ACT:
            if count_syllables(root) > 1 and root[0] not in vowels:
                act_par_all.append(put_accent_on_the_antepenultimate(root + 'γα'))
            else:
                act_par_all.append(put_accent_on_the_antepenultimate('ε' + root + 'γα'))
        elif not act_par_all:
            ic(pres_form, pres_conjugation)
        if pres_form in irregular_active_paratatikos:
            act_par_all = [irregular_active_paratatikos[pres_form]]

        if not has_passive:
            pass_par = []
        act_par = ','.join(act_par_all)

        pass_par = ','.join(pass_par)


        paratatikos = '/'.join([act_par, pass_par])
        if root[-3:] == 'ποι':
            paratatikos = root + 'ούσα/' + root + 'ούμουν' + ',' + root + 'όμουν'

        paratatikos_basic_forms = paratatikos

    elif deponens:
        pass_par = []
        root = remove_all_diacritics(root)
        if pres_form in irregular_passive_paratatikos:
            pass_par = [irregular_passive_paratatikos[pres_form]]

        elif pres_conjugation == CON1_PASS:
            pass_par = [root + 'όμουν']
        elif pres_conjugation == CON2A_PASS:
            pass_par = [root + 'ιόμουν', root + 'ούμουν', root + 'όμουν']
            pass_par = [f for f in pass_par if f in greek_corpus]
            if not pass_par:
                pass_par = [root + 'ιόμουν']
        elif pres_conjugation == CON2SA_PASS:
            pass_par = [root + 'ούμουν']
        elif pres_conjugation == CON2B_PASS:
            pass_par = [root + 'ούμουν', root + 'ιόμουν']
            pass_par = [f for f in pass_par if f in greek_corpus]
            if not pass_par:
                pass_par = [root + 'ούμουν']
        elif pres_conjugation in [CON2C_PASS, CON2AB_PASS]:
            pass_par = [root + 'όμουν']
            alt_pass_par = root + 'ιόμουν'
            if alt_pass_par in greek_corpus:
                pass_par.append(alt_pass_par)
        elif pres_conjugation == CON2D_PASS:
            pass_par = [put_accent_on_the_penultimate(root + 'μην'), root[:-1] + 'όμουν', root + 'όμουν']
            pass_par.extend(add_augment(pass_par[0]))
            pass_par = [f for f in pass_par if f in greek_corpus]
            if not pass_par and pres_form.endswith('ειμαι'):
                pass_par = [put_accent_on_the_antepenultimate(root + 'το')]
        elif pres_conjugation == CON2E_PASS:
            pass_par = [root + 'άμην', root + 'όμουν']
            pass_par = [f for f in pass_par if f in greek_corpus]

        pass_par = set(pass_par)
        pass_par = ','.join(pass_par)
        # if root[-3:] == 'ποι':
        #     pass_par = root + 'ούμουν,' + root + 'όμουν'
        paratatikos_basic_forms = '/' + pass_par

    elif modal_act:
        parat_act_forms = []
        if pres_form[-3:] == 'άει':
            parat_act_forms = add_augment(pres_form[:-3] + 'ούσε')
            parat_act_forms.extend(add_augment(pres_form[:-3] + 'αγε'))
        elif pres_form[-3:] == 'ά':
            parat_act_forms = add_augment(pres_form[:-1] + 'ούσε')
            parat_act_forms.extend(add_augment(pres_form[:-1] + 'γε'))
        elif pres_form[-2:] == 'ει':
            parat_act_forms = add_augment(pres_form[:-2] + 'ε')
        elif pres_form[-2:] == 'εί':
            parat_act_forms = add_augment(pres_form[:-2] + 'ούσε')

        parat_act_forms = [f for f in parat_act_forms if f in greek_corpus]
        parat_act_forms = ','.join(parat_act_forms)

        paratatikos_basic_forms = parat_act_forms + '/'

    elif modal_med:
        parat_med_forms = ''
        if pres_form[-5:] == 'ιέται':
            parat_med_forms = [root + 'ιόταν']

        elif pres_form[-5:] == 'είται':
            parat_med_forms = add_augment(root + 'είτο')
            parat_med_forms.extend([root + 'ούνταν'])

        elif pres_form[-4:] == 'άται':
            parat_med_forms = [root + 'άτο', root + 'όταν', root + 'ιόταν']

        elif pres_form[-4:] == 'εται':
            parat_med_forms = [put_accent_on_the_penultimate(root + 'όταν'), root + 'ετο']
        elif pres_form[-5:] == 'ειται':
            parat_med_forms = [root + 'ειτο']
            parat_med_forms.extend(add_augment(parat_med_forms[0]))
            parat_med_forms = [put_accent_on_the_antepenultimate(v) for v in parat_med_forms]

        parat_med_forms = [f for f in parat_med_forms if f in greek_corpus]
        parat_med_forms = ','.join(parat_med_forms)
        paratatikos_basic_forms = '/' + parat_med_forms

    return paratatikos_basic_forms
