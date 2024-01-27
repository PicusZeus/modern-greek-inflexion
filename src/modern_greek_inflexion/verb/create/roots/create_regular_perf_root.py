from __future__ import annotations

from modern_greek_accentuation.accentuation import *
from modern_greek_accentuation.resources import prefixes_before_augment
from modern_greek_inflexion.resources.resources import greek_corpus
from modern_greek_inflexion.resources.verb import irregular_active_roots, irregular_passive_roots
from modern_greek_inflexion.resources.variables import *
from modern_greek_inflexion.verb.recognize import (recognize_active_non_past_conjugation,
                                                   recognize_passive_present_continuous_conjugation)
from modern_greek_inflexion.helpers import passive_subjunctive_exists, \
    active_subjunctive_exists, active_subjunctive_sigmatic_exists


def create_regular_perf_root(verb: str, voice: str = ACTIVE, act_perf_root: str | None = None,
                             alternative: bool = False) -> str | None:
    # create regular aorist roots from present root. For obvious reasons it's only useful for verbs you don't have
    # supplied aorist forms and so it is prone to errors that cannot be eliminated
    perf_root = None
    irregular = False

    multiple_stems = None
    if verb[-1] in ['ω', 'ώ'] or verb[-2:] in ['ει', 'εί'] or verb[-5:] == 'είμαι':
        res = recognize_active_non_past_conjugation(verb)

    else:
        res = recognize_passive_present_continuous_conjugation(verb)

    if not res:
        return None

    root = res[ROOT]
    conjugation = res['conjugation_ind']

    if conjugation == MODAL:
        perf_root = root

    if voice == ACTIVE:
        # there are no multiple stems in this category, so do not do anything

        if not alternative:
            if verb in irregular_active_roots:
                return irregular_active_roots[verb]

            for ir_verb, ir_root in sorted(irregular_active_roots.items(), key=lambda key: len(key[0]), reverse=True):
                if ir_root:
                    multiple_perf_roots = []
                    for stem in ir_root.split(','):

                        if len(root) >= len(ir_verb) and root[-len(ir_verb):] == ir_verb:
                            prefix = root[:-len(ir_verb)]
                            if prefix in prefixes_before_augment:
                                beta_perf_root = prefix + stem

                                if (beta_perf_root + 'ω' in greek_corpus) or (
                                        beta_perf_root + 'ώ' in greek_corpus) or stem == 'καταστήσ':
                                    multiple_perf_roots.append(beta_perf_root)

                    perf_root = ','.join(multiple_perf_roots)

                    if ',' in perf_root:
                        multiple_stems = True
                    if perf_root:
                        irregular = True
                        break

    if voice == PASSIVE:
        if not alternative:

            if verb in irregular_passive_roots:
                return irregular_passive_roots[verb]

            for ir_verb, ir_root in sorted(irregular_passive_roots.items(), key=lambda key: len(key[0]), reverse=True):

                if ir_root:
                    # that is if many stems
                    multiple_perf_roots = []
                    for stem in ir_root.split(','):
                        if len(root) >= len(ir_verb) and root[-len(ir_verb):] == ir_verb:
                            prefix = root[:-len(ir_verb)]
                            # if prefix in prefixes_before_augment:
                            beta_perf_root = prefix + stem
                            if (beta_perf_root + 'ώ' in greek_corpus) or (beta_perf_root + 'ω' in greek_corpus) or (
                                    beta_perf_root + 'εί' in greek_corpus) or (
                                    beta_perf_root + 'ει' in greek_corpus):
                                multiple_perf_roots.append(beta_perf_root)

                    if multiple_perf_roots:
                        perf_root = ','.join(multiple_perf_roots)
                        irregular = True
                        multiple_stems = True
                        break

    if conjugation in [CON1_ACT, CON1_PASS, CON1_ACT_MODAL] and not perf_root:

        # pattern_a_ain = re.compile(".*α.αίν$")
        if root[-3:] == 'αίν':
            perf_root = root[:-3] + 'ήσ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = root[:-3] + 'άσ'
                if not active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = root[:-3] + 'άν'
                    if not active_subjunctive_exists(perf_root):
                        perf_root = root[:-3] + 'ύν'
                        if not active_subjunctive_exists(perf_root):
                            perf_root = root[:-3] + 'άξ'
                            if not active_subjunctive_sigmatic_exists(perf_root):
                                perf_root = root[:-3] + 'έσ'
                                if not active_subjunctive_sigmatic_exists(perf_root):
                                    perf_root = root[:-3] + 'άν'
                                    if verb in ['χραίνω', 'πααίνω', 'κραίνω', 'πτωχαίνω', 'γλαφυραίνω', 'ξανταίνω',
                                                'αναξαίνω', 'χλιαραίνω', 'ανταίνω']:
                                        # no in db, rare verbs, create different perf root than an
                                        perf_root = ''
        elif root.endswith('άν'):
            perf_root = root[:-1] + 'σ'

            if not active_subjunctive_sigmatic_exists(perf_root):

                perf_root = root[:-2] + 'ήσ'

                if not active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = root[:-1] + 'ξ'
                    if not active_subjunctive_sigmatic_exists(perf_root):
                        perf_root = root

        elif root.endswith('ών'):
            perf_root = root[:-1] + 'σ'
        elif root.endswith('ίν'):
            perf_root = root[:-1] + 'σ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = ''
        elif root.endswith('έν'):
            perf_root = root[:-1] + 'σ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = root[:-2] + 'ήσ'
                if not active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = ''
        elif root.endswith('ν') and root[-2] in vowels:

            perf_root = root[:-1] + 'σ'
            if not active_subjunctive_sigmatic_exists(perf_root) and root[-2:] == 'ύν':
                perf_root = root

        elif root.endswith('έλν'):
            perf_root = root[:-3] + 'είλ'
            if not active_subjunctive_exists(perf_root):
                perf_root = root[:-3] + 'άλ'
                if not active_subjunctive_exists(perf_root):
                    perf_root = ''

        elif root.endswith('έρν'):
            perf_root = root[:-3] + 'είρ'
            if not active_subjunctive_exists(perf_root):
                perf_root = root[:-3] + 'άρ'
                if not active_subjunctive_exists(perf_root):
                    perf_root = root[:-3] + 'ύρ'
                    if not active_subjunctive_exists(perf_root):
                        perf_root = root[:-3] + 'έρ'
                        if not active_subjunctive_exists(perf_root):
                            perf_root = ''
        elif root.endswith('ν'):
            if root.endswith('χν'):
                perf_root = root[:-2] + 'ξ'
            else:
                perf_root = root[:-1]
                if not active_subjunctive_exists(perf_root):
                    perf_root = ''

        elif root[-2:] in ['σσ', 'ττ', 'χν', 'γγ']:
            perf_root = root[:-2] + 'ξ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = ''
        elif root[-2:] in ['φτ', 'πτ']:
            perf_root = root[:-2] + 'ψ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = ''
        elif root[-1] in ['θ', 'δ', 'τ']:

            perf_root = root[:-1] + 'σ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = ''

        elif root[-1] == 'ζ':
            perf_root = root[:-1] + 'ξ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = root[:-1] + 'σ'
                if ((not root.endswith('ίζ') or not root.endswith('άζ')) and
                        not active_subjunctive_sigmatic_exists(perf_root)):
                    # if not check_perf_active_subjunctive_in_corpus(perf_root):
                    perf_root = ''

        elif root.endswith('σκ'):
            perf_root = root[:-2] + 'ξ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = ''

        elif root[-1] in ['κ', 'χ', 'γ']:

            if root.endswith('άγ') and root[:-2] in prefixes_before_augment:
                perf_root = root[:-2] + 'αγάγ'
            else:
                perf_root = root[:-1] + 'ξ'
                if not active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = ''

            # if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
            #     perf_root = ''

        elif root[-1] in ['β', 'π', 'φ']:
            perf_root = root[:-1] + 'ψ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = ''
        elif root[-2:] in ['εύ', 'αύ']:
            perf_root = root[:-2] + put_accent_on_syllable(root[-2]) + 'ψ'
            # alternative stem on eus
            alternative_root = root + 'σ'
            if active_subjunctive_sigmatic_exists(alternative_root):
                if active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = ','.join([perf_root, alternative_root])
                    multiple_stems = True
                else:
                    perf_root = alternative_root

        elif root[-1] in ['ύ', 'ί', 'έ']:
            perf_root = root + 'σ'
            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = ''

        elif root.endswith('έλλ'):
            perf_root = root[:-3] + 'είλ'
            if not active_subjunctive_exists(perf_root):
                perf_root = ''

        elif root.endswith('λλ'):
            perf_root = root[:-1]
            if not active_subjunctive_exists(perf_root):
                perf_root = ''

        elif root.endswith('έμ'):
            perf_root = root[:-2] + 'είμ'
            if not active_subjunctive_exists(perf_root):
                perf_root = ''

        elif root.endswith('μ'):
            perf_root = root

        elif root.endswith('άρ'):
            perf_root = root + ',' + put_accent_on_the_ultimate(root + 'ισ')
            multiple_stems = True

        elif root.endswith('εύρ'):
            perf_root = ''

        elif root.endswith('φέρ'):
            perf_root = root

        elif root.endswith('έρ'):
            perf_root = root[:-2] + 'είρ'
            if not active_subjunctive_exists(perf_root):
                perf_root = ''

        elif root.endswith('είρ'):
            perf_root = root

        elif root.endswith('αίρ'):
            perf_root = root[:-3] + 'άρ'

        elif root.endswith('ύρ'):
            perf_root = root


        elif root.endswith('έρ'):
            perf_root = root[:-2] + 'είρ'
            if not active_subjunctive_exists(perf_root):
                perf_root = ''

        elif root.endswith('ρ'):
            perf_root = put_accent_on_the_ultimate(root + 'ίσ')
            if not active_subjunctive_exists(perf_root):
                perf_root = ""


        elif root in ['επέστη']:
            # ancient form
            perf_root = root

    elif conjugation in [CON2A_ACT, CON2B_ACT, CON2A_PASS, CON2B_PASS, CON2C_PASS, CON2_ACT_MODAL] and \
            not perf_root:

        perf_root = root + 'ήσ'

        # εξαιρέσεις
        if (conjugation in [CON2A_ACT, CON2A_PASS] and
                not active_subjunctive_sigmatic_exists(perf_root) and
                root[-2:] in ['χν', 'ρν']):
            perf_root = root[:-1] + 'άσ'

        if (conjugation in [CON2A_ACT, CON2B_ACT] and
                not active_subjunctive_sigmatic_exists(perf_root)):
            perf_root = root + 'ήξ'

            if (conjugation in [CON2B_ACT, CON2A_ACT] and
                    not active_subjunctive_sigmatic_exists(perf_root)):

                perf_root = root + 'ίσ'

                if not active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = root + 'ήσ'

        if not active_subjunctive_sigmatic_exists(perf_root):
            perf_root = root + 'άσ'

            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = root + 'έσ'
                if not active_subjunctive_sigmatic_exists(perf_root):

                    perf_root = root + 'άξ'
                    if not active_subjunctive_sigmatic_exists(perf_root):
                        perf_root = root + 'έξ'
                        if not active_subjunctive_sigmatic_exists(perf_root):
                            perf_root = root + 'ήξ'
                            if not active_subjunctive_sigmatic_exists(perf_root):
                                perf_root = root + 'ήσ'
        # special case for compounds with ποιω that are not in my db for some reasons

        if root[-3:] == 'ποι' and conjugation in [CON2B_ACT, CON2B_PASS]:
            perf_root = root + 'ήσ'

    elif conjugation == CON2C_ACT and not perf_root:
        # my best guess is to remove 2 last syllables and to add αψα

        irregular_2c_roots = [['τρώ', 'φά'], ['λέ', 'π'], ['τρώγ', 'φάγ']]

        for pair in irregular_2c_roots:

            if len(root) >= len(pair[0]) and root[-len(pair[0]):] == pair[0]:

                beta_perf_root = root[:-len(pair[0])] + pair[1]
                if beta_perf_root + 'ω' in greek_corpus:
                    perf_root = beta_perf_root
                    break
        if root[-2:] == 'ού' and not perf_root:
            # akouw
            perf_root = root + 'σ'
        elif root[-2:] in diphtongs:
            perf_root = root[:-2] + 'άψ'
            if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                perf_root = root + 'ξ'
        else:
            perf_root = root[:-1] + 'άψ'

    elif conjugation == CON2D_ACT and not perf_root:
        # archaic on o
        perf_root = root + 'ώσ'

    if voice == PASSIVE and conjugation in [CON1_ACT, CON1_PASS, CON1_PASS_MODAL,
                                            CON2_PASS_MODAL, CON2D_ACT, CON2D_PASS] and not irregular:

        perf_root = None
        root = remove_all_diacritics(root)
        if root[-3:] == 'αιν':
            perf_root = root[:-3] + 'ανθ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-3] + 'υνθ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-2] + 'θ'
                    if not passive_subjunctive_exists(perf_root):
                        perf_root = root[:-2] + 'χτ'

                        if not passive_subjunctive_exists(perf_root):
                            perf_root = root[:-2] + 'στ'

        elif root.endswith('αν'):
            perf_root = (root[:-1] + 'θ')

            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-2] + 'ηθ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-1] + 'στ'

        elif root.endswith('εν'):
            perf_root = (root[:-1] + 'θ')
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-2] + 'ηθ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-2] + 'ηστ'

        elif root.endswith('ν') and root[-2] in vowels:
            perf_root = root + 'θ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-1] + 'θ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-1] + 'στ'

        elif root.endswith('ελν'):
            perf_root = root[:-3] + 'αλθ'
            if not passive_subjunctive_exists(perf_root):

                perf_root = root[:-3] + 'ελθ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = ''

        elif root.endswith('ερν'):
            perf_root = root[:-3] + 'αρθ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-3] + 'ερθ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = ''

        elif root.endswith('ν'):
            perf_root = root[:-1] + 'θ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-1] + 'τ'

        elif root[-2:] in ['σσ', 'ττ', 'σκ']:
            perf_root = root[:-2] + 'χτ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-2] + 'χθ'

            if passive_subjunctive_exists(root[:-2] + 'γ'):
                perf_root = ','.join([perf_root, root[:-2] + 'γ'])

        elif root[-2:] in ['πτ', 'φτ']:
            perf_root = root[:-2] + 'φτ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-2] + 'π'

        elif root[-1] in ['τ', 'δ']:
            perf_root = root[:-1] + 'θ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root + 'θ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-1] + 'στ'

        elif root[-1] in ['θ', 'σ']:
            perf_root = root[:-1] + 'στ'

        elif root[-1] == 'ζ':
            perf_root = root[:-1] + 'χτ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-1] + 'στ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-1] + 'θ'

        elif root[-1] in ['κ', 'χ', 'γ']:
            if root[-2:] in ['γγ']:
                root = root[:-1]
            perf_root = root[:-1] + 'χτ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-1] + 'χθ'

        elif root[-1] in ['β', 'π', 'φ', 'ψ']:
            perf_root = root[:-1] + 'φτ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-1] + 'φθ'
        elif root[-2:] in ['ευ', 'αυ']:
            perf_root = root + 'τ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root + 'θ'
        elif root[-1] in ['ι', 'υ', 'ε']:
            perf_root = root + 'στ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root + 'σθ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root + 'θ'
        elif root.endswith('ελλ'):
            perf_root = root[:-3] + 'αλθ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-3] + 'ελθ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = ''

        elif root.endswith('λλ'):
            perf_root = root[:-1] + 'θ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = ''

        elif root.endswith('εμ'):
            perf_root = root + 'ηθ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = ''

        elif root.endswith('εuρ'):
            perf_root = root + 'εθ'

        elif root.endswith('αιρ'):

            perf_root = root[:-3] + 'αρθ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-3] + 'αρ'

        elif root.endswith('ειρ'):
            perf_root = root[:-3] + 'αρθ'
            if not passive_subjunctive_exists(perf_root):
                perf_root = root[:-3] + 'αρ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-3] + 'ερθ'

        elif root.endswith('υρ'):
            perf_root = root + 'θ'

        elif root.endswith('αρ'):
            perf_root = root + 'ιστ'

        if conjugation == CON2D_ACT:
            perf_root = root + 'ωθ'
        if perf_root:
            perf_root = remove_all_diacritics(perf_root)
        if perf_root and perf_root[-2:] == "χτ":
            if perf_root + 'εί' not in greek_corpus and perf_root[:-1] + 'θεί' in greek_corpus:
                perf_root = perf_root[:-1] + 'Θ'

        if not perf_root and root + 'στώ' in greek_corpus:
            perf_root = root + 'στ'

    if voice == PASSIVE and \
            conjugation in [CON2A_ACT, CON2B_ACT, CON2C_ACT, CON2A_PASS, CON2B_PASS, CON2E_PASS,
                            CON2C_PASS, CON2AB_PASS] and not irregular:

        perf_root = root + 'ηθ'

        if root[-2:] in ['ρν', 'χν'] and not passive_subjunctive_exists(perf_root):
            perf_root = root[:-1] + 'αστ'
        # εξαιρέσεις

        if not passive_subjunctive_exists(perf_root):

            if conjugation in [CON2A_ACT, CON2B_ACT, CON2B_PASS, CON2B_PASS, CON2A_PASS, CON2AB_PASS]:
                perf_root = root + 'αστ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root + 'εστ'
                    if not passive_subjunctive_exists(perf_root):
                        perf_root = root + "αθ"
                        if not passive_subjunctive_exists(perf_root):
                            perf_root = root + "εθ"

                            if not passive_subjunctive_exists(perf_root) and conjugation not in [CON2AB_PASS]:
                                perf_root = root + "αχτ"
                                if not passive_subjunctive_exists(perf_root) and conjugation not in [CON2AB_PASS]:
                                    perf_root = root + "εχτ"
                                    if not passive_subjunctive_exists(perf_root) and conjugation not in [CON2AB_PASS]:
                                        perf_root = root + "ηχτ"
                                        if not passive_subjunctive_exists(perf_root) and conjugation not in [CON2AB_PASS]:
                                            perf_root = root + "ιστ"

        # σπεσιαλ case for compounds with poiw
        if root[-3:] == 'ποι' and conjugation in [CON2B_ACT, CON2B_PASS]:
            perf_root = root + 'ηθ'
        perf_root = remove_all_diacritics(perf_root)

    if verb.endswith('βαίνω') and verb[:-5] in prefixes_before_augment:
        perf_root = verb[:-5] + 'β'

    if not perf_root:
        return

    if perf_root:
        if (perf_root + 'ω' in greek_corpus or
            perf_root + 'ώ' in greek_corpus or
            perf_root + 'εί' in greek_corpus or
            perf_root[:-1] + 'μένος' in greek_corpus or
            multiple_stems or
            (count_syllables(root) > 1
             and conjugation in [CON2A_ACT, CON2B_ACT, CON1_ACT]
             and voice == ACTIVE)) or perf_root in ['β']:
            return perf_root


