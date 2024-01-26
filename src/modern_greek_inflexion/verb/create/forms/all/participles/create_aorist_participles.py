from __future__ import annotations

from modern_greek_accentuation.accentuation import put_accent_on_the_ultimate, put_accent_on_the_penultimate

from modern_greek_inflexion.resources import greek_corpus


def create_active_aorist_participle(_: str, act_roots: str) -> str:
    result = []
    for act_root in act_roots.split(','):
        active_aorist_participles = None
        masc = act_root + 'ας'
        fem = act_root + 'ασα'
        neut = act_root + 'αν'

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

        if active_aorist_participles:
            result.append(active_aorist_participles)

    return ','.join(result)


def create_passive_aorist_participle(passive_root: str) -> str | None:
    if (passive_root + 'είσα' in greek_corpus or
            passive_root + 'έντες' in greek_corpus or
            passive_root + 'έντα' in greek_corpus or
            passive_root in ['σπαρ']):
        return passive_root + 'είς/' + passive_root + 'είσα/' + passive_root + 'έν'
    else:
        return None
