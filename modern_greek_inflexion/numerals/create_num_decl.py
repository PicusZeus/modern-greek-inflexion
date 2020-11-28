
import copy

from modern_greek_accentuation.accentuation import put_accent_on_the_penultimate, where_is_accent, put_accent_on_the_ultimate

from modern_greek_inflexion.adjective.create_adj_decl import create_all_adj_forms
from modern_greek_inflexion.adjective.create_adj_decl import adj_basic_template

from ..resources import greek_corpus, aklita_num_alternatives


def creat_all_num_adj_forms(num_base_forms, ordinal=False):
    """
    :param num_base_forms:
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
            if accent == 'ultimate':
                acc_masc = put_accent_on_the_ultimate(acc_masc)
                gen_pl = put_accent_on_the_ultimate(gen_pl)
            elif accent == 'antepenultimate':
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
        elif neut in aklita_num_alternatives:
            masc = fem = neut = acc_masc = gen_pl = neut + ',' + aklita_num_alternatives[neut]

        elif neut == 'ένα':

            forms['sg']['masc']['nom'] = masc
            forms['sg']['masc']['acc'] = 'ένα,έναν'
            forms['sg']['masc']['voc'] = 'ένα'
            forms['sg']['masc']['gen'] = 'ενός'

            forms['sg']['fem']['nom'] = 'μια,μία'
            forms['sg']['fem']['acc'] = 'μια,μιαν,μία,μίαν'
            forms['sg']['fem']['gen'] = 'μίας,μιας'
            forms['sg']['fem']['voc'] = 'μία,μια'

            forms['sg']['neut']['gen'] = 'ενός'
            forms['sg']['neut']['nom'] = neut
            forms['sg']['neut']['acc'] = neut
            forms['sg']['neut']['voc'] = neut

            return forms

        elif masc == 'ενάμισης':

            forms['sg']['masc']['nom'] = masc
            forms['sg']['masc']['acc'] = masc[:-1]
            forms['sg']['masc']['voc'] = masc[:-1]
            forms['sg']['masc']['gen'] = masc[:-1]

            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = fem
            forms['sg']['fem']['gen'] = fem + 'ς'
            forms['sg']['fem']['voc'] = fem

            forms['sg']['neut']['gen'] = neut
            forms['sg']['neut']['nom'] = neut
            forms['sg']['neut']['acc'] = neut
            forms['sg']['neut']['voc'] = neut

            return forms

        elif neut == 'μηδέν':
            masc = 'μηδείς'
            fem = 'μηδεμία'

            forms['sg']['masc']['nom'] = masc
            forms['sg']['masc']['acc'] = 'μηδένα'
            forms['sg']['masc']['gen'] = 'μηδενός'

            forms['sg']['neut']['nom'] = neut
            forms['sg']['neut']['gen'] = 'μηδενός'
            forms['sg']['neut']['acc'] = neut

            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = fem + ',μηδεμίαν'
            forms['sg']['fem']['gen'] = 'μηδεμίας'
            forms['sg']['fem']['voc'] = fem

            return forms

        else:
            masc = fem = neut = acc_masc = gen_pl = neut

        forms['pl']['masc']['nom'] = masc
        forms['pl']['masc']['acc'] = acc_masc
        forms['pl']['masc']['gen'] = gen_pl
        forms['pl']['masc']['voc'] = masc

        forms['pl']['fem']['nom'] = fem
        forms['pl']['fem']['acc'] = fem
        forms['pl']['fem']['gen'] = gen_pl
        forms['pl']['fem']['voc'] = fem

        forms['pl']['neut']['nom'] = neut
        forms['pl']['neut']['acc'] = neut
        forms['pl']['neut']['gen'] = gen_pl
        forms['pl']['neut']['voc'] = neut

        if masc[:4] == 'οχτα':
            alt = 'οκτα'
            for number in forms:
                for gender in forms[number]:
                    for case in forms[number][gender]:
                        forms[number][gender][case] += ',' + forms[number][gender][case].replace(masc[:4], alt)
        elif masc[:4] == 'εφτα':
            alt = 'επτα'
            for number in forms:
                for gender in forms[number]:
                    for case in forms[number][gender]:
                        forms[number][gender][case] += ',' + forms[number][gender][case].replace(masc[:4], alt)
        elif masc[:5] == 'εννια':
            alt = 'εννεα'
            for number in forms:
                for gender in forms[number]:
                    for case in forms[number][gender]:
                        forms[number][gender][case] += ',' + forms[number][gender][case].replace(masc[:5], alt)

        return forms

