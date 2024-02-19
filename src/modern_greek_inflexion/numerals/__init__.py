from .create_num_decl import create_all_num_adj_forms
from .create_num_list import create_num_adj
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from ..adjective import Adjective
from ..noun import Noun
from ..resources import greek_pattern
from ..resources.resources import ADJ, ADV
from modern_greek_accentuation.accentuation import convert_to_monotonic
from .._exceptions import NotInGreekException


class Numeral:

    def __init__(self, numeral: str, pos: str = ADJ):
        numeral = convert_to_monotonic(numeral, one_syllable_rule=False)
        if not greek_pattern.match(numeral):
            raise NotInGreekException
        self.numeral = numeral
        self.pos = pos

    def all(self) -> dict:
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

