from modern_greek_accentuation.accentuation import (put_accent_on_the_ultimate,
                                                    put_accent_on_the_penultimate,
                                                    remove_all_diacritics)

from modern_greek_inflexion.resources import CON1_ACT, greek_corpus, CON2A_ACT, CON2B_ACT, CON2D_ACT, CON2AK_ACT, \
    CON2C_ACT, EIMAI


def check_participle_existence(masc: str, gen: str, neut_pl: str) -> bool:
    return masc in greek_corpus and (gen in greek_corpus or neut_pl in greek_corpus)


def create_present_active_participle_arch(_: str, root: str, pres_conjugation: str) -> str:
    arch_pres_part_act = ''

    if pres_conjugation == CON1_ACT:
        masc = root + 'ων'
        fem = root + 'ουσα'
        neut = root + 'ον'
        neut_pl = root + 'οντα'
        if check_participle_existence(masc, fem, neut_pl):
            arch_pres_part_act = masc + '/' + fem + '/' + neut

    elif pres_conjugation in [CON2A_ACT]:
        masc = root + 'ών'
        fem = root + 'ούσα'
        neut = root + 'ών'
        neut_pl = root + 'ώντα'
        if check_participle_existence(masc, fem, neut_pl):
            arch_pres_part_act = masc + '/' + fem + '/' + neut

    elif pres_conjugation in [CON2B_ACT, CON2D_ACT]:
        masc = root + 'ών'
        fem = root + 'ούσα'
        neut = root + 'ούν'
        neut_pl = root + 'ούντα'

        fem_wsa = root + 'ώσα'
        neut_wn = root + 'ών'
        neut_pl_wnta = root + 'ώντα'

        if check_participle_existence(masc, fem, neut_pl):
            arch_pres_part_act = masc + '/' + fem + '/' + neut

        elif check_participle_existence(masc, fem_wsa, neut_pl_wnta):
            arch_pres_part_act = masc + '/' + fem_wsa + '/' + neut_wn

        elif check_participle_existence(remove_all_diacritics(masc), fem_wsa, neut_pl_wnta):
            arch_pres_part_act = remove_all_diacritics(masc) + '/' + fem_wsa + '/' + remove_all_diacritics(neut_wn)

    elif pres_conjugation == CON2AK_ACT:
        if root + 'ών' in greek_corpus:
            arch_pres_part_act = root + 'ών/' + root + 'ώσα/' + root + 'ών'

    elif pres_conjugation == CON2C_ACT:
        if root + 'γων' in greek_corpus and root + 'γοντα' in greek_corpus:
            arch_pres_part_act = root + 'γων/' + root + 'γουσα/' + root + 'γον'

    elif pres_conjugation == EIMAI:

        if root + 'ων' in greek_corpus and \
                root + 'όντα' in greek_corpus:
            masc = put_accent_on_the_ultimate(root + 'ων', accent_one_syllable=False)
            fem = put_accent_on_the_penultimate(root + 'ούσα')
            neut = put_accent_on_the_ultimate(root + 'ον', accent_one_syllable=False)

            arch_pres_part_act = masc + '/' + fem + '/' + neut

    return arch_pres_part_act

