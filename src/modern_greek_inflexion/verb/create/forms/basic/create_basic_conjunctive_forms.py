from modern_greek_accentuation.accentuation import is_accented
from modern_greek_accentuation.syllabify import modern_greek_syllabify

from modern_greek_inflexion.resources import greek_corpus, PASSIVE, CON1_ACT_MODAL, CON2_ACT_MODAL, ACTIVE
from modern_greek_inflexion.resources.verb import irregular_passive_roots, deponens_with_active_perf_forms
from modern_greek_inflexion.verb.create import create_regular_perf_root


def create_basic_conjunctive_forms(pres_form, pres_conjugation, root, deponens=False, not_deponens=True,
                                   intransitive_active=False, modal_act=False, modal_med=False, alternative=False):
    act_root, passive_root = None, None
    active_perf_form = passive_perf_form = ''

    conjunctive_basic_forms = None
    perf_root = None
    if not_deponens:

        act_root = create_regular_perf_root(pres_form, voice=ACTIVE, alternative=alternative)

        if not intransitive_active and not pres_form.endswith('βαίνω'):
            passive_root = create_regular_perf_root(pres_form, voice=PASSIVE, alternative=alternative)

        if act_root:

            act_perf_forms = []
            for stem in act_root.split(','):
                active_perf_form = stem + 'ω'
                syllables = modern_greek_syllabify(active_perf_form)

                if len(syllables) > 1 and not is_accented(syllables[-2]):
                    active_perf_form = stem + 'ώ'
                act_perf_forms.append(active_perf_form)
            active_perf_form = ','.join(act_perf_forms)

            # check for exv
            # if pres_form[-3:] == 'έχω' and act_root + 'ει' not in greek_corpus:
            #     active_perf_form = pres_form

        if not intransitive_active:

            if passive_root or pres_form in irregular_passive_roots:

                if ',' in passive_root:
                    passive_perf_forms = []
                    for stem in passive_root.split(','):
                        passive_perf_form = stem + 'ώ'
                        passive_perf_forms.append(passive_perf_form)
                    passive_perf_form = ','.join(passive_perf_forms)
                else:
                    passive_perf_form = passive_root + 'ώ'

                    if passive_root[-1] == 'τ' and (
                            passive_root + 'ώ' in greek_corpus or passive_root + 'εί') \
                            and (passive_root[:-1] + 'θώ' in greek_corpus or passive_root[:-1] + 'θεί' in greek_corpus):
                        passive_perf_form = passive_perf_form + ',' + passive_root[:-1] + 'θώ'
                        passive_root = passive_root + ',' + passive_root[:-1] + 'θ'
                    elif passive_root[-1] == 'τ' and (
                            passive_root[:-1] + 'θώ' in greek_corpus or passive_root[:-1] + 'θεί' in greek_corpus):
                        passive_perf_form = passive_root[:-1] + 'θώ'
                        passive_root = passive_root[:-1] + 'θ'

        conjunctive_basic_forms = active_perf_form + '/' + passive_perf_form

    elif deponens:

        passive_root = create_regular_perf_root(pres_form, voice=PASSIVE)

        if passive_root:
            if ',' in passive_root:

                passive_perf_forms = []
                for stem in passive_root.split(','):

                    passive_perf_form = stem + 'ώ'

                    if is_accented(stem):
                        passive_perf_form = stem + 'ω'

                    passive_perf_forms.append(passive_perf_form)

                passive_perf_form = ','.join(passive_perf_forms)
            else:
                passive_perf_form = passive_root + 'ώ'
                # check accent
                if is_accented(passive_root):
                    passive_perf_form = passive_root + 'ω'
                if passive_root[-1] == 'τ':

                    if passive_root[:-1] + 'θώ' in greek_corpus or passive_root[:-1] + 'θεί' in greek_corpus:
                        passive_root = passive_root + ',' + passive_root[:-1] + 'θ'

                        passive_perf_form = passive_perf_form + ',' + passive_perf_form[:-2] + 'θώ'

            conjunctive_basic_forms = '/' + passive_perf_form

            if pres_form[-7:] in deponens_with_active_perf_forms:
                act_root = passive_root
                passive_root = None
                conjunctive_basic_forms = passive_perf_form + '/'

    elif modal_act:
        if pres_conjugation == CON1_ACT_MODAL:
            act_root = create_regular_perf_root(root + 'ω', voice=ACTIVE)
        elif pres_conjugation == CON2_ACT_MODAL:
            act_root = create_regular_perf_root(root + 'ώ', voice=ACTIVE)

        if act_root:
            active_perf_form = act_root + 'ει'

            syllables = modern_greek_syllabify(active_perf_form)

            if len(syllables) > 1 and not is_accented(syllables[-2]):
                active_perf_form = act_root + 'εί'

        conjunctive_basic_forms = active_perf_form + '/'

    elif modal_med:
        perf_root = None
        if pres_form[-4:] == 'εται':
            perf_root = create_regular_perf_root(root + 'ομαι', PASSIVE)
            if perf_root and perf_root + 'εί' not in greek_corpus:
                perf_root = create_regular_perf_root(root + 'μαι', PASSIVE)
        elif pres_form[-5:] == 'είται':
            perf_root = create_regular_perf_root(root + 'ούμαι', PASSIVE)
        elif pres_form[-4:] == 'άται':
            perf_root = create_regular_perf_root(root + 'άμαι', PASSIVE)
            if perf_root and perf_root + 'εί' not in greek_corpus:
                perf_root = create_regular_perf_root(root + 'ώμαι', PASSIVE)
        elif pres_form[-4:] == 'αται':
            perf_root = create_regular_perf_root(root + 'αμαι', PASSIVE)
        elif pres_form[-3:] == 'ται':
            perf_root = create_regular_perf_root(root + 'μαι', PASSIVE)
        passive_root = perf_root

        if perf_root:
            conjunctive_basic_forms = '/' + passive_root + 'εί'

    # if passive_root and passive_root[-1] == 'τ':
    #     if passive_root[:-1] + 'θώ' in greek_corpus or passive_root[:-1] + 'θεί' in greek_corpus:
    #         passive_root = passive_root + ',' + passive_root[-1:] + 'θ'

    return conjunctive_basic_forms, perf_root, act_root, passive_root