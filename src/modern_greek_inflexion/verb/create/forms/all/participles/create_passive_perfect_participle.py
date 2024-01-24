from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate
from modern_greek_accentuation.augmentify import add_augment

from modern_greek_inflexion.resources import greek_corpus
from modern_greek_inflexion.resources.verb import irregular_passive_perfect_participles


def create_passive_perfect_participle(pres_form: str, root: str, act_root: str, passive_root: str) -> str:
    passive_perfect_participles = []
    reg_passive_perfect_participles = []
    # check for irregularities
    for pr_f in irregular_passive_perfect_participles.keys():

        if pr_f == pres_form and not irregular_passive_perfect_participles[pr_f]:
            return ''

        elif pr_f == pres_form[-(len(pr_f)):] and irregular_passive_perfect_participles[pr_f]:

            part = pres_form[:-len(pr_f)] + irregular_passive_perfect_participles[pr_f]

            part_aug = add_augment(part)

            passive_perfect_participles = [part]

            for p in part_aug:
                if p in greek_corpus:
                    passive_perfect_participles.append(p)

            passive_perfect_participles = [p for p in passive_perfect_participles if p in greek_corpus]
            break

    if passive_root:

        for passive_root in passive_root.split(','):

            if passive_root[-2:] == 'νθ':
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'σμενος')
            elif passive_root[-2:] == 'στ':
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')

            elif passive_root[-1] == 'θ':
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
            elif passive_root[-2:] == 'φτ':
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'μμενος')
            elif passive_root[-1] == 'φ':
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μμενος')

            elif passive_root[-3:] == 'ευτ':
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'μενος')
                if act_root and act_root[-1] == 'σ':
                    passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
                if passive_perfect_participle not in greek_corpus:
                    passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-1] + 'μενος')
            elif passive_root[-3:] in ['γχτ', 'γχθ']:

                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-3] + 'γμενος')

            elif passive_root[-2:] in ['χτ', 'χθ']:
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root[:-2] + 'γμενος')

            else:
                passive_perfect_participle = put_accent_on_the_penultimate(passive_root + 'μένος')

            reg_passive_perfect_participles.extend(add_augment(passive_perfect_participle))

            reg_passive_perfect_participles = [f for f in reg_passive_perfect_participles if f in greek_corpus]
            if root[-3:] == 'ποι':
                reg_passive_perfect_participles = [root + 'ημένος']
            if root[-3:] == 'ιστ' and passive_root[-3:] == 'αστ':
                passive_perfect_participle = passive_root + 'ημένος'
                reg_passive_perfect_participles = add_augment(passive_perfect_participle)
                reg_passive_perfect_participles = [f for f in reg_passive_perfect_participles if f in greek_corpus]

            if root[-1] in ['λ', 'ρ'] and root + 'εμένος' in greek_corpus:
                reg_passive_perfect_participles.append(root + 'εμένος')

    if not reg_passive_perfect_participles and act_root:

        if act_root[-2:] in ['ύσ', 'άσ', 'ίσ']:
            passive_perfect_participle = put_accent_on_the_penultimate(act_root + 'μενος')
        elif act_root[-1] in ['σ', 'ν'] and act_root[-2:] != 'άν':
            passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-1] + 'μενος')
            if passive_perfect_participle not in greek_corpus:
                passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-1] + 'σμενος')
        elif act_root[-1] == 'ξ':
            passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-1] + 'γμενος')
        elif act_root[-1] == 'ψ':
            passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-1] + 'uμενος')

        elif len(pres_form) > 4 and pres_form[-4:] == 'αίνω' and act_root[-2:] == 'άν':

            passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-2] + 'αμενος')

            if passive_perfect_participle not in greek_corpus:
                passive_perfect_participle = put_accent_on_the_penultimate(act_root[:-2] + 'ημενος')
        else:
            passive_perfect_participle = put_accent_on_the_penultimate(act_root + 'μενος')
        if passive_perfect_participle:
            reg_passive_perfect_participles = add_augment(passive_perfect_participle)

            reg_passive_perfect_participles = [f for f in reg_passive_perfect_participles if f in greek_corpus]
        if not reg_passive_perfect_participles:
            if root + 'ισμένος' in greek_corpus:
                reg_passive_perfect_participles.append(put_accent_on_the_penultimate(root + 'ισμένος'))

    if reg_passive_perfect_participles:
        # these are all possible participles in masc sg!!!
        if 'παρμένος' in reg_passive_perfect_participles:
            # since επαιρομαι is kinda περνομαι but not really, not an elegand trick, but if more such situations occure, better solution should be found
            reg_passive_perfect_participles = ['παρμένος']
        reg_passive_perfect_participles = list(set(reg_passive_perfect_participles))
    if passive_perfect_participles:
        reg_passive_perfect_participles.extend(passive_perfect_participles)

    all_passive_perfect_participles = ','.join(reg_passive_perfect_participles)

    return all_passive_perfect_participles

