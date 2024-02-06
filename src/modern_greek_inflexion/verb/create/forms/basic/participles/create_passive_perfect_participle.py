from __future__ import annotations
from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate
from modern_greek_accentuation.augmentify import add_augment

from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.verb import irregular_passive_perfect_participles


def create_passive_perfect_participle(pres_form: str, root: str, act_root: str, passive_root: str) -> str:
    passive_perfect_participles = []

    if pres_form in irregular_passive_perfect_participles:
        return irregular_passive_perfect_participles[pres_form]

    else:
        for pr_f in irregular_passive_perfect_participles.keys():

            if pr_f == pres_form[-(len(pr_f)):] and irregular_passive_perfect_participles[pr_f]:
                part = pres_form[:-len(pr_f)] + irregular_passive_perfect_participles[pr_f]

                passive_perfect_participles.append(part)

    if passive_root:

        for passive_root in passive_root.split(','):

            if passive_root[-2:] == 'νθ':
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-2] + 'σμενος'))
            elif passive_root.endswith('αστ') and root.endswith('στ'):
                passive_perfect_participles.append(passive_root + 'ημένος')
            elif passive_root.endswith('στ') and len(passive_root) > 3:
                # passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root + 'μενος'))
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-1] + 'μενος'))
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-2] + 'μενος'))

            elif passive_root[-2:] == 'φτ':
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-2] + 'μμενος'))
            elif passive_root[-1] == 'φ':
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-1] + 'μμενος'))

            elif passive_root[-3:] == 'ευτ':
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-2] + 'μενος'))

                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-1] + 'μενος'))
            elif passive_root[-3:] in ['γχτ', 'γχθ']:

                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-3] + 'γμενος'))

            elif passive_root[-2:] in ['χτ', 'χθ']:
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-2] + 'γμενος'))

            elif passive_root[-1] == 'θ' and not passive_root.endswith('σθ'):
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-1] + 'μενος'))
                # if passive_root.endswith('αθ'):
                #     passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root[:-2] + 'ημενος'))

            else:
                passive_perfect_participles.append(put_accent_on_the_penultimate(passive_root + 'μένος'))

    if act_root:

        if act_root[-2:] in ['ύσ', 'άσ', 'ίσ']:
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root + 'μενος'))

        elif pres_form.endswith('αίνω') and act_root.endswith('άν'):

            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-2] + 'αμενος'))

            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-2] + 'ημενος'))

        elif act_root.endswith('ήσ'):
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-1] + 'μενος'))
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root + 'μενος'))

            if root.endswith('ρ'):
                passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-2] + 'εμενος'))

            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-2] + 'ισμενος'))

        elif act_root[-1] in ['σ', 'ν'] and act_root[-2:] != 'άν':
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-1] + 'μενος'))
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-1] + 'σμενος'))
        elif act_root[-1] == 'ξ':
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-1] + 'γμενος'))
        elif act_root[-1] == 'ψ':
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-1] + 'uμενος'))
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-1] + 'μενος'))
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root[:-1] + 'μμενος'))

        elif act_root.endswith('ρ') or act_root.endswith('λ'):
            passive_perfect_participles.append(put_accent_on_the_penultimate(root + 'ισμένος'))
            passive_perfect_participles.append(put_accent_on_the_penultimate(root + 'εμένος'))
        else:
            passive_perfect_participles.append(put_accent_on_the_penultimate(act_root + 'μενος'))

    participles_augmented = []
    for p in passive_perfect_participles:
        participles_augmented.extend(add_augment(p))

    passive_perfect_participles.extend(participles_augmented)
    passive_perfect_participles = [p for p in passive_perfect_participles if
                                   p in greek_corpus or p[:-1] in greek_corpus]

    return ",".join(passive_perfect_participles)
