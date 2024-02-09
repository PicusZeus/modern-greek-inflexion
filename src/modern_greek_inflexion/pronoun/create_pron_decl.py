from modern_greek_accentuation.accentuation import put_accent, where_is_accent

from ..adjective import create_all_adj_forms
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from ..resources.pronouns import *
from ..resources.resources import greek_corpus
from ..resources.variables import MASC, FEM, NEUT, SG, PL, ACC, NOM, GEN, VOC, ND


def remove_vocatives(forms):
    for number in forms:
        for gender in forms[number]:
            for case in forms[number][gender]:

                if case == VOC:
                    forms[number][gender][case] = ''
    return forms


def create_all_pron_forms(bas_forms: str, strong: bool = True) -> dict:
    """

    :param bas_forms: basic forms in all genders
    :param strong: if false, creates week pronouns
    :return: dict with all forms
    """
    # forms: dic FEM, MASC, neut', if not inflected forms is a string

    masc, fem, neut = bas_forms.split('/')
    forms = None
    accent = where_is_accent(masc, true_syllabification=False)
    if masc != neut:
        if masc == 'ούτος':
            return OUTOS

        elif masc == 'ος':
            return OS

        elif masc[-2:] in ['ός', 'ος'] or masc.endswith('πας'):

            forms, alternatives = create_all_adj_forms(bas_forms)

            if masc in ['οποίος', 'πόσος', 'οσος', 'απατός', 'μόνος']:
                forms = remove_vocatives(forms)

            if alternatives:
                forms = merging_all_dictionaries(forms, alternatives)
            else:
                forms = merging_all_dictionaries(forms)

            if accent == ANTEPENULTIMATE and masc not in ['όποιος', 'κάμποσος']:
                # in case of pronouns accent can be moved according to general rules.

                gens_sg_masc = forms[SG][MASC][GEN].copy()
                gens_pl = forms[PL][MASC][GEN].copy()
                accs_pl_masc = forms[PL][MASC][ACC].copy()
                fems_sg = forms[SG][FEM][NOM].copy()

                # gen_sg_masc_parox = {put_accent(gen_sg_masc, PENULTIMATE, true_syllabification=False)}
                # gen_sg_masc_parox
                for gen_sg_masc in gens_sg_masc:
                    gen_sg_masc_parox = put_accent(gen_sg_masc, PENULTIMATE, true_syllabification=False)
                    if gen_sg_masc_parox in greek_corpus:
                        forms[SG][MASC][GEN].add(gen_sg_masc_parox)

                for gen_pl in gens_pl:
                    gen_pl_parox = put_accent(gen_pl, PENULTIMATE, true_syllabification=False)
                    if gen_pl_parox in greek_corpus:
                        forms[PL][MASC][GEN].add(gen_pl_parox)
                        forms[PL][FEM][GEN].add(gen_pl_parox)
                        forms[PL][NEUT][GEN].add(gen_pl_parox)

                for acc_pl_masc in accs_pl_masc:
                    acc_pl_masc_parox = put_accent(acc_pl_masc, PENULTIMATE, true_syllabification=False)
                    if acc_pl_masc_parox in greek_corpus:
                        forms[PL][MASC][ACC].add(acc_pl_masc_parox)

                for fem_sg in fems_sg:
                    fem_sg_parox = put_accent(fem_sg, PENULTIMATE, true_syllabification=False)
                    if fem_sg_parox in greek_corpus:
                        forms[SG][FEM][NOM].add(fem_sg_parox)
                        forms[SG][FEM][ACC].add(fem_sg_parox + 'ν')
                        forms[SG][FEM][GEN].add(fem_sg_parox + 'ς')

            if masc == 'εαυτός':
                del forms[SG][FEM]
                del forms[SG][NEUT]
                del forms[PL][FEM]
                del forms[PL][NEUT]

            if masc == 'αυτός':
                if strong:
                    from modern_greek_inflexion.resources.pronouns import AUTOS_STRONG
                    forms = AUTOS_STRONG
                else:
                    from modern_greek_inflexion.resources.pronouns import AUTOS_WEAK
                    forms = AUTOS_WEAK

            if masc == 'ποιος':
                gen_fem_sg = {'ποιας', 'ποιανής', 'τίνος'}
                gen_neut_sg = gen_masc_sg = {'ποιου', 'ποιανού', 'τίνος'}
                gen_pl = {'ποιων', 'ποιανών', 'τίνων'}
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
            new_forms = {}
            for number in forms:
                new_forms[number] = {}
                for gender in forms[number]:
                    new_forms[number][gender] = {}
                    for case in forms[number][gender]:

                        case_forms = forms[number][gender][case].copy()

                        forms_for_case = set()
                        for s_f in case_forms:
                            if s_f:
                                if s_f[-1] == 'ς':
                                    s_f = s_f[:-1] + 'σ'
                                r = s_f + suffix
                                forms_for_case.add(r)

                        new_forms[number][gender][case] = forms_for_case

            forms = new_forms
        # ενας, μια, ενα

        elif masc[-4:] == 'ένας' or masc[-3:] == 'είς':
            forms = {SG: {MASC: {},
                          FEM: {},
                          NEUT: {}}
                     }
            if masc[-4:] == 'ένας':
                prefix_mn = masc[:-4]
            else:
                prefix_mn = masc[:-3]

            forms[SG][MASC][NOM] = {prefix_mn + 'ένας', prefix_mn + 'είς'}
            if masc in ['κανείς', 'κανένας']:
                forms[SG][MASC][NOM].add('κάνας')
            forms[SG][MASC][ACC] = {prefix_mn + 'ένα', prefix_mn + 'έναν'}

            forms[SG][MASC][GEN] = {prefix_mn + 'ενός'}

            forms[SG][FEM][NOM] = set(fem.split(','))
            forms[SG][FEM][ACC] = set(fem.split(','))
            forms[SG][FEM][GEN] = set([sf + 'ς' for sf in fem.split(',')])

            forms[SG][NEUT][NOM] = {prefix_mn + 'ένα'}
            forms[SG][NEUT][ACC] = {prefix_mn + 'ένα'}
            forms[SG][NEUT][GEN] = {prefix_mn + 'ενός'}

        elif masc == 'τις':
            from modern_greek_inflexion.resources.pronouns import TIS
            return TIS

        elif masc == 'όστις':
            return OSTIS
        elif masc == 'όσπερ':

            forms = OSPER
        elif masc[-2:] in ['οι', 'οί']:
            forms = {PL: {MASC: {}, FEM: {}, NEUT: {}}}
            thema = masc[:-2]
            accent = where_is_accent(masc)
            gen_pl = put_accent(thema + 'ων', accent)
            acc_masc_pl = put_accent(thema + 'ους', accent)
            forms[PL][MASC][NOM] = {masc}
            forms[PL][MASC][GEN] = {gen_pl}
            forms[PL][MASC][ACC] = {put_accent(thema + 'ους', accent)}
            forms[PL][MASC][VOC] = {masc}

            forms[PL][FEM][NOM] = {fem}
            forms[PL][FEM][GEN] = {gen_pl}
            forms[PL][FEM][ACC] = {fem}
            forms[PL][FEM][VOC] = {fem}

            forms[PL][NEUT][NOM] = {neut}
            forms[PL][NEUT][GEN] = {gen_pl}
            forms[PL][NEUT][ACC] = {neut}
            forms[PL][NEUT][VOC] = {neut}

            if accent == ANTEPENULTIMATE:
                gen_pl_parox = put_accent(thema + 'ων', PENULTIMATE)
                acc_pl_masc_parox = put_accent(thema + 'ους', PENULTIMATE)

                forms[PL][MASC][GEN].add(gen_pl_parox)
                forms[PL][FEM][GEN].add(gen_pl_parox)
                forms[PL][NEUT][GEN].add(gen_pl_parox)
                forms[PL][MASC][ACC].add(acc_pl_masc_parox)

    else:
        if masc in ['κάθε', 'δείνα', 'που', 'τάδε', 'τάδες']:
            forms, _ = create_all_adj_forms(bas_forms)
            forms = remove_vocatives(forms)
            return merging_all_dictionaries(forms)


        elif masc in ['κάτι', 'τι', 'ίντα', 'ήντα', 'είντα', ]:
            return {SG:
                        {MASC: {NOM: {masc}, ACC: {masc}},
                         FEM: {NOM: {masc}, ACC: {masc}},
                         NEUT: {NOM: {masc}, ACC: {masc}}},
                    PL: {MASC: {NOM: {masc}, ACC: {masc}},
                         FEM: {NOM: {masc}, ACC: {masc}},
                         NEUT: {NOM: {masc}, ACC: {masc}}}}

        elif masc in ['καθετί', 'κατιτίς', 'κατιτί', 'τίποτα', 'τίποτε', 'τουθόπερ', 'οτιδήποτε', 'τίποτες', 'ίντα',
                      'ό,τι']:
            return {SG: {NEUT: {NOM: {masc}, ACC: {masc}}}}
        elif masc in ['οπού', 'όπου', 'πότε', 'όποτε', 'κάποτε', 'ποτέ', 'πάντα', 'πού', 'κάπου', 'πουθενά', 'παντού']:
            # adv
            return {ND: {ND: {ND: {masc}}}}
        elif masc == 'εγώ':
            if strong:
                forms = EGO_STRONG
            else:
                forms = EGO_WEAK
        elif masc == 'εσύ':
            if strong:
                forms = ESU_STRONG
            else:
                forms = ESU_WEAK

        elif masc == 'αλλήλων':
            forms = {PL: {
                MASC: {
                    GEN: 'αλλήλων',
                    ACC: 'αλλήλους'
                },
                FEM: {
                    GEN: 'αλλήλων',
                    ACC: 'αλλήλες'
                },
            }}
            return forms

        elif masc in ['όπερ', 'τουθόπερ', 'ό']:

            forms = {SG: {
                NEUT: {
                    NOM: {masc},
                    ACC: {masc}
                }}}
            return forms
        elif masc in ['κάνα']:
            forms = {PL: {
                MASC: {
                    NOM: {masc},
                    ACC: {masc}
                },
                FEM: {
                    NOM: {masc},
                    ACC: {masc}
                },
                NEUT: {
                    NOM: {masc},
                    ACC: {masc}
                }}}
            return forms
        elif masc in ['ταύτα']:
            forms = {PL: {
                NEUT: {
                    NOM: {masc},
                    ACC: {masc}
                }}}
            return forms
        else:
            raise ValueError

    # remove vocatives

    # acc n
    if masc.endswith('ος') or masc.endswith('ός'):
        accs_masc_sg = forms[SG][MASC][ACC].copy()
        for acc_masc_sg in accs_masc_sg:
            acc_masc_sg_n = acc_masc_sg + 'ν'
            if acc_masc_sg_n in greek_corpus:
                forms[SG][MASC][ACC].add(acc_masc_sg_n)

    if fem[-1] in ['α', 'η', 'ά', 'ή'] and FEM in forms[SG].keys():
        accs_fem_sg = forms[SG][FEM][ACC].copy()
        for acc_fem_sg in accs_fem_sg:
            acc_fem_sg_n = acc_fem_sg + 'ν'
            if acc_fem_sg_n in greek_corpus:
                forms[SG][FEM][ACC].add(acc_fem_sg_n)

    return forms
