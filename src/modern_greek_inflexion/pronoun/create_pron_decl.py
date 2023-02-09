from modern_greek_accentuation.accentuation import put_accent, where_is_accent

from ..adjective import create_all_adj_forms
from ..resources import MASC, FEM, NEUT, SG, PL, ACC, NOM, GEN, VOC, ND


def create_all_pron_forms(bas_forms, strong=True):
    """

    :param bas_forms: basic forms in all genders
    :param strong: if false, creates week pronouns
    :return: dict with all forms
    """
    # forms: dic 'fem', 'masc', neut', if not inflected forms is a string

    masc, fem, neut = bas_forms.split('/')
    forms = None
    if masc == 'που':
        print('pou')
    if masc != neut:

        if masc[-2:] in ['ός', 'ος'] or masc[-3:] == 'πας':

            forms, _ = create_all_adj_forms(bas_forms)

            # acc masc
            acc_masc_sg = forms[SG][MASC][ACC]
            acc_fem_sg = forms[SG][FEM][ACC]
            if acc_masc_sg[-1] in ['ο', 'ό']:
                forms[SG][MASC][ACC] = acc_masc_sg + ',' + acc_masc_sg + 'ν'
            forms[SG][FEM][ACC] = acc_fem_sg + ',' + acc_fem_sg + 'ν'

            if masc == 'αυτός':
                if strong:
                    from ..resources import AUTOS_STRONG
                    forms = AUTOS_STRONG
                else:
                    from ..resources import AUTOS_WEAK
                    forms = AUTOS_WEAK

            if masc == 'ποιος':
                gen_fem_sg = 'ποιας,ποιανάς,τίνος'
                gen_neut_sg = gen_masc_sg = 'ποιου,ποιανού,τίνος'
                gen_pl = 'ποιων,ποιανών,τίνων'
                forms[SG][MASC][GEN] = gen_masc_sg
                forms[SG][FEM][GEN] = gen_fem_sg
                forms[SG][NEUT][GEN] = gen_neut_sg
                forms[PL][MASC][GEN] = gen_pl
                forms[PL][FEM][GEN] = gen_pl
                forms[PL][NEUT][GEN] = gen_pl

        elif masc[-6:] == 'δήποτε':
            suffix = 'δήποτε'
            bas_forms = bas_forms.replace('σδήποτε', 'ς')
            bas_forms = bas_forms.replace('δήποτε', '')

            forms = create_all_pron_forms(bas_forms)
            for number in forms:
                for gender in forms[number]:
                    for case in forms[number][gender]:
                        form = forms[number][gender][case]

                        forms_for_case = []
                        for s_f in form.split(','):
                            if s_f:
                                if s_f[-1] == 'ς':
                                    s_f = s_f[:-1] + 'σ'
                                r = s_f + suffix
                                forms_for_case.append(r)

                        forms[number][gender][case] = ','.join(forms_for_case)
        # ενας, μια, ενα

        elif masc[-4:] == 'ένας' or masc[-3:] == 'είς':
            forms = {'sg': {'masc': {},
                            'fem': {},
                            'neut': {}}
                     }
            if masc[-4:] == 'ένας':
                prefix_mn = masc[:-4]
            else:
                prefix_mn = masc[:-3]

            forms['sg']['masc']['nom'] = prefix_mn + 'ένας' + ',' + prefix_mn + 'είς'
            if masc in ['κανείς', 'κανένας']:
                forms['sg']['masc']['nom'] = 'κανείς,κανένας,' + 'κάνας'
            forms['sg']['masc']['acc'] = prefix_mn + 'ένα' + ',' + prefix_mn + 'έναν'
            forms['sg']['masc']['gen'] = prefix_mn + 'ενός'

            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = ','.join([sf + ',' + sf + 'ν' for sf in fem.split(',')])
            forms['sg']['fem']['gen'] = ','.join([sf + 'ς' for sf in fem.split(',')])

            forms['sg']['neut']['nom'] = prefix_mn + 'ένα'
            forms['sg']['neut']['acc'] = prefix_mn + 'ένα'
            forms['sg']['neut']['gen'] = prefix_mn + 'ενός'

        elif masc == 'τις':
            from ..resources import TIS
            forms = TIS

        elif masc == 'όστις':
            from ..resources import OSTIS
            forms = OSTIS
        elif masc == 'όσπερ':
            from ..resources import OSPER
            forms = OSPER
        elif masc[-2:] in ['οι', 'οί']:
            forms = {'pl': {'masc': {}, 'fem': {}, 'neut': {}}}
            thema = masc[:-2]
            accent = where_is_accent(masc)

            forms[PL][MASC][NOM] = masc
            forms[PL][MASC][GEN] = put_accent(thema + 'ων', accent)
            forms[PL][MASC][ACC] = put_accent(thema + 'ους', accent)
            forms[PL][MASC][VOC] = masc

            forms[PL][FEM][NOM] = fem
            forms[PL][FEM][GEN] = put_accent(thema + 'ων', accent)
            forms[PL][FEM][ACC] = fem
            forms[PL][FEM][VOC] = fem

            forms[PL][NEUT][NOM] = neut
            forms[PL][NEUT][GEN] = put_accent(thema + 'ων', accent)
            forms[PL][NEUT][ACC] = neut
            forms[PL][NEUT][VOC] = neut

    else:
        if masc in ['κάθε', 'κάτι', 'τι', 'δείνα', 'που']:
            forms, _ = create_all_adj_forms(bas_forms)
            for number in forms:
                for gender in forms[number]:
                    for case in forms[number][gender]:

                        if case not in [NOM, ACC]:
                            forms[number][gender][case] = ''
        elif masc in ['καθετί', 'κατιτίς', 'κατιτί', 'τίποτα', 'τίποτε', 'οτιδήποτε', 'τίποτες', 'ίντα', 'ό,τι']:
            forms = {SG: {NEUT: {NOM: masc, ACC: masc}}}
        elif masc in ['οπού', 'όπου', 'πότε', 'όποτε', 'κάποτε', 'ποτέ', 'πάντα', 'πού', 'κάπου', 'πουθενά', 'παντού']:
            # adv
            forms = {ND: {ND: {ND: masc}}}
        elif masc == 'εγώ':
            if strong:
                from ..resources import EGO_STRONG
                forms = EGO_STRONG
            else:
                from ..resources import EGO_WEAK
                forms = EGO_WEAK
        elif masc == 'εσύ':
            if strong:
                from ..resources import ESU_STRONG
                forms = ESU_STRONG
            else:
                from ..resources import ESU_WEAK
                forms = ESU_WEAK

        elif masc == 'αλλήλων':
            forms = {'pl': {
                'masc': {
                    'gen': 'αλλήλων',
                    'acc': 'αλλήλους'
                },
                'fem': {
                    'gen': 'αλλήλων',
                    'acc': 'αλλήλες'
                },
            }}

        elif masc in ['όπερ', 'τουθόπερ']:

            forms = {'sg': {
                'neut': {
                    'nom': masc,
                    'acc': masc
                }}}
            return forms

        elif masc in ['ταύτα', 'τάδε', 'τάδες']:
            forms = {'pl': {
                'neut': {
                    'nom': masc,
                    'acc': masc
                }}}
            return forms

        elif masc == 'εαυτός':
            forms = {'sg': {
                'masc': {
                    'nom': masc,
                    'acc': 'εαυτό,εαυτόν',
                    'gen': 'εαυτού'
                },
                'pl': {
                    'masc': {
                        'nom': 'εαυτοί',
                        'acc': 'εαυτούς',
                        'gen': 'ευτών'
                    }
                }}

            }
            return forms

        else:
            raise ValueError

    # remove vocatives
    for number in forms:
        for gender in forms[number]:
            for case in forms[number][gender]:

                if case == VOC:
                    forms[number][gender][case] = ''

    return forms
