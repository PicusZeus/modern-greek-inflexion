import copy

from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, where_is_accent, \
    put_accent_on_the_ultimate
from modern_greek_accentuation.resources import ANTEPENULTIMATE, PENULTIMATE, ULTIMATE
from ..adjective import create_all_adj_forms
from ..resources import adj_basic_template
from ..resources import greek_corpus, SG, PL, NOM, GEN, ACC, VOC, FEM, MASC, NEUT


def create_all_num_adj_forms(num_base_forms, ordinal=False):
    """
    :param num_base_forms masc/fem/neut:
    :return: a dictionary of forms (like adj)
    """
    if ordinal:
        all_forms = create_all_adj_forms(num_base_forms)

        return all_forms[0]
    else:
        masc, fem, neut = num_base_forms.split('/')
        forms = copy.deepcopy(adj_basic_template)

        if masc[-2:] in ['οι', 'οί'] and fem[-2:] in ['ες', 'ές'] and neut[-1] in ['α', 'ά']:
            # exclusively for numerals, as there are for obvious reasons only in plural
            accent = where_is_accent(masc, true_syllabification=False)
            acc_masc = masc[:-2] + 'ους'
            gen_pl = masc[:-2] + 'ων'
            if accent == ULTIMATE:
                acc_masc = put_accent_on_the_ultimate(acc_masc)
                gen_pl = put_accent_on_the_ultimate(gen_pl)
            elif accent == ANTEPENULTIMATE:
                accs_masc = [acc_masc, put_accent_on_the_penultimate(acc_masc, true_syllabification=False)]
                gens_pl = [gen_pl, put_accent_on_the_penultimate(gen_pl, true_syllabification=False)]
                gen_pl = ','.join([g for g in gens_pl if g in greek_corpus])
                acc_masc = ','.join([a for a in accs_masc if a in greek_corpus])

        elif neut[-4:] == 'τρία':
            gen_pl = neut[:-4] + 'τριών'
            acc_masc = masc

        elif neut[-7:] == 'τέσσερα':
            gen_pl = 'τεσσάρων'
            acc_masc = masc

        elif neut == 'ένα':

            forms[SG][MASC][NOM] = masc
            forms[SG][MASC][ACC] = 'ένα,έναν'
            forms[SG][MASC][VOC] = 'ένα'
            forms[SG][MASC][GEN] = 'ενός'

            forms[SG][FEM][NOM] = 'μια,μία'
            forms[SG][FEM][ACC] = 'μια,μιαν,μία,μίαν'
            forms[SG][FEM][GEN] = 'μίας,μιας'
            forms[SG][FEM][VOC] = 'μία,μια'

            forms[SG][NEUT][GEN] = 'ενός'
            forms[SG][NEUT][NOM] = neut
            forms[SG][NEUT][ACC] = neut
            forms[SG][NEUT][VOC] = neut

            return forms

        elif masc == 'ενάμισης':

            forms[SG][MASC][NOM] = masc
            forms[SG][MASC][ACC] = masc[:-1]
            forms[SG][MASC][VOC] = masc[:-1]
            forms[SG][MASC][GEN] = masc[:-1]

            forms[SG][FEM][NOM] = fem
            forms[SG][FEM][ACC] = fem
            forms[SG][FEM][GEN] = fem + 'ς'
            forms[SG][FEM][VOC] = fem

            forms[SG][NEUT][GEN] = neut
            forms[SG][NEUT][NOM] = neut
            forms[SG][NEUT][ACC] = neut
            forms[SG][NEUT][VOC] = neut

            return forms

        elif neut == 'μηδέν':
            masc = 'μηδείς'
            fem = 'μηδεμία'

            forms[SG][MASC][NOM] = masc
            forms[SG][MASC][ACC] = 'μηδένα'
            forms[SG][MASC][GEN] = 'μηδενός'

            forms[SG][NEUT][NOM] = neut
            forms[SG][NEUT][GEN] = 'μηδενός'
            forms[SG][NEUT][ACC] = neut

            forms[SG][FEM][NOM] = fem
            forms[SG][FEM][ACC] = fem + ',μηδεμίαν'
            forms[SG][FEM][GEN] = 'μηδεμίας'
            forms[SG][FEM][VOC] = fem

            return forms

        else:
            masc = fem = neut = acc_masc = gen_pl = neut

        forms[PL][MASC][NOM] = masc
        forms[PL][MASC][ACC] = acc_masc
        forms[PL][MASC][GEN] = gen_pl
        forms[PL][MASC][VOC] = masc

        forms[PL][FEM][NOM] = fem
        forms[PL][FEM][ACC] = fem
        forms[PL][FEM][GEN] = gen_pl
        forms[PL][FEM][VOC] = fem

        forms[PL][NEUT][NOM] = neut
        forms[PL][NEUT][ACC] = neut
        forms[PL][NEUT][GEN] = gen_pl
        forms[PL][NEUT][VOC] = neut

        return forms
