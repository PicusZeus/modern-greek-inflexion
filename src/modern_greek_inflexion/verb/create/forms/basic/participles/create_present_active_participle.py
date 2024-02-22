from __future__ import annotations

from modern_greek_inflexion.resources import CON1_ACT, CON2A_ACT, CON2B_ACT, CON2D_ACT, CON2AK_ACT, CON2C_ACT, \
    EIMAI
from modern_greek_inflexion.resources.typing import presentConjugationType


def create_present_active_participle(_: str,
                                     root: str,
                                     pres_conjugation: presentConjugationType) -> str:
    """
    Creates present active participles
    :param _: ignored
    :param root: present tense stem
    :param pres_conjugation: present conjugation type
    :return: present active participle as string
    """
    pres_part_act = ''

    if pres_conjugation == CON1_ACT:
        pres_part_act = root + 'οντας'

    elif pres_conjugation in [CON2A_ACT, CON2B_ACT, CON2D_ACT, CON2AK_ACT]:
        pres_part_act = root + 'ώντας'

    elif pres_conjugation == CON2C_ACT and root != 'πά':
        pres_part_act = root + 'γοντας'

    elif pres_conjugation == EIMAI:
        pres_part_act = root + 'όντας'

    return pres_part_act

