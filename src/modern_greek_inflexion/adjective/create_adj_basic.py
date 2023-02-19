from modern_greek_accentuation.accentuation import is_accented, where_is_accent, put_accent, count_syllables, \
    put_accent_on_the_antepenultimate, put_accent_on_the_penultimate, remove_all_diacritics, put_accent_on_the_ultimate
from modern_greek_accentuation.resources import vowels
from modern_greek_accentuation.syllabify import modern_greek_syllabify
from modern_greek_accentuation.resources import ULTIMATE, ANTEPENULTIMATE, PENULTIMATE
from ..exceptions import NotLegalAdjectiveException
from ..resources import greek_corpus, irregular_comparatives, irregular_comparative_adverbs, ADJ, ADVERB,\
    ADVERB_COMPARATIVE, COMPARATIVE

def create_all_basic_adj_forms(adj, aklito=False):
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
    elif adj[-1] == 'ί' and adj[:-1] + 'ής' in greek_corpus:
        adj = adj[:-1] + 'ής'
    accent = where_is_accent(adj, true_syllabification=False)

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

            if fem in greek_corpus and fem_alt in greek_corpus:
                fem = fem + ',' + fem_alt

            elif fem not in greek_corpus and fem_alt in greek_corpus:
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

            # if it's lacking from the db, still the best guess is to leave the form on -h

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
            # type kafetzhs kafetzou, but is it a adj?
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

    elif adj[-2:] in ['υς', 'ύς'] or adj in ['γλυκύ']:
        # my database is unfortunately not that great...
        stem = adj[:-2]
        masc = adj
        neuter = adj[:-1]
        if adj in ['γλυκύ']:
            # unfortunately there are some mistakes in my word list wherever forms are given as lemma
            # and so I have to correct them in this way
            stem = adj[:-1]
            masc = adj + 'ς'
            neuter = adj

        fem = stem + 'ιά'

        if fem + 'ς' not in greek_corpus:
            # look for gen because nom fem can be mistaken for acc pl
            fem_eia = stem + 'εία'
            if fem_eia in greek_corpus:
                fem = fem_eia
            if adj[-5:] == 'πολύς':
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
            if not accent:
                neuter = remove_all_diacritics(neuter)

        # it is also possible, that there are wn, onos
        if adj[:-2] + 'ονος' in greek_corpus:
            masc, fem = adj, adj
            neuter = adj[:-2] + 'ον'

    elif adj[-3:] == 'είς':
        # passive aorist participles
        if not adj[:-3] + 'έντα' in greek_corpus:
            raise NotLegalAdjectiveException
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
        if pl_nta in greek_corpus or adj[-4:] == 'άπας':
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

        elif adj[-4:] == 'ονας':
            masc = adj
            fem = adj[:-4] + 'ων'
            neuter = adj[:-2]
        elif adj[-4:] == 'ντας':
            masc = adj
            fem = adj[:-5] + 'ούσα'
            neuter = adj[:-3]
        elif where_is_accent(adj) in [ULTIMATE, PENULTIMATE]:
            masc = adj
            fem = adj[:-2] + 'ού'
            neuter = adj[:-1] + 'δικο'
            if where_is_accent(adj) == PENULTIMATE:
                fem = adj[:-1]
                neuter = adj[:-2] + 'ικο'

        else:
            raise NotLegalAdjectiveException

    elif adj in ['προβεβηκώς', 'κεχηνώς', 'τεθνεώς', 'αφεστώς', 'ενεστώς']:
        masc = adj
        fem = adj[:-1] + 'σα'
        neuter = adj
        # rare but sometimes ancient perf participle

    elif adj in ['άρρην']:
        # so rare that it can be solved like that
        masc = adj
        fem = adj
        neuter = masc[:-2] + 'εν'

    elif adj in ['περίφροντις', 'φέρελπις', 'άφροντις', 'φιλόπατρις', 'μόνορχις', 'παλίμπαις', 'πολύφροντις',
                 'αρνησίπατρις', 'άπολις', 'άπατρις', 'αφιλόπατρις', 'ενήλιξ', 'πυρρόθριξ', 'δασύθριξ', 'ουλόθριξ',
                 'κεντρόφυξ', 'πυρρόθριξ', 'υπερήλιξ', 'βλαξ', 'ομήλιξ', 'υπερμέτρωψ', 'κεντρόφυξ', 'μεσήλιξ']:
        masc, fem = adj, adj
        neuter = '-'

    elif adj in ['εύχαρις', 'επίχαρις', 'άχαρις']:
        masc, fem = adj, adj
        neuter = adj[:-1]

    elif adj in ['ίλεως']:
        masc, fem = adj, adj
        neuter = adj[:-1] + 'ν'

    elif adj[-2:] == 'ωρ':
        masc, fem = adj, adj
        neuter = '-'

    else:
        masc, fem, neuter = adj, adj, adj

    if aklito:
        masc, fem, neuter = adj, adj, adj


    try:
        adj_forms = [masc, fem, neuter]
    except:
        raise NotLegalAdjectiveException
    # if these are referenced before assignment, it means the adj cannot be processed, as it either
    # doesn't exist or I have too small dictionary, so it cannot be recognized


    adj_temp[ADJ] = '/'.join(adj_forms)

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

    if neuter[-1] in ['ο', 'ό']:

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


