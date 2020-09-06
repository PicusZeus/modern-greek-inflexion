import pickle
from modern_greek_accentuation.accentuation import is_vowel, where_is_accent, put_accent_on_the_ultimate

file = open('modern_greek_stemmer/el_GR.pickle', 'br')
greek_corpus = pickle.load(file)


file.close()



# create two lists, of inflected and not inflected forms, and also of improper forms
# those inflected will be treated as adj, so produce forms for masc, fem, neut



def create_basic_forms(pron):

    temp = {'inflected': False, 'forms': {'fem':'', 'masc':'', 'neut':''}}

    if pron[-2:] in ['ος', 'ός'] and pron != 'τίνος':
        # like poios
        print('os')
        temp['inflected'] = True
        temp['forms']['masc'] = pron

        temp['forms']['neut'] = pron[:-1]

        if is_vowel(pron[-3]):
            temp['forms']['fem'] = pron[:-2] + 'α'


        else:
            temp['forms']['fem'] = pron[:-2] + 'η'
        if where_is_accent(pron) == 'ultimate':
            temp['forms']['fem'] =  put_accent_on_the_ultimate(temp['forms']['fem'])
        return temp

    elif pron[-4:] == 'ένας' or pron[-3:] == 'είς':
        # all the pron like kathenas
        temp['inflected'] = True
        temp['forms']['masc'] = pron
        if pron[-4:] == 'ένας':

            temp['forms']['neut'] = pron[:-1]
            temp['forms']['fem'] = pron[:-4] + 'εμία'
            if pron[-5] == 'ν':
                temp['forms']['fem'] = pron[:-5] + 'μία'

        else:

            temp['forms']['neut'] = pron[:-3] + 'ένα'


            temp['forms']['fem'] = pron[:-3] + 'εμία'
            if pron[-4] == 'ν':
                temp['forms']['fem'] = pron[:-4] + 'μία'

        return temp
    elif 'δήποτε' in pron:
        suffix = 'δήποτε'
        pron = pron[:-6]

        bas_forms = create_basic_forms(pron)
        print(bas_forms)
        if bas_forms['inflected']:
            for key, value in bas_forms['forms']:
                bas_forms['forms'][key] = value + suffix

        else:
            bas_forms['forms'] = bas_forms['forms'] + suffix

        return bas_forms
    elif pron[-1] in ['η', 'ὴ']:
        # there are some random fem nine forms in the list, should be filter out
        return None

    elif pron in ['μηδεμία', 'κατιτίς', 'μερικοί', 'εγώ', 'μου', 'πας', 'πάσα', 'παν', 'κάνας', 'τίνος']:
        # also random forms of personal and other forms pron have to be filter out
        return None

    else:
        # if else it is assumed that the pronouns are not inflected
        temp['forms'] = pron
        return temp