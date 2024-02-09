from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, put_accent_on_the_antepenultimate, \
    where_is_accent
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_accentuation.resources import vowels
from modern_greek_accentuation.syllabify import count_syllables

from modern_greek_inflexion.verb.helpers import aorist_exists
from modern_greek_inflexion.resources import greek_corpus, PENULTIMATE
from modern_greek_inflexion.resources.verb import irregular_active_aorists, prefixes_before_augment


def create_basic_aorist_active(pres_form: str, active_root: str,
                               modal: bool = False) -> set:
    active_aor_forms = []

    if modal:

        active_aor_forms.extend(add_augment(active_root + 'ε'))

        # for symbainei
        anc_forms = add_augment(active_root + 'η')
        anc_forms = [a for a in anc_forms if where_is_accent(a) == PENULTIMATE]
        active_aor_forms.extend(anc_forms)

        active_aor_forms = [f for f in active_aor_forms if f in greek_corpus]
        if not active_aor_forms and active_root:
            active_aor_forms.append(put_accent_on_the_antepenultimate(active_root + 'ε'))

    else:

        if pres_form in irregular_active_aorists:
            return set(irregular_active_aorists[pres_form].split(','))

        elif pres_form[-4:-2] != active_root[-3:-1]:

            for ir_verb in irregular_active_aorists:
                length_ir_verb = len(ir_verb)
                if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
                    prefix = pres_form[:-length_ir_verb]

                    active_aor_forms.extend(add_augment(prefix + irregular_active_aorists[ir_verb]))

                    active_aor_forms = [f for f in active_aor_forms if f in greek_corpus]
                    # active_aor_forms = [put_accent_on_the_antepenultimate(f) for f in active_aor_forms]
                    if irregular_active_aorists[ir_verb][-4:] == 'βηκα' and 'λαβαίνω' not in pres_form:
                        # add archaic athematic aorist for compounds with bainw
                        archaic_aor_forms = add_augment(prefix + irregular_active_aorists[ir_verb][:-2])
                        archaic_aor_forms = [put_accent_on_the_penultimate(a) for a in archaic_aor_forms]
                        active_aor_forms.extend(archaic_aor_forms)
                        # active_aor_forms.extend(pres_form[:-length_ir_verb] + irregular_active_aorists[ir_verb][:-2])

        # if act_root and pres_form not in irregular_active_aorists and not alternative:

        for stem in active_root.split(','):
            active_aor_forms.extend(add_augment(put_accent_on_the_antepenultimate(stem + 'α')))

            # filter_out
        active_aor_forms = [f for f in active_aor_forms if aorist_exists(f)]

        if active_root.endswith('άσχ') and pres_form.endswith('έχω'):
            archaic_aor_forms = [pres_form[:-3] + 'έσχον']
            active_aor_forms = archaic_aor_forms

            # there are some instances where this algorithm can be confused by irregular imperative forms
        irregular_imperative_similar_to_aorist = ('ανέβα', 'κατέβα', 'τρέχα', 'φεύγα')

        active_aor_forms = list(set(active_aor_forms).difference(irregular_imperative_similar_to_aorist))

        if not active_aor_forms:
            if pres_form.endswith('έχω') and (
                    pres_form[:-3] in prefixes_before_augment.keys() or pres_form[:-3] in ['ισαπ']):
                # συνέθετα του έχω
                active_aor_forms.append(pres_form[:-3] + 'είχα')
                # if pres_form[:-3] + 'έσχε' in greek_corpus:
                #     active_aor_forms.append(pres_form[:-3] + 'έσχον')

            elif pres_form.endswith('άγω') and pres_form[:-3] in prefixes_before_augment.keys():
                active_aor_forms.append(pres_form[:-3] + 'ήγαγα')
            elif pres_form.endswith('βαίνω') and pres_form[:-5] in prefixes_before_augment:
                athematic = prefixes_before_augment[pres_form[:-5]] + 'έβην'
                modern = prefixes_before_augment[pres_form[:-5]] + 'έβηκα'
                # if athematic in greek_corpus:
                active_aor_forms.append(athematic)
                active_aor_forms.append(modern)

            else:
                for act_r in active_root.split(','):
                    aor = act_r + 'α'
                    if count_syllables(aor) < 3 and aor[0] not in vowels:
                        aor = 'ε' + aor
                    active_aor_forms.append(put_accent_on_the_antepenultimate(aor))

    return set(active_aor_forms)
