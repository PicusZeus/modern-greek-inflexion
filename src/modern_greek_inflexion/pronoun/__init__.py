from .create_pron_basic import create_basic_forms
from .create_pron_decl import create_all_pron_forms
from ..helping_functions import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic


def create_all(pron, strong=True):
    pron = convert_to_monotonic(pron, one_syllable_rule=False)

    bas_form = create_basic_forms(pron)
    res = create_all_pron_forms(bas_form, strong=strong)
    res = merging_all_dictionaries(res)
    return res

