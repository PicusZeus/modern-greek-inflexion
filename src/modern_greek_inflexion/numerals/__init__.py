from __future__ import annotations

from .create_num_decl import create_all_num_adj_forms
from .create_num_list import create_num_adj
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from ..adjective import Adjective
from ..noun import Noun
from ..resources import greek_pattern
from ..resources.resources import ADJ, ADV
from modern_greek_accentuation.accentuation import convert_to_monotonic
from .._exceptions import NotInGreekException
from ..resources.typing import declension_forms_type

cardinal_irregulars = ['δεύτερος', 'τρίτος', 'τέταρτος', 'πέμπτος', 'έκτος', 'έβδομος', 'όγδοος', 'ένατος', 'δέκατος']


class Numeral:
    """
    This class creates numerals
    """
    def __init__(self, numeral: str, pos: str = ADJ):
        """

        :param numeral: str, nom singular or plural
        :param pos: Either ADJ or NOUN
        """
        numeral = convert_to_monotonic(numeral, one_syllable_rule=False)
        if not greek_pattern.match(numeral):
            raise NotInGreekException
        self.numeral = numeral
        self.pos = pos

    def all(self) -> dict[ADJ: declension_forms_type] | declension_forms_type:
        """
        Numerals can be divided into adjective types or noun types
        :return: If numeral is of noun type it returns a dictionary {SG: {MASC: {NOM: set(forms), ...}, ...},
        if numeral is of adjective type it returns a dictionary {ADJ: {SG: {MASC: {NOM: set(forms), ...}, ...}}
        """
        if self.pos == ADJ:
            if self.numeral[-2:] in ['ος', 'ός']:
                # true cardinals
                if self.numeral in cardinal_irregulars or self.numeral.endswith('στός'):
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

