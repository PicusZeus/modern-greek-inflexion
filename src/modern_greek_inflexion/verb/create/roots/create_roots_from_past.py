from modern_greek_accentuation.augmentify import deaugment_stem, deaugment_prefixed_form


def create_stem_from_augmented_past(past_form: str, pres_form: str) -> str:
    """
    This function creates deaugmented stem
    :param past_form: past 1st sg form
    :param pres_form: present simple 1st sg form
    :return: deaugmented stem
    """
    # argument only in 1st person

    if past_form[-1] in ['α']:
        stem = past_form[:-1]
    else:
        return None
    deaugmented_stem = deaugment_stem(stem, pres_form)
    deaugmented_stem_prefixed = deaugment_prefixed_form(stem)
    if deaugmented_stem:
        return deaugmented_stem
    else:
        return deaugmented_stem_prefixed
