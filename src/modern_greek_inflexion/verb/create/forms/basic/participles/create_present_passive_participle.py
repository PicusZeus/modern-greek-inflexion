from modern_greek_accentuation.accentuation import remove_all_diacritics, put_accent_on_the_antepenultimate

from modern_greek_inflexion.resources.typing import presentConjugationType
from modern_greek_inflexion.resources.variables import CON1_PASS, CON1_ACT, CON2AK_ACT, CON2A_ACT, CON2AK_PASS, CON2A_PASS, \
    CON2C_ACT, CON2B_ACT, CON2B_PASS, CON2C_PASS, CON2D_ACT, CON2E_PASS, CON2D_PASS
from modern_greek_inflexion.resources import greek_corpus


def passive_present_participle_exists(participle: str) -> bool:
    """
    This function checks if a participle exists in the language corpus
    :param participle: nom sg masc
    :return: False or True
       """
    masc = participle
    neut = participle[:-1]
    fem = participle[:-2] + 'η'
    neut_pl = participle[:-2] + 'α'
    return masc in greek_corpus or neut in greek_corpus or fem in greek_corpus or neut_pl in greek_corpus


def create_present_passive_participle(_: str,
                                      root: str,
                                      pres_conjugation: presentConjugationType) -> str:
    """
    Creates present passive participles
    :param _:
    :param root: present tense stem
    :param pres_conjugation: present tense conjugation type
    :return: Basic forms as string ("masc/fem/neut"), if multiple, separated by coma.
    """
    pres_part_pass = []
    part_root = remove_all_diacritics(root)

    if pres_conjugation in [CON1_ACT, CON1_PASS]:
        pres_part_pass = [part_root + 'όμενος', part_root + 'ούμενος', part_root + 'έμενος']

    elif pres_conjugation in [CON2A_ACT, CON2AK_PASS, CON2A_PASS, CON2AK_ACT]:
        pres_part_pass = [part_root + 'ώμενος', part_root + 'ούμενος', part_root + 'άμενος']

    elif pres_conjugation == CON2C_ACT:
        pres_part_pass = [part_root + 'γόμενος']

    elif pres_conjugation in [CON2B_ACT, CON2B_PASS, CON2C_PASS, CON2D_ACT]:

        pres_part_pass = [part_root + 'ούμενος']
    elif pres_conjugation == CON2E_PASS:
        pres_part_pass = [part_root + 'άμενος']
    elif pres_conjugation == CON2D_PASS:
        pres_part_pass = [put_accent_on_the_antepenultimate(root + 'μενος')]

    # special case for xairomai
    if part_root == 'χαιρ':
        pres_part_pass = ['χαρούμενος']

    present_passive_participle = [part for part in pres_part_pass if passive_present_participle_exists(part)]

    return ','.join([f'{p}/{p[:-2]}η/{p[:-1]}' for p in present_passive_participle])

