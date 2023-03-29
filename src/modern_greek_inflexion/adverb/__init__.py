from .. import adjective
from ..resources import irregular_adv, ADV, COMP_ADV, ADJ, COMP, SUPERL, SUPERL_ADV
from ..exceptions import NotInGreekException
import re
greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)


def create_all(adverb):
    # adverb = convert_to_monotonic(adverb, one_syllable_rule=False)
    if not greek_pattern.match(adverb):
        raise NotInGreekException
    """
    :param adverb:
    :return: returns a dictionary:
    'adv' the same adverb
    'comp_adv' if exists is given in an array
    'superl_adv' if exists is given in an array
    'comp' if exists adj comp created from a given adverb, dictionary is given in an array
    'superl' if exists adj superl created from a given adverb, dictionary is given in an array

    """

    if adverb in irregular_adv:
        result = {ADV: {adverb}}
        comp_adv, superl_adv = irregular_adv[adverb][COMP_ADV].split('/')
        result[COMP_ADV] = {comp_adv}
        result[SUPERL_ADV] = {superl_adv}
        if COMP in irregular_adv[adverb]:
            comp_base, superl_base = irregular_adv[adverb][COMP].split('/')
            comp = adjective.create_all(comp_base)[ADJ]
            superl = adjective.create_all(superl_base)[ADJ]
            result[COMP] = comp
            result[SUPERL] = superl

        return result
    else:

        return {ADV: {adverb}}
