from __future__ import annotations

from icecream import ic
from modern_greek_accentuation.augmentify import deaugment_stem, deaugment_prefixed_form


def create_roots_from_past(verb: str, lemma: str) -> str | None:
    # argument only in 1st person

    res = None
    if verb[-1] in ['α']:
        stem = verb[:-1]
    else:
        return None
    deaugmented_stem = deaugment_stem(stem, lemma)
    deaugmented_stem_prefixed = deaugment_prefixed_form(stem)
    if deaugmented_stem:
        return deaugmented_stem
    else:

        if verb == 'συνελάμβανα':
            ic(deaugmented_stem_prefixed)
        return deaugmented_stem_prefixed






    # if deaugmented_stem:
    #     res = deaugmented_stem
    # elif deaugmented_stem_prefixed:
    #     res = deaugmented_stem_prefixed
    # return res

