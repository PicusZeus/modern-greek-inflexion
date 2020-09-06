import pickle
import copy
from modern_greek_accentuation.accentuation import where_is_accent, put_accent_on_the_ultimate

with open('modern_greek_stemmer/el_GR.pickle', 'rb') as file:
    greek_corpus = pickle.load(file)

pron_basic = {'sg':{
                    'masc':{
                        'nom': '',
                        'gen': '',
                        'acc': '',
                        'voc': ''
                    },
                    'fem':{
                        'nom': '',
                        'gen': '',
                        'acc': '',
                        'voc': ''},
                    'neut':{
                        'nom': '',
                        'gen': '',
                        'acc': '',
                        'voc': ''}
                    },
              'pl': {
                  'masc': {
                        'nom': '',
                        'gen': '',
                        'acc': '',
                        'voc': ''},
                  'fem': {
                      'nom': '',
                      'gen': '',
                      'acc': '',
                      'voc': ''
                  },
                  'neut': {
                      'nom': '',
                      'gen': '',
                      'acc': '',
                      'voc': ''
                  }
              }}





def all_pron_forms(inflected, bas_forms):
    # inflected: boolean
    # forms: dic 'fem', 'masc', neut', if not inflected forms is a string



    if inflected:
        fem = bas_forms['fem']
        masc = bas_forms['masc']
        neuter = bas_forms['neut']


        if masc[-2:] in ['ός', 'ος'] and fem[-1] in ['α', 'ά', 'η', 'ή'] and neuter[-1] in ['ο', 'ό']:
            forms = copy.deepcopy(pron_basic)
            # os, h/a, o
            forms['sg']['masc']['nom'] = masc
            forms['sg']['masc']['acc'] = masc[:-1] + '/' + masc[:-1] + 'ν'
            forms['sg']['masc']['gen'] = masc[:-2] + 'ου'
            forms['sg']['masc']['voc'] = masc[:-2] + 'ε'
            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = fem + '/' + fem + 'ν'
            forms['sg']['fem']['gen'] = fem + 'ς'
            forms['sg']['fem']['voc'] = fem
            forms['sg']['neut']['nom'] = neuter
            forms['sg']['neut']['gen'] = neuter[:-1] + 'ου'
            forms['sg']['neut']['acc'] = neuter
            forms['sg']['neut']['voc'] = neuter

            forms['pl']['masc']['nom'] = masc[:-2] + 'οι'
            forms['pl']['masc']['acc'] = masc[:-2] + 'ους'
            forms['pl']['masc']['gen'] = masc[:-2] + 'ων'
            forms['pl']['masc']['voc'] = masc[:-2] + 'οι'
            forms['pl']['fem']['nom'] = fem[:-1] + 'ες'
            forms['pl']['fem']['acc'] = fem[:-1] + 'ες'
            forms['pl']['fem']['gen'] = fem[:-1] + 'ων'
            forms['pl']['fem']['voc'] = fem[:-1] + 'ες'
            forms['pl']['neut']['nom'] = neuter[:-1] + 'α'
            forms['pl']['neut']['acc'] = neuter[:-1] + 'α'
            forms['pl']['neut']['gen'] = neuter[:-1] + 'ων'
            forms['pl']['neut']['voc'] = neuter[:-1] + 'α'

            accent = where_is_accent(masc)
            if accent == 'ultimate':
                for num in forms.keys():
                    for gender in forms[num].keys():
                        for case, form in forms[num][gender].items():
                            forms[num][gender][case] = put_accent_on_the_ultimate(form)

            if fem[-2] == 'κ':
                forms['sg']['fem']['nom'] += '/' + fem[:-1] + 'ια'
                forms['sg']['fem']['acc'] += '/' + fem[:-1] + 'ια'
                forms['sg']['fem']['gen'] += '/' + fem[:-1] + 'ιας'
                forms['sg']['fem']['voc'] += '/' + fem[:-1] + 'ια'

            if masc == 'ποιος':
                forms['sg']['masc']['gen'] = 'ποιου/ποιανού/τίνος'

                forms['sg']['fem']['gen'] = 'ποιας/ποιανής/τίνος'

                forms['sg']['neut']['gen'] = 'ποιου/ποιανού/τίνος'

                forms['pl']['masc']['gen'] = 'ποιων/ποιανών/τίνων'
                forms['pl']['masc']['acc'] = 'ποιους/ποιανούν/τίνας'

                forms['pl']['fem']['gen'] = 'ποιων/ποιανών/τίνων'

                forms['pl']['neut']['gen'] = 'ποιων/ποιανών/τίνων'

            return forms


        else:
            forms = copy.deepcopy(pron_basic)
            # ενας, μια, ενα
            prefix_mn = neuter[:-3]

            prefix_f = fem[:-3]
            if masc[-4:] == 'ένας':

                forms['sg']['masc']['nom'] = prefix_mn + 'ένας' + '/' + prefix_mn + 'είς'
                forms['sg']['masc']['acc'] = prefix_mn + 'ένα' + '/' + prefix_mn + 'έναν'
                forms['sg']['masc']['gen'] = prefix_mn + 'ενός'

                forms['sg']['fem']['nom'] = prefix_f + 'μιά' + '/' + prefix_f + 'μία'
                forms['sg']['fem']['acc'] = prefix_f + 'μιά' + '/' + prefix_f + 'μία' + '/' + prefix_f + 'μιάν' + '/' + prefix_f + 'μίαν'
                forms['sg']['fem']['gen'] = prefix_f + 'μιάς' + '/' + prefix_f + 'μίας'

                forms['sg']['neut']['nom'] = prefix_mn + 'ένα'
                forms['sg']['neut']['acc'] = prefix_mn + 'ένα'
                forms['sg']['neut']['gen'] = prefix_mn + 'ενός'

            elif masc[-3:] == 'είς':
                prefix_mn = masc[:-3]

                forms['sg']['masc']['nom'] = prefix_mn + 'είς'
                forms['sg']['masc']['acc'] = prefix_mn + 'ένα'
                forms['sg']['masc']['gen'] = prefix_mn + 'ενός'

                forms['sg']['fem']['nom'] =  prefix_f + 'μία'
                forms['sg']['fem']['acc'] =  prefix_f + 'μίαν'
                forms['sg']['fem']['gen'] = prefix_f + 'μίας'

                forms['sg']['neut']['nom'] = prefix_mn + 'έν'
                forms['sg']['neut']['acc'] = prefix_mn + 'έν'
                forms['sg']['neut']['gen'] = prefix_mn + 'ενός'







    else:

        #if not inflected, there are some pronouns not exactly well described in the db,
        # so will have to do it manually

        if bas_forms in ['καθετί', 'τι', 'κατιτί', 'τίποτα', 'οτιδήποτε']:
            # only in onomastiki and aitiatiki
            forms = copy.deepcopy(pron_basic)

            for num in forms:
                for gender in forms[num]:
                    for case in forms[num][gender]:
                        if case not in ['gen', 'voc']:
                            forms[num][gender][case] = bas_forms
            return forms
        elif bas_forms == 'όσο':
            return None
            # its actually an adverb

        elif bas_forms == 'αλλήλων':
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
            return forms


        elif bas_forms == 'όπερ':

            forms =  {'sg':{
                    'neut':{
                        'nom': bas_forms,
                        'acc': bas_forms
                    }}}
            return forms

        elif bas_forms == 'ταύτα':
            forms = {'pl':{
                        'neut':{
                            'nom': bas_forms,
                            'acc': bas_forms
                    }}}
            return forms

        elif len(bas_forms) > 7 and bas_forms[-7:] == 'σδήποτε':
            dhpote = 'δήποτε'

            pron = bas_forms[:-6]
            forms = copy.deepcopy(pron_basic)
            masc = pron
            fem = pron[:-2] + 'η'

            if pron[-3] == 'ι':
                fem = pron[:-2] + 'α'
            neuter = pron[:-1]

            forms['sg']['masc']['nom'] = masc + dhpote
            forms['sg']['masc']['acc'] = masc[:-1] + 'ν' + dhpote
            forms['sg']['masc']['gen'] = masc[:-2] + 'ου' + dhpote

            forms['sg']['fem']['nom'] = fem + dhpote
            forms['sg']['fem']['acc'] = fem + 'ν' + dhpote + '/' + fem + dhpote
            forms['sg']['fem']['gen'] = fem + 'σ' + dhpote

            forms['sg']['neut']['nom'] = neuter + dhpote
            forms['sg']['neut']['gen'] = neuter[:-1] + 'ου' + dhpote
            forms['sg']['neut']['acc'] = neuter + dhpote

            forms['pl']['masc']['nom'] = masc[:-2] + 'οι' + dhpote
            forms['pl']['masc']['acc'] = masc[:-2] + 'ουσ' + dhpote
            forms['pl']['masc']['gen'] = masc[:-2] + 'ων' + dhpote

            forms['pl']['fem']['nom'] = fem[:-1] + 'εσ' + dhpote
            forms['pl']['fem']['acc'] = fem[:-1] + 'εσ' + dhpote
            forms['pl']['fem']['gen'] = fem[:-1] + 'ων' + dhpote

            forms['pl']['neut']['nom'] = neuter[:-1] + 'α' + dhpote
            forms['pl']['neut']['acc'] = neuter[:-1] + 'α' + dhpote
            forms['pl']['neut']['gen'] = neuter[:-1] + 'ων' + dhpote

            return forms

        else:
            forms = copy.deepcopy(pron_basic)
            for num in forms:
                for gender in forms[num]:
                    for case in forms[num][gender]:
                        forms[num][gender][case] = bas_forms
            return forms


