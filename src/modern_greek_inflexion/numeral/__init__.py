from __future__ import annotations

from .create_num_decl import create_all_num_adj_forms
from .create_num_list import create_num_adj
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from ..adjective import Adjective
from ..noun import Noun
from ..resources import greek_pattern
from ..resources.numerals import cardinal_irregulars
from ..resources.variables import ADJ, ADV
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..exceptions import NotInGreekException
from ..resources.typing import genders_declensions_type


class Numeral:
    """
    This class can be used to create inflected forms of numerals. Most numerals behave like adjectives, but there are also ones, that can be viewed as nouns, because of that you should supply this info during instantiation, but you can also hope that it will be correctly guessed by algorithm.

    :param numeral: nominative singular or plural
    :type numeral: str
    :param pos: if you know it is a noun numeral, set it to 'noun', otherwise set 'adj' or leave it out.
    :type pos: str, optional
    """
    def __init__(self, numeral: str, pos: str = ADJ):

        numeral = convert_to_monotonic(numeral, one_syllable_rule=False)
        if not greek_pattern.match(numeral):
            raise NotInGreekException
        self.numeral = numeral
        self.pos = pos

    def all(self) -> {ADJ: genders_declensions_type, ADV: set[str], COMP: genders_declensions_type, COMP_ADV: set[str],
                      SUPERL: genders_declensions_type, SUPERL_ADV: set[str]} | genders_declensions_type:
        """
        This method will create all the inflected forms.

        :return: If numeral is of noun type it returns a dictionary of the following shape ``{SG: {MASC: {NOM: set(forms), ...}, ...}``, but if the numeral is of adjective type it returns a dictionary of this shape ''{ADJ: {SG: {MASC: {NOM: set(forms), ...}, ...}}''
        "rtype: dict
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

