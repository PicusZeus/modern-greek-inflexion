from modern_greek_inflexion.resources import greek_corpus
from modern_greek_accentuation.accentuation import remove_all_diacritics, put_accent_on_the_penultimate
from modern_greek_accentuation.syllabify import count_syllables


def create_imp_pass(perf_pass_root: str) -> str:
    # useful for deponentia

    if perf_pass_root[-2:] in ['φτ', 'φθ']:
        form = perf_pass_root[:-2] + 'ψου'
    elif perf_pass_root[-2:] in ['χτ', 'χθ']:
        form = perf_pass_root[:-2] + 'ξου'
    elif perf_pass_root[-2:] == 'στ':
        form = perf_pass_root[:-2] + 'σου'
    elif perf_pass_root[-1] == 'θ':
        form = perf_pass_root[:-1] + 'σου'
    elif perf_pass_root[-3:] == 'ευτ':
        form = perf_pass_root[:-3] + 'έψου'
    else:
        form = None
    if form:
        form = remove_all_diacritics(form)
        form = put_accent_on_the_penultimate(form)
    if form in greek_corpus and count_syllables(form) > 1:
        return form
    else:
        return ''

