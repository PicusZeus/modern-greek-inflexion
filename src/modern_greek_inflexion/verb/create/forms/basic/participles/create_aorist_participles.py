from __future__ import annotations

from modern_greek_accentuation.accentuation import put_accent_on_the_ultimate, put_accent_on_the_penultimate

from modern_greek_inflexion.resources import greek_corpus


def create_active_aorist_participle(pres_root: str, act_roots: str) -> str:
    """
    This function creates basic forms for active aorist participle
    :param pres_root: present tense stem, used to check only in case of βαίνω compounds
    :param act_roots: perfect active stem
    :return: Basic forms as string ("masc/fem/neut"), if multiple, separated by coma.
    """
    result = []
    for act_root in act_roots.split(','):
        active_aorist_participles = None
        masc = act_root + 'ας'
        fem = act_root + 'ασα'
        neut = act_root + 'αν'

        masc_b = act_root + 'άς'
        fem_b = act_root + 'άσα'
        neut_b = act_root + 'άν'

        masc_wn = put_accent_on_the_ultimate(act_root + 'ων')
        fem_ousa = put_accent_on_the_penultimate(act_root + 'ουσα')
        neut_on = put_accent_on_the_ultimate(act_root + 'ον')

        if masc in greek_corpus and fem in greek_corpus:
            active_aorist_participles = masc + '/' + fem + '/' + neut
            # on as
        elif (act_root[-1] not in ['σ', 'ξ', 'ψ'] and
              masc_wn in greek_corpus and
              fem_ousa in greek_corpus and
              act_root not in ['πάρ']):

            active_aorist_participles = masc_wn + '/' + fem_ousa + '/' + neut_on

        elif act_root.endswith('β') and pres_root == 'βαίν':
            active_aorist_participles = masc_b + '/' + fem_b + '/' + neut_b

        if active_aorist_participles:
            result.append(active_aorist_participles)

    return ','.join(result)


def create_passive_aorist_participle(passive_root: str) -> str:
    """
    This function creates basic forms for passive aorist participle, if it is found in the language corpus
    :param passive_root: passive perfect root
    :return: Basic forms as string ("masc/fem/neut"), if multiple, separated by coma.
    """
    pass_aor_part = None
    if (passive_root + 'είσα' in greek_corpus or
            passive_root + 'έντες' in greek_corpus or
            passive_root + 'έντα' in greek_corpus or
            passive_root in ['σπαρ']):
        pass_aor_part = passive_root + 'είς/' + passive_root + 'είσα/' + passive_root + 'έν'
    elif (passive_root.endswith('στ') and passive_root + 'άς' in greek_corpus or
            passive_root + 'άντες' in greek_corpus or
            passive_root + 'άντα' in greek_corpus):
        pass_aor_part = passive_root + 'άς/' + passive_root + 'άσα/' + passive_root + 'άν'

    return pass_aor_part
