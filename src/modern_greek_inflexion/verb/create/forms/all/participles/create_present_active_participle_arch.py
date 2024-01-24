from modern_greek_accentuation.accentuation import put_accent_on_the_ultimate, put_accent_on_the_penultimate

from modern_greek_inflexion.resources import CON1_ACT, greek_corpus, CON2A_ACT, CON2B_ACT, CON2D_ACT, CON2A_ACT_LOGIA, \
    CON2C_ACT, EIMAI


def create_present_active_participle_arch(_: str, root: str, pres_conjugation: str) -> str:
    arch_pres_part_act = ''

    if pres_conjugation == CON1_ACT:
        if root + 'ων' in greek_corpus and root + 'ουσα' in greek_corpus:
            arch_pres_part_act = root + 'ων/' + root + 'ουσα/' + root + 'ον'

    elif pres_conjugation in [CON2A_ACT]:
        if root + 'ών' in greek_corpus and root + 'ώσα' in greek_corpus:
            arch_pres_part_act = root + 'ών/' + root + 'ώσα/' + root + 'ών'

    elif pres_conjugation in [CON2B_ACT, CON2D_ACT]:
        if root + 'ών' in greek_corpus and root + 'ούντα' in greek_corpus:
            arch_pres_part_act = root + 'ών/' + root + 'ούσα/' + root + 'ούν'
        elif root + 'ών' in greek_corpus and root + 'ώντα' in greek_corpus:
            arch_pres_part_act = root + 'ών/' + root + 'ώσα/' + root + 'ών'
        elif root + 'ων' in greek_corpus and root + 'ώντα' in greek_corpus:
            arch_pres_part_act = root + 'ων/' + root + 'ώσα/' + root + 'ων'
    elif pres_conjugation == CON2A_ACT_LOGIA:
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

