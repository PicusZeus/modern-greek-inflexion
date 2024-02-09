from __future__ import annotations

from modern_greek_accentuation.accentuation import *

from modern_greek_inflexion.resources.verb import irregular_passive_roots
from modern_greek_inflexion.resources.variables import *
from modern_greek_inflexion.verb.helpers import passive_subjunctive_exists


def create_regular_perf_passive_root(verb: str, act_perf_root: str | None = None,
                                     pres_conjugation: str = None,
                                     root: str = None) -> str | None:
    # create regular aorist roots from present root. For obvious reasons it's only useful for verbs you don't have
    # supplied aorist forms and so it is prone to errors that cannot be eliminated
    perf_root = None
    irregular = False

    multiple_stems = None

    if pres_conjugation == MODAL:
        perf_root = root

    if verb in irregular_passive_roots:

        return irregular_passive_roots[verb]

    for ir_verb, ir_root in sorted(irregular_passive_roots.items(), key=lambda key: len(key[0]), reverse=True):

        if ir_root:
            # that is if many stems
            multiple_perf_roots = []
            for stem in ir_root.split(','):
                if len(root) >= len(ir_verb) and root[-len(ir_verb):] == ir_verb:
                    prefix = root[:-len(ir_verb)]
                    beta_perf_root = prefix + stem
                    if passive_subjunctive_exists(beta_perf_root):
                        multiple_perf_roots.append(beta_perf_root)

            if multiple_perf_roots:
                perf_root = ','.join(multiple_perf_roots)
                irregular = True
                multiple_stems = True
                break

    if not irregular:
        if pres_conjugation in [CON1_ACT, CON1_PASS, CON1_PASS_MODAL, CON2D_PASS]:

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
                                perf_root = root[:-2] + 'χθ'
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
                    multiple_stems = True

            elif root[-2:] in ['πτ', 'φτ']:
                perf_root = root[:-2] + 'φτ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root[:-2] + 'φθ'
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
                    perf_root = root[:-1] + 'χθ'
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
                    # if not passive_subjunctive_exists(perf_root):
                    #     perf_root = ''

            elif root.endswith('λλ'):
                perf_root = root[:-1] + 'θ'
                # if not passive_subjunctive_exists(perf_root):
                #     perf_root = ''

            elif root.endswith('εμ'):
                perf_root = root + 'ηθ'
                # if not passive_subjunctive_exists(perf_root):
                #     perf_root = ''

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

            # elif root.endswith('υρ'):

            elif root.endswith('ρ'):
                perf_root = root + 'θ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root + 'ιστ'
                    if not passive_subjunctive_exists(perf_root):
                        perf_root = root + 'ηθ'

        elif pres_conjugation in [CON2A_ACT, CON2B_ACT, CON2C_ACT, CON2A_PASS, CON2B_PASS, CON2E_PASS,
                                  CON2C_PASS, CON2AK_PASS, CON2AK_ACT, CON2_PASS_MODAL]:

            perf_root = root + 'ηθ'

            if root[-2:] in ['ρν', 'χν', 'λν'] and not passive_subjunctive_exists(perf_root):
                perf_root = root[:-1] + 'αστ'

            elif not passive_subjunctive_exists(perf_root):
                perf_root = root + "αχτ"
                alt_perf_root = root + 'ηχτ'
                if passive_subjunctive_exists(perf_root) and passive_subjunctive_exists(alt_perf_root):
                    perf_root = perf_root + ',' + alt_perf_root
                    multiple_stems = True
            elif passive_subjunctive_exists(root + 'ηχτ'):
                alt_perf_root = root + 'ηχτ'
                perf_root = perf_root + ',' + alt_perf_root
                multiple_stems = True
            # εξαιρέσεις
            if not passive_subjunctive_exists(perf_root) and not multiple_stems:
                perf_root = root + 'αστ'
                if not passive_subjunctive_exists(perf_root):
                    perf_root = root + 'εστ'
                    if not passive_subjunctive_exists(perf_root):
                        perf_root = root + "αθ"
                        if not passive_subjunctive_exists(perf_root):
                            perf_root = root + "εθ"
                            if not passive_subjunctive_exists(perf_root) and pres_conjugation not in [CON2AK_PASS]:
                                perf_root = root + "εχτ"
                                if not passive_subjunctive_exists(perf_root) and pres_conjugation not in [CON2AK_PASS]:
                                    perf_root = root + "εχθ"
                                    if not passive_subjunctive_exists(perf_root) and pres_conjugation not in [
                                        CON2AK_PASS]:
                                        perf_root = root + "ηχτ"
                                        if not passive_subjunctive_exists(perf_root) and pres_conjugation not in [
                                            CON2AK_PASS]:
                                            perf_root = root + "ηχθ"
                                            if not passive_subjunctive_exists(perf_root) and pres_conjugation not in [
                                                CON2AK_PASS]:
                                                perf_root = root + "ιστ"

                # σπεσιαλ case for compounds with poiw
                if root[-3:] == 'ποι' and pres_conjugation in [CON2B_ACT, CON2B_PASS]:
                    perf_root = root + 'ηθ'
                    multiple_stems = True

        elif pres_conjugation in [CON2D_ACT, CON2F_PASS]:

            perf_root = root + 'ωθ'
    if perf_root:
        perf_root = remove_all_diacritics(perf_root)

    if perf_root and (multiple_stems or passive_subjunctive_exists(perf_root)):
        return perf_root

