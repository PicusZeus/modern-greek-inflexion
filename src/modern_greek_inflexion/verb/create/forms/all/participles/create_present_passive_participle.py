from modern_greek_accentuation.accentuation import remove_all_diacritics, put_accent_on_the_antepenultimate

from modern_greek_inflexion.resources import CON1_PASS, CON1_ACT, CON2A_ACT_LOGIA, CON2A_ACT, CON2AB_PASS, CON2A_PASS, \
    CON2C_ACT, CON2B_ACT, CON2B_PASS, CON2C_PASS, CON2D_ACT, CON2E_PASS, CON2D_PASS, greek_corpus


def create_present_passive_participle(_: str, root: str, pres_conjugation: str) -> str:
    pres_part_pass = []
    part_root = remove_all_diacritics(root)

    if pres_conjugation in [CON1_ACT, CON1_PASS]:
        pres_part_pass = [part_root + 'όμενος']

    elif pres_conjugation == CON2A_ACT_LOGIA:
        pres_part_pass = [part_root + 'άμενος', part_root + 'ώμενος']

    elif pres_conjugation in [CON2A_ACT, CON2AB_PASS, CON2A_PASS]:
        pres_part_pass = [part_root + 'ώμενος', part_root + 'ούμενος']

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

    present_passive_participle = [part for part in pres_part_pass if part in greek_corpus]

    return ','.join(present_passive_participle)
