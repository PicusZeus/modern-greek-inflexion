from .create_pron_basic import create_basic_forms
from .create_pron_decl import create_all_pron_forms
from ..helping_functions import merging_all_dictionaries


def create_all(pron, strong=True):

    bas_form = create_basic_forms(pron)
    res = create_all_pron_forms(bas_form, strong=strong)
    res = merging_all_dictionaries(res)
    return res

