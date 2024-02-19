from .create_num_decl import create_all_num_adj_forms
from .create_num_list import create_num_adj
from .. import adjective
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from .. import noun
from ..adjective import Adjective
from ..noun import Noun
from ..resources.resources import ADJ, ADV
from modern_greek_accentuation.accentuation import convert_to_monotonic
from .._exceptions import NotInGreekException
import re
greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)


class Numeral:

    def __init__(self, numeral, pos=ADJ):
        numeral = convert_to_monotonic(numeral, one_syllable_rule=False)
        if not greek_pattern.match(numeral):
            raise NotInGreekException
        self.numeral = numeral
        self.pos = pos

    def all(self):
        if self.pos == ADJ:
            if self.numeral[-2:] in ['ος', 'ός']:
                # true cardinals
                if self.numeral in ['δεύτερος', 'τρίτος', 'τέταρτος', 'πέμπτος', 'έκτος', 'έβδομος', 'όγδοος', 'ένατος', 'δέκατος'] or self.numeral.endswith('στός'):
                    base_adj = create_num_adj(self.numeral, cardinal=True)
                    forms_adj = create_all_num_adj_forms(base_adj[ADJ], cardinal=True)
                    adverbs = [adv for adv in base_adj['adverb'].split(',')]
                    forms = {ADJ: forms_adj, ADV: set(adverbs)}
                    forms = merging_all_dictionaries(forms)
                else:
                    # they can be treated as common adjectives otherwise, special case is protos
                    forms = Adjective(self.numeral).all()

                    if self.numeral == 'πρώτος':
                        forms[ADV] = {'πρώτον', 'πρώτα'}
                    forms = merging_all_dictionaries(forms)
            else:
                base_adj = create_num_adj(self.numeral)

                forms_adj = create_all_num_adj_forms(base_adj[ADJ])
                forms = {ADJ: forms_adj}
                forms = merging_all_dictionaries(forms)
        else:
            forms = Noun(self.numeral).all()

        return forms

def create_all_adj_num(base_form: str) -> dict:

    """
    :param base_form: base neuter form of a numeral, in case of ordinals, masc
    :return: dict with all possible forms
    """
    base_form = convert_to_monotonic(base_form, one_syllable_rule=False)
    if not greek_pattern.match(base_form):
        raise NotInGreekException

    # ordinal or not, it should be assumed, as I don't know about any exception,
    # that ordinals and alike have base_form that ends on os

    if base_form[-2:] in ['ος', 'ός']:
        # true ordinals
        if base_form in ['δεύτερος', 'τρίτος', 'τέταρτος', 'πέμπτος', 'έκτος', 'έβδομος', 'όγδοος', 'ένατος',
                         'δέκατος'] or base_form[-4:] == 'στός':
            base_adj = create_num_adj(base_form, cardinal=True)
            forms_adj = create_all_num_adj_forms(base_adj[ADJ], cardinal=True)
            adverbs = [adv for adv in base_adj['adverb'].split(',')]
            forms = {ADJ: forms_adj, ADV: set(adverbs)}
            forms = merging_all_dictionaries(forms)
        else:
            # they can be treated as common adjectives otherwise, special case is protos
            forms = adjective.create_all(base_form)

            if base_form == 'πρώτος':
                forms[ADV] = {'πρώτον', 'πρώτα'}
            forms = merging_all_dictionaries(forms)
    else:
        base_adj = create_num_adj(base_form)

        forms_adj = create_all_num_adj_forms(base_adj[ADJ])
        forms = {ADJ: forms_adj}
        forms = merging_all_dictionaries(forms)

    return forms


def create_all_noun_num(base_form: str) -> dict:
    """
    There is no real difference between noun and quant noun, so noun logic employed
    :param base_form: base form
    :return: dict with all forms
    """
    return noun.create_all(base_form)
