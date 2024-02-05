from __future__ import annotations

from modern_greek_accentuation.accentuation import *
from modern_greek_accentuation.resources import prefixes_before_augment, prefixes_before_augment_on_vowel

from modern_greek_inflexion.resources.resources import greek_corpus
from modern_greek_inflexion.resources.verb import irregular_active_roots
from modern_greek_inflexion.resources.variables import *
from modern_greek_inflexion.verb.helpers import active_subjunctive_exists, active_subjunctive_sigmatic_exists


def create_regular_perf_active_root(verb: str, pres_conjugation: str = None,
                                    root: str = None) -> str | None:
    # create regular aorist roots from present root. For obvious reasons it's only useful for verbs you don't have
    # supplied aorist forms and so it is prone to errors that cannot be eliminated
    perf_root = None
    irregular = False

    if pres_conjugation == MODAL:
        perf_root = root

    if verb in irregular_active_roots:
        return irregular_active_roots[verb]

    for ir_verb, ir_root in sorted(irregular_active_roots.items(), key=lambda key: len(key[0]), reverse=True):
        if ir_root:
            multiple_perf_roots = []
            for stem in ir_root.split(','):

                if len(root) >= len(ir_verb) and root[-len(ir_verb):] == ir_verb:
                    prefix = root[:-len(ir_verb)]
                    if prefix in prefixes_before_augment or prefix in prefixes_before_augment_on_vowel:
                        beta_perf_root = prefix + stem

                        if (beta_perf_root + 'ω' in greek_corpus) or (
                                beta_perf_root + 'ώ' in greek_corpus) or stem == 'καταστήσ':
                            multiple_perf_roots.append(beta_perf_root)

            perf_root = ','.join(multiple_perf_roots)

            if perf_root:
                irregular = True
                break

    if pres_conjugation in [CON1_ACT, CON1_PASS, CON1_ACT_MODAL] and not irregular:

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
                                    perf_root = ""
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
            if root.endswith('άγ') and root[:-2] in prefixes_before_augment_on_vowel:
                perf_root = root[:-2] + 'αγάγ'
            else:
                perf_root = root[:-1] + 'ξ'
                if not active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = ''

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
            if not active_subjunctive_exists(perf_root) and root.endswith('χαίρ'):
                perf_root = put_accent_on_the_ultimate(root + 'ησ')
                if not active_subjunctive_exists(perf_root):
                    perf_root = ''

        elif root.endswith('άρ') or root.endswith('ίρ'):
            perf_root = root + ',' + put_accent_on_the_ultimate(root + 'ισ')
        # elif root.endswith('ύρ'):
        #     perf_root = root

        elif root.endswith('ρ'):
            perf_root = put_accent_on_the_ultimate(root + 'ίσ')
            if not active_subjunctive_exists(perf_root):
                perf_root = put_accent_on_the_ultimate(root + 'ήσ')
                if not active_subjunctive_exists(perf_root):
                    perf_root = root

        elif root in ['επέστη']:
            # ancient form
            perf_root = root

    elif pres_conjugation in [CON2A_ACT, CON2AK_ACT, CON2B_ACT, CON2A_PASS, CON2B_PASS, CON2C_PASS, CON2_ACT_MODAL] and \
            not irregular:

        perf_root = root + 'ήσ'
        if root[-2:] in ['χν', 'ρν', 'λν']:
            perf_root = root[:-1] + 'ήσ'

        if active_subjunctive_sigmatic_exists(perf_root) and active_subjunctive_sigmatic_exists(root + 'ήξ'):
            alternative_root = root + 'ήξ'
            perf_root = perf_root + ',' + alternative_root


        # elif not active_subjunctive_sigmatic_exists(perf_root) and root[-2:] in ['χν', 'ρν', 'λν']:
        #     perf_root = root[:-1] + 'άσ'
        #     if not active_subjunctive_sigmatic_exists(perf_root):
        #         perf_root = root + 'ίσ'
        #         if not active_subjunctive_sigmatic_exists(perf_root):
        #             perf_root = root + 'ήσ'
        #             if not active_subjunctive_sigmatic_exists(perf_root):
        #                 perf_root = ''

        elif not active_subjunctive_sigmatic_exists(perf_root):
            perf_root = root + 'άσ'
            if root[-2:] in ['χν', 'ρν', 'λν']:
                perf_root = root[:-1] + 'άσ'

            if not active_subjunctive_sigmatic_exists(perf_root):
                perf_root = root + 'έσ'
                if not active_subjunctive_sigmatic_exists(perf_root):
                    perf_root = root + 'άξ'
                    if active_subjunctive_sigmatic_exists(perf_root) and active_subjunctive_sigmatic_exists(
                            root + 'ήξ'):
                        perf_root = perf_root + ',' + root + 'ήξ'
                    elif not active_subjunctive_sigmatic_exists(perf_root):
                        perf_root = root + 'έξ'
                        if not active_subjunctive_sigmatic_exists(perf_root):
                            perf_root = root + 'ήξ'
                            if not active_subjunctive_sigmatic_exists(perf_root):
                                perf_root = root + 'ίσ'
                                if not active_subjunctive_sigmatic_exists(perf_root) and root[-2:] in ['χν', 'ρν',
                                                                                                       'λν']:
                                    perf_root = root[:-1] + 'ίσ'

                                if not active_subjunctive_sigmatic_exists(perf_root):
                                    perf_root = root + 'ήσ'
                                    if not active_subjunctive_sigmatic_exists(perf_root) and not verb.endswith('άω'):
                                        perf_root = ''
        # special case for compounds with ποιω that are not in my db for some reasons

        if root[-3:] == 'ποι' and pres_conjugation in [CON2B_ACT, CON2B_PASS]:
            perf_root = root + 'ήσ'

    elif pres_conjugation == CON2C_ACT and not perf_root:

        if root[-2:] == 'ού' and not perf_root:
            # akouw
            perf_root = root + 'σ'
        elif root[-2:] in diphtongs:
            perf_root = root[:-2] + 'άψ'

        else:
            perf_root = root[:-1] + 'άψ'

    elif pres_conjugation == CON2D_ACT and not perf_root:
        # archaic on o
        perf_root = root + 'ώσ'

    if verb.endswith('βαίνω') and verb[:-5] in prefixes_before_augment:
        perf_root = verb[:-5] + 'β'

    if perf_root:
        return perf_root
