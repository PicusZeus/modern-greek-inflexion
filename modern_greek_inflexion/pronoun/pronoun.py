from .create_pron_basic import create_basic_forms
from .create_pron_decl import create_all_pron_forms


def create_all(adj):

    bas_form = create_basic_forms(adj)
    res = create_all_pron_forms(bas_form)
    return res

