from .. import adjective
from ..adjective import Adjective
from ..resources import greek_pattern
from ..resources.adv import irregular_adv
from modern_greek_inflexion.resources.variables import ADV, COMP_ADV, ADJ, COMP, SUPERL, SUPERL_ADV
from ..exceptions import NotInGreekException
from ..resources.typing import declension_forms_type


class Adverb:
    """
    This class can be used to create adverb forms
    """

    def __init__(self, adverb: str):
        """
        :param adverb: an adverb form
        """
        if not greek_pattern.match(adverb):
            raise NotInGreekException
        self.adverb = adverb

    def all(self) -> dict[ADV: set[str], COMP_ADV: set[str], SUPERL_ADV: set[str], SUPERL: declension_forms_type,
                          COMP: declension_forms_type]:
        """
        Checks if an adverb belongs to irregular ones that creates comparative and superlative degree
        :return: A dictionary always with an ADV key, and if it's an adverb that creates comparative or/and
        superlative degree, there are also additional forms under COMP_ADV, SUPERL_ADV, COMP, SUPERL keys.
        """
        if self.adverb in irregular_adv:
            result = {ADV: {self.adverb}}
            comp_adv, superl_adv = irregular_adv[self.adverb][COMP_ADV].split('/')
            result[COMP_ADV] = {comp_adv}
            result[SUPERL_ADV] = {superl_adv}
            if COMP in irregular_adv[self.adverb]:
                comp_base, superl_base = irregular_adv[self.adverb][COMP].split('/')
                comp = Adjective(comp_base).all()[ADJ]
                superl = Adjective(superl_base).all()[ADJ]
                result[COMP] = comp
                result[SUPERL] = superl

            return result
        else:

            return {ADV: {self.adverb}}


