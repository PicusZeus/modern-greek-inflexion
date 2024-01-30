from modern_greek_accentuation.accentuation import is_accented, where_is_accent, put_accent, count_syllables, \
    put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, remove_all_diacritics, put_accent_on_the_ultimate
from modern_greek_accentuation.resources import vowels
from modern_greek_accentuation.syllabify import modern_greek_syllabify
from modern_greek_inflexion.exceptions import NotLegalAdjectiveException
from modern_greek_inflexion.resources.resources import greek_corpus
from modern_greek_inflexion.resources.variables import (ADJ, ADVERB, ADVERB_COMPARATIVE, COMPARATIVE, INCORRECT_ACCENT, ULTIMATE,
                                                        ANTEPENULTIMATE, PENULTIMATE, ADJ_FEM_OS_ONLY, ADJ_FEM_OS_ALSO)
from modern_greek_inflexion.resources.adj import irregular_comparatives, irregular_comparative_adverbs, adj_grammar_lists


def create_all_basic_adj_forms(adj: str, aklito=False) -> dict:
    """
    :param aklito: if relevant, boolean
    :param adj: masc nom sg form (`ωραίος`)
    :return: dictionary with keys:
    ADJ: masc, fem, neut forms as a string divided with / ('ωραίος/ωραία/ωραίο') if alternatives, they are added and
    separated with a coma
    COMPARATIVE: if exists in form parathetiko + ',' + alt_parathetiko + '/' + uperthetiko + ',' + alt_uperthetiko with
    form only in masc sing nom
    ADVERB: adverb form, if alternatives, then separated with coma
    ADVERB_COMPARATIVE: if exists, adverb_parathetiko + ',' + alt_adverb_parathetiko + '/' + adverb_uperthetiko + ',' + alt_adverb_uperthetiko
    """

    if adj[-2:] == 'ον' and adj + 'τα' in greek_corpus:
        adj = adj[:-2] + 'ων'

    elif adj[-2:] == 'ές' and adj[:-2] + 'ής' in greek_corpus:
        #  ['εκκρεμές', 'λυκαυγές', 'αλκαλοειδές']:
        adj = adj[:-2] + 'ής'
    elif adj[-2:] == 'έν' and adj[:-2] + 'είς' in greek_corpus:
        # ['ανακοινωθέν']:
        adj = adj[:-2] + 'είς'
    elif adj[-2:] == 'ού':
        if adj[:-2] + 'άς' in greek_corpus:
            adj = adj[:-2] + 'άς'
        elif put_accent_on_the_penultimate(adj[:-2] + 'ης') in greek_corpus:
            adj = put_accent_on_the_penultimate(adj[:-2] + 'ης')

    accent = where_is_accent(adj, true_syllabification=True)
    if accent == INCORRECT_ACCENT:
        raise NotLegalAdjectiveException
    if adj[-1] in ['υ', 'ύ'] and not aklito:
        raise NotLegalAdjectiveException

    # default
    masc, fem, neuter = adj, adj, adj
    adj_temp = {ADJ: 'masc,fem,neuter', COMPARATIVE: '', ADVERB: '', ADVERB_COMPARATIVE: ''}

    adj_forms = []
    # most basic case -os

    if adj[-2:] in ['ός', 'ος']:
        masc = adj
        adj_forms.append(masc)

        if accent == ULTIMATE:
            fem = adj[:-2] + 'ή'
        else:
            fem = adj[:-2] + 'η'

        if adj[-3] in vowels and count_syllables(adj) <= 2:
            if accent == ULTIMATE:
                fem = adj[:-2] + 'ά'
            else:
                fem = adj[:-2] + 'α'

        elif adj[-3] in vowels and count_syllables(adj) > 2 and not is_accented(modern_greek_syllabify(adj)[-3]):
            if accent == ULTIMATE:
                fem = adj[:-2] + 'ά'
            else:
                fem = adj[:-2] + 'α'

        if adj[-3] in ['κ', 'θ', 'χ']:

            if accent == ULTIMATE:
                fem_alt = adj[:-2] + 'ιά'
            else:
                fem_alt = adj[:-2] + 'ια'

            # if fem in greek_corpus and fem_alt in greek_corpus:
            #     fem = fem + ',' + fem_alt

            if fem not in greek_corpus and fem_alt in greek_corpus:
                fem = fem_alt

            elif fem in greek_corpus and fem_alt not in greek_corpus:
                fem = fem
            else:
                # for the most part forms on h should be correct, but adj is not very common, so is lacking from db
                # check for -a by looking for genitive on as in db
                if accent == ULTIMATE:
                    gen = adj[:-2] + 'άς'
                    beta_fem = adj[:-2] + 'ά'
                else:
                    gen = adj[:-2] + 'ας'
                    beta_fem = adj[:-2] + 'α'

                if gen in greek_corpus:
                    fem = beta_fem

        elif (adj[-3] not in vowels and put_accent(adj[:-2] + 'η', accent) not in greek_corpus and
              put_accent(adj[:-2] + 'ας', accent) in greek_corpus):

            fem = put_accent(adj[:-2] + 'α', accent)
            # if it's lacking from the db, still the best guess is to leave the form on -h

        if adj in adj_grammar_lists[ADJ_FEM_OS_ALSO]:

            fem = fem + ',' + masc

        elif adj in adj_grammar_lists[ADJ_FEM_OS_ONLY] or ((adj.endswith('ποιός') and fem + 'ς' not in greek_corpus) or adj.endswith('αγωγός') or
                adj.endswith('ουργός')):

            fem = masc

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
            if stem + 'ισσα' in greek_corpus:
                fem = stem + 'ισσα'
            neuter = stem + 'ικο'

        elif where_is_accent(adj) == ULTIMATE and (stem + 'ὶ' in greek_corpus or stem + 'ιά' in greek_corpus):
            # type, hs, ia, i, mostly colors

            masc = adj
            fem = put_accent(stem + 'ια', accent)
            neuter = put_accent(stem + 'ι', accent)

        elif put_accent(stem + 'ους', accent, true_syllabification=False) in greek_corpus:
            # type hs, hs, es
            masc, fem = adj, adj
            neuter = put_accent(stem + 'ες', accent, true_syllabification=False)
            if accent != ULTIMATE and neuter not in greek_corpus:
                neuter = put_accent(stem + 'ες', ANTEPENULTIMATE, true_syllabification=False)

        elif stem + 'ού' in greek_corpus:
            # type kafetzhs kafetzou
            masc = adj
            fem = adj[:-2] + 'ού'
            neuter = adj[:-1] + 'δικο'

        else:
            """
            In cases where my corpus cannot help me, I will surmise that it's hs, a (or issa), iko
            """
            if accent == PENULTIMATE:
                if adj.endswith('ώδης'):
                    masc, fem = adj, adj
                    neuter = stem + 'ες'
                else:
                    masc = adj
                    fem = stem + 'α'
                    if stem + 'ισσα' in greek_corpus:
                        fem = stem + 'ισσα'
                    neuter = stem + 'ικο'
            elif accent == ULTIMATE:
                masc, fem = adj, adj
                neuter = stem + 'ές'

    elif adj[-3:] == 'ους':
        masc, fem = adj, adj
        neuter = adj[:-1] + 'ν'

    elif adj[-3:] == 'ούς':
        masc = adj
        if adj[-4] in vowels or adj[-4] == 'ρ':
            fem = adj[:-3] + 'ά'
        else:
            fem = adj[:-3:] + 'ή'
        neuter = adj[:-1] + 'ν'

    elif adj[-2:] in ['υς', 'ύς']:
        # my database is unfortunately not that great...
        stem = adj[:-2]
        masc = adj
        neuter = adj[:-1]

        fem = stem + 'ιά'

        if fem + 'ς' not in greek_corpus:
            # look for gen because nom fem can be mistaken for acc pl
            fem_eia = stem + 'εία'
            if fem_eia in greek_corpus:
                fem = fem_eia
            if adj.endswith('πολύς'):
                fem = adj[:-5] + 'πολλή'

    elif adj[-2:] in ['ων', 'ών']:
        stem = adj[:-2]
        masc = adj
        fem = None
        neuter = None
        if accent == PENULTIMATE or not accent:
            fem = stem + 'ουσα'

            neuter = stem + 'ον'

        if accent == ULTIMATE or not accent:
            fem = stem + 'ούσα'
            neuter = stem + 'ούν'
            neuter_alt_1 = stem + 'ών'
            neuter_alt_2 = stem + 'ούν'
            neuter_alt_3 = stem + 'όν'
            if neuter + 'τα' in greek_corpus or neuter + 'τες' in greek_corpus:
                fem = stem + 'ούσα'
            elif neuter_alt_1 + 'τα' in greek_corpus or neuter_alt_1 + 'τες' in greek_corpus or adj in ['ζων',
                                                                                                        'κυβερνών',
                                                                                                        'επιζών']:

                fem = stem + 'ώσα'
                neuter = neuter_alt_1
            elif neuter_alt_2 + 'τα' in greek_corpus or neuter_alt_2 + 'τες' in greek_corpus or neuter_alt_2 + 'των' in greek_corpus:
                fem = stem + 'ούσα'
                neuter = neuter_alt_2
            elif neuter_alt_3 + 'τα' in greek_corpus:
                fem = stem + 'ούσα'
                neuter = neuter_alt_3
            if not accent:
                neuter = remove_all_diacritics(neuter)

        # it is also possible, that there are wn, onos
        if adj[:-2] + 'ονος' in greek_corpus or adj[:-2] + 'ονα' in greek_corpus or adj[:-2] + 'ες' in greek_corpus:
            masc, fem = adj, adj
            neuter = adj[:-2] + 'ον'

    elif adj.endswith('είς'):
        # passive aorist participles

        masc = adj
        fem = adj[:-1] + 'σα'
        neuter = adj[:-3] + 'έν'

    elif adj[-2:] in ['ας', 'άς']:

        # pas, pasa pan and active aorist participles
        # pas pasa pan

        pl_nta = adj[:-1] + 'ντα'
        fem_sa = adj[:-1] + 'σα'

        if count_syllables(adj) == 1:
            pl_nta = put_accent(pl_nta, PENULTIMATE)
            fem_sa = put_accent(fem_sa, PENULTIMATE)
        if (pl_nta in greek_corpus or
                adj.endswith('άπας') or
                (adj[-4:] != 'ντας' and
                 adj[-3:] in ['ψας', 'σας', 'ξας'] and
                 put_accent_on_the_antepenultimate(adj[:-1] + 'δικο') not in greek_corpus)):
            masc = adj
            fem = fem_sa
            neuter = adj[:-1] + 'ν'

        elif adj in ['μέλας']:
            masc = adj
            fem = adj[:-2] + 'αινα'
            neuter = adj[:-1] + 'ν'

        elif adj == 'μέγας':
            masc = adj
            fem = 'μαγάλη'
            neuter = 'μέγα'

        elif adj.endswith('ονας'):
            masc = adj
            fem = adj[:-4] + 'ων'
            neuter = adj[:-2]
        elif adj.endswith('σαντας') or adj.endswith('ξαντας') or adj.endswith('ψαντας'):
            # modernized active aorist participles
            masc = adj
            fem = adj[:-4] + 'σα'
            neuter = adj[:-3]

        elif adj.endswith('οντας'):
            masc = adj
            fem = put_accent_on_the_antepenultimate(adj[:-5] + 'ουσα')
            neuter = adj[:-3]
        elif adj.endswith('ώντας'):
            masc = adj
            fem = put_accent_on_the_antepenultimate(adj[:-5] + 'ούσα')
            neuter = adj[:-3]
        elif where_is_accent(adj) in [ULTIMATE, PENULTIMATE]:
            masc = adj
            fem = adj[:-2] + 'ού'
            neuter = adj[:-1] + 'δικο'
            if where_is_accent(adj) == PENULTIMATE:
                fem = adj[:-1]
                neuter = adj[:-2] + 'ικο'

        elif not aklito:
            raise NotLegalAdjectiveException
    # in ['προβεβηκώς', 'κεχηνώς', 'τεθνεώς', 'αφεστώς', 'ενεστώς']
    elif adj.endswith('ώς') and not aklito:
        masc = adj
        fem = adj[:-1] + 'σα'
        neuter = adj
        # rare but sometimes ancient perf participle

    elif adj in ['άρρην']:
        # so rare that it can be solved like that
        masc = adj
        fem = adj
        neuter = masc[:-2] + 'εν'

    elif adj.endswith('εις') and not aklito:
        masc = adj
        fem = adj[:-3] + 'εσσα'
        neuter = adj[:-3] + 'εν'

    elif adj[-2:] in ['ις', 'ιξ', 'υξ', 'αξ', 'ωψ', 'ωρ'] and not aklito:
        """ancient 3rd declension"""
        neuter_3rd = adj[:-1]
        """only for -is"""
        if adj.endswith('ις'):
            neuter = neuter_3rd
        else:
            neuter = '-'
        masc, fem = adj, adj

    elif adj.endswith('εως') and not aklito:
        # attic
        masc, fem = adj, adj
        neuter = adj[:-1] + 'ν'

    else:
        masc, fem, neuter = [adj, adj, adj]

    if aklito:
        masc, fem, neuter = adj, adj, adj

    adj_forms = [masc, fem, neuter]

    adj_temp[ADJ] = '/'.join(adj_forms)

    # παραθετικά

    stem = neuter

    if stem.endswith('ς'):
        stem = stem[:-1] + 'σ'
    elif stem[-3:] in ['ουν', 'ούν']:
        stem = stem[:-1] + 'σ'
    elif stem.endswith('ν'):
        stem = stem[:-1]
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
            alt_uperthetiko = put_accent_on_the_antepenultimate(alt_parathetiko[:-5] + 'τατος')
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
        adj_temp[COMPARATIVE] = parathetika

    # επιρρήματα

    alt_adv = None

    if aklito:
        adverb = neuter

    elif neuter[-1] in ['ο', 'ό']:

        accent = where_is_accent(neuter)
        if accent != ULTIMATE:
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
    elif neuter.endswith('ί') and masc.endswith('ς'):
        # colors
        adverb = put_accent_on_the_ultimate(adj_forms[2] + 'α')

    elif ((masc[-2:] in ['ας', 'άς', 'ων', 'ών'] or masc[-3:] in ['εις', 'είς']) and
          fem[-2:] == 'σα' and neuter[-1] == 'ν'):
        # ancient adverbs

        if put_accent_on_the_penultimate(neuter + 'τως') in greek_corpus:
            adverb = put_accent_on_the_penultimate(neuter + 'τως')
        else:
            adverb = ''

    elif masc[-3:] in ['ους', 'ούς']:
        if accent == ULTIMATE and masc[:-3] + 'ώς' in greek_corpus:
            adverb = masc[:-3] + 'ώς'
        elif put_accent_on_the_penultimate(masc[:-3] + 'οως') in greek_corpus:
            adverb = put_accent_on_the_penultimate(masc[:-3] + 'οως')
        else:
            adverb = ''

    elif masc.endswith('ώς'):
        adverb = ''

    else:
        # for aklita without flags
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

    elif masc in ['άρρην', 'μέλας']:
        adverb = None

    epirrimata = [e for e in [adverb, alt_adv] if e and e in greek_corpus]

    epirrimata = ','.join(epirrimata)
    if epirrimata:
        adj_temp[ADVERB] = epirrimata

    # comparative epirrimata
    adv_parathetika = None

    adverb_parathetiko = alt_adverb_parathetiko = adverb_uperthetiko = alt_adverb_uperthetiko = ''

    if parathetiko:
        adverb_parathetiko = parathetiko[:-2] + 'α'
        if uperthetiko != '-':
            adverb_uperthetiko = ','.join([yp[:-2] + 'α' for yp in uperthetiko.split(',')])
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
        adj_temp[ADVERB_COMPARATIVE] = adv_parathetika

    return adj_temp
