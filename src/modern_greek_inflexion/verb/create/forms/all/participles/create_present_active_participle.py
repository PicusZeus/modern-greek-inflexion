from __future__ import annotations

from modern_greek_inflexion.resources import CON1_ACT, CON2A_ACT, CON2B_ACT, CON2D_ACT, CON2A_ACT_LOGIA, CON2C_ACT, \
    EIMAI


def create_present_active_participle(_: str, root: str, pres_conjugation: str) -> str | None:
    pres_part_act = ''

    if pres_conjugation == CON1_ACT:
        pres_part_act = root + 'οντας'

    elif pres_conjugation in [CON2A_ACT, CON2B_ACT, CON2D_ACT, CON2A_ACT_LOGIA]:
        pres_part_act = root + 'ώντας'

    elif pres_conjugation == CON2C_ACT and root != 'πά':
        pres_part_act = root + 'γοντας'

    elif pres_conjugation == EIMAI:
        pres_part_act = root + 'όντας'

    # if pres_part_act and pres_part_act in greek_corpus or root[-3:] == 'ποι':
    #     return pres_part_act
    # else:
    #     return None

    return pres_part_act

