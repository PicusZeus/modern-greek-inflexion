# from a list of adj in masc forms creates all three basic forms plus comparative and superlative (if exist) and
# adverb
import pickle

from modern_greek_accentuation.accentuation import is_accented, where_is_accent, put_accent, count_syllables,\
    put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, remove_all_diacritics, put_accent_on_the_ultimate
from modern_greek_accentuation.syllabify import modern_greek_syllabify
from modern_greek_accentuation.resources import vowels


with open('el_GR.pickle', 'br') as file:
    greek_corpus = pickle.load(file)

irregular_comparatives = {'καλό': 'καλύτερος/άριστος',
                          'κακό': 'χειρότερος,ήσσων/χείριστος,ήκιστος',
                          'απλό': 'απλούστερος/απλούστατος',
                          'μεγάλο': 'μεγαλύτερος/μέγιστος',
                          'πολύ': 'περισσότερος/-',
                          'λίγο': 'λιγότερος/ελάχιστος',
                          'μέγα': 'μεγαλύτερος/μέγιστος',
                          'πρώτο': 'πρωτύτερος/πρώτιστος'}

irregular_comparative_adverbs = {'κακό': 'χειρότερα,ήσσον,ήττον/κάκιστα,ήκιστα',
                                 'καλό': 'καλύτερα,κάλλιον,κάλλιο/άριστα',
                                 'λίγο': 'λιγότερο/ελάχιστα', 'πολύ': 'περισσότερο/-'}

def create_all_basic_adj_forms(adj):
    """
    :param adj: masc nom sg form (`ωραίος`)
    :return: dictionary with keys:
    'adj': masc, fem, neut forms as a string divided with / ('ωραίος/ωραία/ωραίο') if alternatives, they are added and
    separated with a coma
    'comparative': if exists in form parathetiko + ',' + alt_parathetiko + '/' + uperthetiko + ',' + alt_uperthetiko with
    form only in masc sing nom
    'adverb': adverb form, if alternatives, then separated with coma
    'adverb_comparative': if exists, adverb_parathetiko + ',' + alt_adverb_parathetiko + '/' + adverb_uperthetiko + ',' + alt_adverb_uperthetiko
    """
    # correct possible errors in the list
    if adj[-2:] == 'ον' and adj + 'τα' in greek_corpus:
        adj = adj[:-2] + 'ων'

    elif adj[-2:] == 'ές' and adj[:-2] + 'ής' in greek_corpus:
        #    in ['εκκρεμές', 'λυκαυγές', 'αλκαλοειδές']:
        adj = adj[:-2] + 'ής'
    elif adj[-2:] == 'έν' and adj[:-2] + 'είς' in greek_corpus:
        #['ανακοινωθέν']:
        adj = adj[:-2] + 'είς'
    elif adj[-2:] == 'ού':
        if adj[:-2] + 'άς' in greek_corpus:
            adj = adj[:-2] + 'άς'
        elif put_accent_on_the_penultimate(adj[:-2] + 'ης') in greek_corpus:
            adj = put_accent_on_the_penultimate(adj[:-2] + 'ης')
    elif adj[-1] == 'ί' and adj[:-1] + 'ής' in greek_corpus:
        adj = adj[:-1] + 'ής'
    accent = where_is_accent(adj, true_syllabification=False)

    adj_temp = {'adj': 'masc,fem,neuter', 'comparative': '', 'adverb': '', 'adverb_comparative': ''}

    adj_forms = []
    # most basic case -os

    if adj[-2:] in ['ός', 'ος']:
        masc = adj
        adj_forms.append(masc)

        if accent == 'ultimate':
            fem = adj[:-2] + 'ή'
        else:
            fem = adj[:-2] + 'η'
        fem_alt = None

        if adj[-3] in vowels and count_syllables(adj) <= 2:
            if accent == 'ultimate':
                fem = adj[:-2] + 'ά'
            else:
                fem = adj[:-2] + 'α'

        elif adj[-3] in vowels and count_syllables(adj) > 2 and not is_accented(modern_greek_syllabify(adj)[-3]):
            if accent == 'ultimate':
                fem = adj[:-2] + 'ά'
            else:
                fem = adj[:-2] + 'α'

        if adj[-3] in ['κ', 'θ', 'χ']:

            if accent == 'ultimate':
                fem_alt = adj[:-2] + 'ιά'
            else:
                fem_alt = adj[:-2] + 'ια'

        if fem in greek_corpus and fem_alt in greek_corpus:
            fem = fem + ',' + fem_alt

        elif fem not in greek_corpus and fem_alt in greek_corpus:
            fem = fem_alt

        elif fem in greek_corpus and fem_alt not in greek_corpus:
            fem = fem
        else:
            # for the most part forms on h should be correct, but adj is not very common, so is lacking from db
            # check for -a by looking for genetive on as in db
            if accent == 'ultimate':
                gen = adj[:-2] + 'άς'
                beta_fem = adj[:-2] + 'ά'
            else:
                gen = adj[:-2] + 'ας'
                beta_fem = adj[:-2] + 'α'

            if gen in greek_corpus:
                fem = beta_fem

            elif adj[-5:] in ['μένος', 'μενος']:
                fem = adj[:-2] + 'η'

            # if its lacking from the db, still the best shot is to leave the supposed femine form

        adj_forms.append(fem)

        neuter = adj[:-1]

        adj_forms.append(neuter)

    elif adj[-2:] in ['ής', 'ης']:

        # first check which type
        stem = adj[:-2]
        if stem + 'ικο' in greek_corpus:
            # type hs, a, iko, here accent is always on the last syllable of the stem
            masc = adj
            fem = stem + 'α'
            neuter = stem + 'ικο'

        elif put_accent(stem + 'ι', accent) in greek_corpus:
            # type, hs, ia, i, mostly colors

            masc = adj
            fem = put_accent(stem + 'ια', accent)
            neuter = put_accent(stem + 'ι', accent)

        elif put_accent(stem + 'ους', accent, true_syllabification=False) in greek_corpus:
            # type hs, hs, es
            masc, fem = adj, adj
            neuter = put_accent(stem + 'ες', accent, true_syllabification=False)
            if accent != 'ultimate' and neuter not in greek_corpus:
                neuter = put_accent(stem + 'ες', 'antepenultimate', true_syllabification=False)

        elif stem + 'ού' in greek_corpus:
            # type kafetzhs kafetzou, only masc and fem
            masc = adj
            fem = adj[:-2] + 'ού'
            neuter = adj[:-1] + 'δικο'

        else:
            raise AssertionError

    elif adj[-2:] in ['υς', 'ύς'] or adj in ['γλυκύ']:
        stem = adj[:-2]
        masc = adj
        neuter = adj[:-1]
        if adj in ['γλυκύ']:
            # unforturetly there are some mistakes in my word list whereneuter forms are given as lemma
            # and so I have to correct them in this way
            stem = adj[:-1]
            masc = adj + 'ς'
            neuter = adj

        adj_forms.append(masc)

        fem = stem + 'εία'

        if fem not in greek_corpus:
            fem = stem + 'ιά'
            if fem not in greek_corpus and adj[-5:] == 'πολύς':
                fem = adj[:-5] + 'πολλή'

    elif adj[-2:] in ['ων', 'ών']:
        stem = adj[:-2]
        masc = adj
        fem = None
        neuter = None
        if accent == 'penultimate' or not accent:
            fem = stem + 'ουσα'
            if not accent:
                fem = put_accent_on_the_penultimate(fem)

            neuter = stem + 'ον'

        if accent == 'ultimate' or not accent:
            fem = '-'
            neuter = stem + 'όν'
            neuter_alt_1 = stem + 'ών'
            neuter_alt_2 = stem + 'ούν'
            if neuter + 'τα' in greek_corpus or neuter + 'τες' in greek_corpus:
                fem = stem + 'ούσα'
            elif neuter_alt_1 + 'τα' in greek_corpus or neuter_alt_1 + 'τες' in greek_corpus:
                fem = stem + 'ώσα'
                neuter = neuter_alt_1
            elif neuter_alt_2 + 'τα' in greek_corpus or neuter_alt_2 + 'τες' in greek_corpus or neuter_alt_2 + 'των' in greek_corpus:
                fem = stem + 'ούσα'
                neuter = neuter_alt_2
            if not accent:
                neuter = remove_all_diacritics(neuter)

            if not neuter:
                neuter = '-'
            if adj in ['ζων', 'κυβερνών', 'επιζών']:
                # if adj are the old present participles contracted on a and
                neuter = adj
                fem = stem + 'ώσα'

        # it is also possible, that there are wn, onos
        if adj[:-2] + 'ονος' in greek_corpus:
            masc, fem = adj, adj
            neuter = adj[:-2] + 'ον'

        if not fem:
            print(adj)
            raise AssertionError

    elif adj[-3:] == 'είς':
        # passive aorist participles
        if not adj[:-3] + 'έντα' in greek_corpus:
            raise AssertionError
        masc = adj
        fem = adj[:-1] + 'σα'
        neuter = adj[:-3] + 'έν'

    elif adj[-2:] in ['ας', 'άς']:

        # pas, pasa pan and active aorist participles
        # pas pasa pan

        pl_nta = adj[:-1] + 'ντα'
        fem_sa =adj[:-1] + 'σα'

        if count_syllables(adj) == 1:
            pl_nta = put_accent(pl_nta, 'penultimate')
            fem_sa = put_accent(fem_sa, 'penultimate')
        if pl_nta in greek_corpus:
            masc = adj
            fem = fem_sa
            neuter = adj[:-1] + 'ν'

        elif adj == 'μέγας':
            masc = adj
            fem = 'μαγάλη'
            neuter = 'μέγα'

        elif adj[-4:] == 'ονας':
            masc = adj
            fem = adj[:-4] + 'ων'
            neuter = adj[:-2]
        else:
            raise AssertionError

    elif adj in ['άρρην']:
        # so rare that it can be solved like that
        masc = adj
        fem = adj
        neuter = masc[:-2] + 'εν'

    else:
        masc, fem, neuter = adj, adj, adj

    adj_forms = [masc, fem, neuter]

    adj_temp['adj'] = '/'.join(adj_forms)
# παραθετικά

    stem = neuter
    if stem[-1] == 'ς':
        stem = stem[:-1] + 'σ'
    parathetika = None
    alt_parathetiko = None
    uperthetiko = '-'
    alt_uperthetiko = None

    parathetiko = put_accent_on_the_antepenultimate(stem + 'τερος')

    if parathetiko not in greek_corpus:
        parathetiko = None
    else:
        uperthetiko = put_accent_on_the_antepenultimate(parathetiko[:-5] + 'τατος')

        if uperthetiko not in greek_corpus:
            uperthetiko = '-'

    if neuter[-1] in ['ο', 'ό']:
        alt_parathetiko = remove_all_diacritics(neuter[:-1]) + 'ύτερος'
        if alt_parathetiko not in greek_corpus:
            alt_parathetiko = None
        else:
            alt_uperthetiko =put_accent_on_the_antepenultimate(alt_parathetiko[:-5] + 'τατος')
            if alt_uperthetiko not in greek_corpus:
                alt_uperthetiko = '-'

    if parathetiko and alt_parathetiko:
        parathetika = parathetiko + ',' + alt_parathetiko + '/' + uperthetiko + ',' + alt_uperthetiko

    elif parathetiko:
        parathetika = parathetiko + '/' + uperthetiko

    elif alt_parathetiko and alt_uperthetiko:
        parathetika = alt_parathetiko + '/' + alt_uperthetiko

    if neuter in irregular_comparatives.keys():
        parathetiko = irregular_comparatives[neuter].split('/')[0]
        uperthetiko = irregular_comparatives[neuter].split('/')[1]
        alt_parathetiko, alt_uperthetiko = None, None
        parathetika = irregular_comparatives[neuter]

    if parathetika:
        adj_temp['comparative'] = parathetika

    # επιρρήματα

    alt_adv = None

    if neuter[-1] in ['ο', 'ό']:
        accent = where_is_accent(neuter)
        if accent != 'ultimate':
            adverb = neuter[:-1] + 'α'
            alt_adv = put_accent_on_the_penultimate(neuter[:-1] + 'ως', true_syllabification=False)
        else:
            adverb = neuter[:-1] + 'ά'
            alt_adv = neuter[:-1] + 'ώς'

    elif masc[-2:] in ['ής', 'ης'] and neuter[-2:] in ['ές', 'ες']:

        adverb = remove_all_diacritics(neuter[:-2]) + 'ώς'
        if adverb not in greek_corpus and neuter[:-2] + 'ως' in greek_corpus:
            adverb = neuter[:-2] + 'ως'
        alt_adv = neuter[:-2] + 'ά'

    elif neuter[-1] in ['υ', 'ύ'] and masc[-1] == 'ς':
        # it should have the ancient form on ews
        adverb = put_accent_on_the_penultimate(neuter[:-1] + 'εως')
        if adverb not in greek_corpus:
            adverb = adj_forms[1]
    elif neuter[-1] == 'ί':
        # colors
        adverb = put_accent_on_the_ultimate(adj_forms[2] + 'α')

    elif (masc[-2:] in ['ας', 'άς', 'ων', 'ών'] or masc[-3:] in ['εις', 'είς']) and fem[-2:] == 'σα' and neuter[
        -1] == 'ν':
        # ancient adverbs
        adverb = put_accent_on_the_penultimate(neuter + 'τως')
    else:
        # for aklita
        adverb = neuter

    if neuter in ['λίγο', 'πολύ', 'ήσσον', 'κάλλιον']:
        adverb = neuter

    # special cases
    if neuter in ['μέγα', 'μεγάλο']:
        # special case
        adverb = 'μέγα'
        alt_adv = 'μεγάλως'

    elif (masc[-4:] == 'ονας' or masc[-2:] == 'ων') and fem[-2:] == 'ων':
        adverb = None

    elif masc in ['άρρην']:
        adverb = None

    epirrimata = [e for e in [adverb, alt_adv] if e and e in greek_corpus]

    epirrimata = ','.join(epirrimata)
    if epirrimata:
        adj_temp['adverb'] = epirrimata

# comparative epirrimata
    adv_parathetika = None

    adverb_parathetiko = alt_adverb_parathetiko =adverb_uperthetiko = alt_adverb_uperthetiko = ''

    if parathetiko:
        adverb_parathetiko = parathetiko[:-2] + 'α'
        if uperthetiko != '-':
            adverb_uperthetiko = uperthetiko[:-2] + 'α'
        else:
            adverb_uperthetiko = '-'

    if alt_parathetiko:
        alt_adverb_parathetiko = alt_parathetiko[:-2] + 'α'
        if alt_uperthetiko:

            alt_adverb_uperthetiko = alt_uperthetiko[:-2] + 'α'
        else:
            alt_adverb_uperthetiko = '-'

    if parathetiko and alt_parathetiko:
        adv_parathetika = adverb_parathetiko + ',' + alt_adverb_parathetiko + '/' + adverb_uperthetiko + ',' + alt_adverb_uperthetiko

    elif parathetiko:
        adv_parathetika = adverb_parathetiko + '/' + adverb_uperthetiko
    elif alt_parathetiko:
        adv_parathetika = alt_adverb_parathetiko + '/' + alt_adverb_uperthetiko

    if neuter in irregular_comparative_adverbs.keys():
        adv_parathetika = irregular_comparative_adverbs[neuter]

    if adv_parathetika:
        adj_temp['adverb_comparative'] = adv_parathetika
    assert adj_temp['adj'].split('/')[1] != '-'

    if adj in ['είμαι', 'τάχατες', 'βεληνεκές', 'γιαχνί', 'πλακί', 'μύριοι']:
        # in my adjective list there are some strange errors which have to be filtered out
        return None
    return adj_temp