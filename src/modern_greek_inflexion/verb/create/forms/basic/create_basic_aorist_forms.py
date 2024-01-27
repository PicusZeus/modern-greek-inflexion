from __future__ import annotations

from modern_greek_accentuation.accentuation import put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, \
    where_is_accent
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.resources import vowels, prefixes_before_augment
from modern_greek_accentuation.syllabify import count_syllables

from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.verb import irregular_active_aorists, irregular_passive_aorists, \
    deponens_with_active_perf_forms


def create_basic_aorist_forms(pres_form: str, act_root: str, passive_root: str, deponens: bool = False,
                              not_deponens: bool = True, modal_act: bool = False,
                              modal_med: bool = False, alternative: bool = False) -> str:
    """
    :param pres_form:
    :param act_root:
    :param passive_root:
    :param deponens:
    :param not_deponens:
    :param modal_act:
    :param modal_med:
    :param alternative:
    :return: aorist_basic_forms - active_alt,active_alt/passive_alt,passive_alt'
    """
    aorist_basic_forms = ''
    active_aor_forms, passive_aor_forms = [], []

    if not_deponens:
        if not alternative:

            if pres_form in irregular_active_aorists:
                active_aor_forms.append(irregular_active_aorists[pres_form])

            elif act_root and pres_form[-4:-2] != act_root[-3:-1]:

                for ir_verb in irregular_active_aorists:
                    length_ir_verb = len(ir_verb)
                    if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
                        if pres_form in irregular_active_aorists:

                            active_aor_forms.append(irregular_active_aorists[pres_form])
                        else:
                            active_aor_forms.extend(
                                add_augment(pres_form[:-length_ir_verb] + irregular_active_aorists[ir_verb]))
                        active_aor_forms = [f for f in active_aor_forms if f in greek_corpus]
                        # active_aor_forms = [put_accent_on_the_antepenultimate(f) for f in active_aor_forms]
                        if irregular_active_aorists[ir_verb][-4:] == 'βηκα' and 'λαβαίνω' not in pres_form:
                            # add archaic athematic aorist for compounds with bainw

                            active_aor_forms.extend(
                                add_augment(pres_form[:-length_ir_verb] + irregular_active_aorists[ir_verb][:-2]))
                            # active_aor_forms.extend(pres_form[:-length_ir_verb] + irregular_active_aorists[ir_verb][:-2])

                for ir_verb in irregular_passive_aorists:
                    length_ir_verb = len(ir_verb)

                    if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
                        passive_aor_forms.extend(
                            add_augment(pres_form[:-length_ir_verb] + irregular_passive_aorists[ir_verb]))

        if act_root and pres_form not in irregular_active_aorists and not alternative:

            if ',' in act_root:
                for stem in act_root.split(','):
                    active_aor_forms.extend(add_augment(put_accent_on_the_antepenultimate(stem + 'α')))
            else:
                active_aor_forms.extend(add_augment(put_accent_on_the_antepenultimate(act_root + 'α')))

            if act_root.endswith('άσχ'):
                archaic_aor_form = add_augment(pres_form[:-3] + 'σχον')
                active_aor_forms.extend(archaic_aor_form)

            # filter_out
            active_aor_forms_e = [f for f in active_aor_forms if (f[:-1] + 'ε' in greek_corpus)]
            active_aor_forms_e = [f for f in active_aor_forms_e if count_syllables(f) > count_syllables(act_root) + 1]
            active_aor_forms = [f for f in active_aor_forms if (f in greek_corpus or f[:-1] + 'ες' in greek_corpus)]
            active_aor_forms.extend(active_aor_forms_e)
            if not active_aor_forms and pres_form[-3:] == 'άρω':
                # common argo and english loans
                active_aor_forms.append(put_accent_on_the_antepenultimate(pres_form[:-1] + 'α'))
                if 'ρίσ' in act_root:
                    active_aor_forms.append(put_accent_on_the_antepenultimate(pres_form[:-1] + 'ισα'))

            if 'ρίσ' in act_root and pres_form[-3:] == 'άρω':
                # common argo and english loans
                active_aor_forms.append(put_accent_on_the_antepenultimate(pres_form[:-1] + 'α'))

            if not active_aor_forms and act_root[-1] in ['σ', 'ξ', 'ψ']:
                aor = act_root + 'α'
                if count_syllables(act_root) == 1 and act_root[0] not in vowels:
                    aor = 'ε' + aor
                active_aor_forms.append(put_accent_on_the_antepenultimate(aor))

            # there are some instances where this algorithm can be confused by irregular imperative forms
            irregular_imperative_similar_to_aorist = ('ανέβα', 'κατέβα', 'τρέχα', 'φεύγα')

            active_aor_forms = list(set(active_aor_forms).difference(irregular_imperative_similar_to_aorist))

            # special case for poiw
            if 'ποιήσ' in act_root:
                active_aor_forms.append(put_accent_on_the_antepenultimate(act_root + 'α', true_syllabification=False))

        if passive_root or passive_aor_forms:

            # archaic_passive_aor = stem + 'ηκα'

            for stem in passive_root.split(','):
                pass_aor_form = stem + 'ηκα'

                passive_aor_forms.append(put_accent_on_the_antepenultimate(pass_aor_form))
                passive_aor_forms.append(put_accent_on_the_antepenultimate(pass_aor_form, true_syllabification=False))

                # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in corpus
                if not pres_form.endswith('έχω'):
                    archaic_passive_aor = put_accent_on_the_penultimate(stem + 'η')

                    archaic_passive_aor = add_augment(archaic_passive_aor)

                    archaic_passive_aor = [put_accent_on_the_penultimate(v) for v in archaic_passive_aor]
                    if stem.endswith('ιδωθ'):
                        archaic_passive_aor = add_augment(stem + 'ηκα')
                    passive_aor_forms.extend(archaic_passive_aor)

            passive_aor_forms = [f for f in passive_aor_forms if f in greek_corpus or f + 'ν' in greek_corpus]

            if not passive_aor_forms:

                if pres_form in irregular_passive_aorists:
                    passive_aor_forms.append(irregular_passive_aorists[pres_form])
                elif passive_root:
                    passive_aor_forms.append(put_accent_on_the_antepenultimate(passive_root + 'ηκα'))

        # if active_aor_forms:
        active_aor_forms = list(set(active_aor_forms))
        active_aor_forms = ','.join(active_aor_forms)

        if (not active_aor_forms and
                pres_form.endswith('έχω') and
                pres_form[:-3] in prefixes_before_augment.keys() or pres_form[:-3] in ['ισαπ']):
            # συνέθετα του έχω
            active_aor_forms = pres_form[:-3] + 'είχα'
        elif not active_aor_forms and pres_form in irregular_active_aorists.keys():
            active_aor_forms = put_accent_on_the_antepenultimate(irregular_active_aorists[pres_form])
        elif not active_aor_forms and pres_form.endswith('άγω') and pres_form[:-3] in prefixes_before_augment.keys():
            active_aor_forms = pres_form[:-3] + 'ήγαγα'
        elif not active_aor_forms and pres_form.endswith('βαίνω') and pres_form[:-5] in prefixes_before_augment:
            active_aor_forms = prefixes_before_augment[pres_form[:-5]] + 'έβη'
        elif not active_aor_forms and act_root:
            active_aor_forms = put_accent_on_the_antepenultimate(act_root + 'α')

        # if passive_aor_form:
        passive_aor_forms = set(passive_aor_forms)
        passive_aor_forms = ','.join(passive_aor_forms)

        aorist_basic_forms = '/'.join([active_aor_forms, passive_aor_forms])

    elif deponens:
        if pres_form[-7:] in deponens_with_active_perf_forms:
            passive_root = act_root
        if passive_root:



            if ',' in passive_root:
                passive_aor_forms = []
                for stem in passive_root.split(','):
                    pass_aor_form = stem + 'ηκα'
                    passive_aor_forms.append(put_accent_on_the_antepenultimate(pass_aor_form))

                    # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in
                    # corpus
                    archaic_passive_aor = stem + 'η'
                    archaic_passive_aor = add_augment(archaic_passive_aor)
                    passive_aor_forms.extend(archaic_passive_aor)

            else:
                passive_aor_forms = passive_root + 'ηκα'

                passive_aor_forms = [put_accent_on_the_antepenultimate(passive_aor_forms)]
                # archaic passive
                archaic_passive_aor = passive_root + 'η'
                archaic_passive_aor = add_augment(archaic_passive_aor)
                passive_aor_forms.extend(archaic_passive_aor)
            # filter out

            # ginomai, erxomai, kathomai

            if pres_form[-7:] in deponens_with_active_perf_forms:
                if ',' in passive_root:
                    passive_aor_forms = []
                    for stem in passive_root.split(','):
                        pass_aor_form = stem + 'α'
                        passive_aor_forms.extend(add_augment(pass_aor_form))
                else:
                    passive_aor_forms = passive_root + 'α'
                    passive_aor_forms = add_augment(passive_aor_forms)

            passive_aor_forms = [form for form in passive_aor_forms if form in greek_corpus]

            if pres_form in irregular_passive_aorists:
                passive_aor_forms.append(irregular_passive_aorists[pres_form])

            if not passive_aor_forms:
                passive_aor_forms.append(put_accent_on_the_antepenultimate(passive_root.split(',')[0] + 'ηκα'))
            passive_aor_forms = ','.join(passive_aor_forms)

            aorist_basic_forms = '/' + passive_aor_forms
            if pres_form[-7:] in deponens_with_active_perf_forms:
                aorist_basic_forms = passive_aor_forms + '/'
    elif modal_act or modal_med:
        mod_root = None
        if act_root:
            mod_root = act_root
        elif passive_root:
            mod_root = passive_root
        if mod_root:
            aor_forms = add_augment(mod_root + 'ε')
            if passive_root:
                aor_forms.extend(add_augment(mod_root + 'ηκε'))
            # mainly for symbainei
            anc_forms = add_augment(mod_root + 'η')
            anc_forms = [a for a in anc_forms if where_is_accent(a) == 'penultimate']
            aor_forms.extend(anc_forms)

            aor_forms = [f for f in aor_forms if f in greek_corpus]

            aorist_basic_forms = ','.join(aor_forms)
            if modal_act:
                aorist_basic_forms = aorist_basic_forms + '/'
            elif modal_med:
                aorist_basic_forms = '/' + aorist_basic_forms

    return aorist_basic_forms
