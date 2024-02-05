from __future__ import annotations

from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, put_accent_on_the_antepenultimate, \
    remove_all_diacritics
from modern_greek_accentuation.augmentify import add_augment

from modern_greek_inflexion.resources import CON1_ACT, CON2A_ACT, CON2AK_ACT, CON2B_ACT, CON2D_ACT, CON2C_ACT, \
    greek_corpus, CON2E_PASS, CON2D_PASS, CON2B_PASS, CON2A_PASS, CON1_PASS, CON2C_PASS, CON2AK_PASS, CON2F_PASS
from modern_greek_inflexion.resources.verb import irregular_passive_paratatikos


def passive_paratatikos_exists(f_person: str | None, th_person: str = None) -> bool:
    if not th_person:
        th_person = f_person[:-4] + 'ταν'
        th_person_pl = put_accent_on_the_antepenultimate(f_person[:-4] + 'νταν')
        if f_person.endswith('ούμουν'):
            th_person = f_person[:-4] + 'νταν'
            th_person_pl = th_person
        elif f_person.endswith('άμην'):
            th_person = put_accent_on_the_antepenultimate(f_person[:-4] + 'ατο')
            th_person_pl = put_accent_on_the_antepenultimate(f_person[:-4] + 'αντο')

        elif f_person.endswith('μην'):
            th_person = f_person[:-3] + 'το'
            th_person_pl = f_person[:-3] + 'ντο'
        return f_person in greek_corpus or th_person in greek_corpus or th_person_pl in greek_corpus

    if not f_person:
        return th_person in greek_corpus


def create_basic_paratatikos_passive(pres_form: str, root: str, pres_conjugation: str, pres_pass_form: tuple,
                                     modal: bool = False) -> str | None:
    pass_par = []
    root = remove_all_diacritics(root)

    if not modal:
        for pass_form in pres_pass_form:

            if pres_form in irregular_passive_paratatikos:
                return irregular_passive_paratatikos[pres_form]

            elif pass_form in irregular_passive_paratatikos:
                return irregular_passive_paratatikos[pass_form]

            elif pass_form.endswith('τίθεμαι'):
                pass_par.append(put_accent_on_the_penultimate(pass_form[:-3] + 'μην'))

            elif pres_conjugation in [CON1_ACT, CON1_PASS, CON2C_ACT, CON2C_PASS]:
                if pres_conjugation == CON2C_ACT:
                    root = root + 'γ'

                pass_par.append(put_accent_on_the_penultimate(root + 'όμουν'))
                if root.endswith('ρ') and pres_conjugation in [CON1_ACT, CON1_PASS]:
                    if passive_paratatikos_exists(root + 'ιζόμουν'):
                        pass_par.append(root + 'ιζόμουν')

            elif pres_conjugation in [CON2A_ACT, CON2A_PASS]:
                pass_par.extend([root + 'ιόμουν', root + 'ούμουν', root + 'όμουν'])
                pass_par = [f for f in pass_par if passive_paratatikos_exists(f)]
                if not pass_par:
                    pass_par.append(root + 'ιόμουν')

            elif pres_conjugation in [CON2AK_ACT, CON2AK_PASS]:

                pass_par = [root + 'όμουν', root + 'ιόμουν', root + 'άμην']
                pass_par = [f for f in pass_par if passive_paratatikos_exists(f)]
                if pres_conjugation == CON2AK_ACT and not pass_par:
                    pass_par.append(root + 'ιόμουν')
                elif pres_conjugation == CON2AK_PASS and not pass_par:
                    pass_par.append(root + 'όμουν')

            elif pres_conjugation in [CON2B_ACT, CON2D_ACT, CON2F_PASS, CON2B_PASS]:
                pass_par = [root + 'ούμουν', root + 'ιόμουν']
                pass_par = [f for f in pass_par if passive_paratatikos_exists(f)]
                if not pass_par:
                    pass_par = [root + 'ούμουν']

                if pres_conjugation == CON2B_ACT and root[-1] in ['ι', 'υ']:
                    # if passive_paratatikos_exists(root + 'όμουν'):
                    pass_par.append(root + 'όμουν')

            elif pres_conjugation == CON2D_PASS:
                pass_par = [put_accent_on_the_penultimate(root + 'μην'), root[:-1] + 'όμουν', root + 'όμουν']
                augmented = [put_accent_on_the_penultimate(f) for f in add_augment(pass_par[0])]
                pass_par.extend(augmented)
                pass_par = [f for f in pass_par if passive_paratatikos_exists(f)]
                if not pass_par and pres_form.endswith('ειμαι'):
                    pass_par = [put_accent_on_the_antepenultimate(root + 'το')]

            elif pres_conjugation == CON2E_PASS:
                pass_par = [root + 'άμην', root + 'όμουν']
                pass_par = [f for f in pass_par if passive_paratatikos_exists(f)]

    else:
        # if modal
        if pres_form[-5:] == 'ιέται':
            pass_par = [root + 'ιόταν']

        elif pres_form[-5:] == 'είται':
            pass_par = add_augment(root + 'είτο')
            pass_par.append(root + 'ούνταν')

        elif pres_form[-4:] == 'άται':
            pass_par = [root + 'όταν', root + 'ιόταν']
            pass_par.extend(add_augment(root + 'άτο'))
        elif pres_form[-4:] == 'αται':
            pass_par = [put_accent_on_the_penultimate(root + 'όταν')]
            pass_par.extend(add_augment(root + 'ατο'))
        elif pres_form[-4:] == 'εται':
            pass_par = add_augment(pres_form[:-4] + 'ετο')
            pass_par.append(root + 'όταν')

        elif pres_form[-5:] == 'ειται':
            pass_par = add_augment(pres_form[:-5] + 'ειτο')
        elif pres_form.endswith('ται'):
            pass_par = add_augment(pres_form[:-3] + 'το')
        pass_par = [f for f in pass_par if passive_paratatikos_exists(None, th_person=f)]
        if not pass_par and pres_form.endswith('κειται'):
            pass_par = [pres_form[:-5] + 'ειτο']

    if pass_par:
        return ','.join(pass_par)
