from modern_greek_accentuation.accentuation import put_accent_on_the_antepenultimate, put_accent_on_the_penultimate
from modern_greek_accentuation.augmentify import add_augment
from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.verb import irregular_passive_aorists


def passive_aorist_exists(f_s: str) -> bool:
    if f_s.endswith('ηκα'):
        th_s = f_s[:-1] + 'ε'
        f_pl = put_accent_on_the_antepenultimate(f_s + 'με')
        th_pl = f_s + 'ν'
        return f_s in greek_corpus or th_s in greek_corpus or f_pl in greek_corpus or th_pl
    else:
        th_p = f_s + 'ν'
        return f_s in greek_corpus or th_p in greek_corpus


def create_basic_aorist_passive(pres_form: str, passive_root: str,
                                modal: bool = False) -> set:
    passive_aor_forms = []

    if pres_form in irregular_passive_aorists:
        return set(irregular_passive_aorists[pres_form].split(','))

    if modal:
        for stem in passive_root.split(','):
            pass_aor_form = put_accent_on_the_antepenultimate(stem + 'ηκε', False)
            passive_aor_forms.append(pass_aor_form)

            archaic_passive_aorist = add_augment(put_accent_on_the_penultimate(stem + 'η'))
            archaic_passive_aorist = [put_accent_on_the_penultimate(a) for a in archaic_passive_aorist]
            passive_aor_forms.extend(archaic_passive_aorist)

            passive_aor_forms = [a for a in passive_aor_forms if a in greek_corpus]

            return set(passive_aor_forms)

    else:

        for ir_verb in irregular_passive_aorists:
            length_ir_verb = len(ir_verb)

            if len(pres_form) >= length_ir_verb and pres_form[-length_ir_verb:] == ir_verb:
                prefix = pres_form[:-length_ir_verb]
                ir_aorists = irregular_passive_aorists[ir_verb]
                for ir_a in ir_aorists.split(','):
                    passive_aor_forms.append(prefix + ir_a)

        # passive_aor_forms = [a for a in passive_aor_forms if aorist_exists(a)]

        for stem in passive_root.split(','):
            pass_aor_form = stem + 'ηκα'

            # passive_aor_forms.append(put_accent_on_the_antepenultimate(pass_aor_form))
            passive_aor_forms.append(put_accent_on_the_antepenultimate(pass_aor_form, true_syllabification=False))
            if pass_aor_form.endswith('ιδωθηκα'):
                passive_aor_forms.append(put_accent_on_the_antepenultimate(pass_aor_form.replace('ιδωθηκα', 'ειδωθηκα')))
            # archaic passive on purpose 3rd person, because it's more popular and so more probable that exists in corpus
            if not pres_form.endswith('έχομαι') and not pres_form.endswith('έχω'):
                archaic_passive_aor = add_augment(put_accent_on_the_penultimate(stem + 'η'))
                archaic_passive_aor = [put_accent_on_the_penultimate(a) for a in archaic_passive_aor]

                passive_aor_forms.extend(archaic_passive_aor)

        passive_aor_forms = set([a for a in passive_aor_forms if passive_aorist_exists(a)])

        if not passive_aor_forms:

            passive_aor_forms = [put_accent_on_the_antepenultimate(a + 'ηκα') for a in passive_root.split(',')]

    return passive_aor_forms
