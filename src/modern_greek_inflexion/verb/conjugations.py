from modern_greek_accentuation.accentuation import *

from ..exceptions import NotLegalVerbException
from ..resources import greek_corpus, irregular_passive_roots, irregular_active_roots
from ..resources import EIMAI, PRESENT_ACTIVE_PART_EIMAI, CON1_ACT, CON1_ACT_MODAL, CON2_ACT_MODAL, CON2A_ACT, \
    CON2B_ACT, CON2C_ACT, IMPER_ACT_EIMAI, PARAT2_ACT, EIMAI_PARATATIKOS, CON2B_PASS, CON1_PASS, CON2C_PASS, \
    CON2A_PASS, CON2AB_PASS, MODAL, ACTIVE, IMPERF, PERF, PASSIVE, CON1_PASS_MODAL, CON2_PASS_MODAL, CON2D_ACT, \
    CON2D_PASS, PARAT2E_PASS, CON2E_PASS, PARAT2A_PASS, PARAT1_PASS, PARAT2B_PASS_LOGIA, PARAT2B_PASS, PARAT2C_PASS, \
    PARAT2D_PASS, PRESENT_ACTIVE_PART_1, CON2AB, PAST, ARCH_PASS_AOR, IMPER_ACT_CONT_2A, FIN, \
    IMPER_PASS_AOR_A, IMPER_PASS_CONT_1, IMPER_ACT_AOR_CA, PRESENT_ACTIVE_PART_2, PARAT_ACT_MODAL, \
    AOR_ACT, PRESENT_PASSIVE_PART_2B, PRESENT_ACTIVE_PART_2C, PRESENT_PASSIVE_PART_2E, PRESENT_PASSIVE_PART_1, \
    PRESENT_PASSIVE_PART_2A, PRESENT_PASSIVE_PART_2D, PRESENT_PASSIVE_PART_2AB, IMPER_ACT_CONT_1, IMPER_ACT_CONT_2B, \
    IMPER_ACT_CONT_2C, IMPER_PASS_CONT_2C, IMPER_ACT_AOR_A, IMPER_PASS_CONT_2A, IMPER_ACT_CONT_2D, IMPER_PASS_CONT_2B, \
    IMPER_PASS_CONT_2D, IMPER_PASS_CONT_2E, IMPER_ACT_AOR_B, IMPER_ACT_AOR_C


def create_imp_pass(perf_pass_root):
    # useful for deponentia

    if perf_pass_root[-1] == 'θ':
        form = perf_pass_root[:-1] + 'σου'
    elif perf_pass_root[-2:] == 'φτ':
        form = perf_pass_root[:-2] + 'ψου'

    elif perf_pass_root[-2:] == 'στ':
        form = perf_pass_root[:-2] + 'σου'
    elif perf_pass_root[-2:] == 'χτ':
        form = perf_pass_root[:-2] + 'ξου'
    elif perf_pass_root[-3:] == 'ευτ':
        form = perf_pass_root[:-3] + 'έψου'

    else:
        form = None
    if form:
        form = remove_all_diacritics(form)
        form = put_accent_on_the_penultimate(form)
    if form in greek_corpus:
        return form
    else:
        return ''


def create_regular_perf_root(verb, voice=ACTIVE):
    # create regular aorist roots from present root. For obvious reasons it's only useful for verbs you don't have
    # supplied aorist forms and so it is prone to errors that cannot be eliminated
    perf_root = None
    irregular = False

    multiple_stems = None
    if verb[-1] in ['ω', 'ώ'] or verb[-2:] in ['ει', 'εί'] or verb[-5:] == 'είμαι':
        res = recognize_active_non_past_conjugation(verb)

    else:
        res = recognize_passive_present_continuous_conjugation(verb)

    if not res:
        return None

    root = res['root']
    conjugation = res['conjugation_ind']

    if conjugation == MODAL:
        perf_root = root

    # an idea: to solve problem with irregular verbs that cannot be simply caught because they are combined with
    # some suffix

    # to do: verbs with ancient aorist forms (ekserragi) have to be put in manually, as there is no poin in creating
    # more code, list of such verbs: εξερράγη απεστάλη, συνέβη, συνελήφθη.
    # But code might be useful here, especially that it wont be that complicated. But here
    # check for 1 and 3 person sing.

    if voice == ACTIVE:
        # there are no multiple stems in this category, so do not do anything
        for pair in irregular_active_roots:
            if ',' in pair[1]:
                multiple_perf_roots = []
                for stem in pair[1].split(','):

                    if len(root) >= len(pair[0]) and root[-len(pair[0]):] == pair[0]:
                        beta_perf_root = root[:-len(pair[0])] + stem

                        if (beta_perf_root + 'ω' in greek_corpus) or (
                                beta_perf_root + 'ώ' in greek_corpus
                        ):
                            multiple_perf_roots.append(beta_perf_root)

                if multiple_perf_roots:
                    perf_root = ','.join(multiple_perf_roots)
                    irregular = True
                    multiple_stems = True
                    break

            if len(root) >= len(pair[0]) and root[-len(pair[0]):] == pair[0]:
                beta_perf_root = root[:-len(pair[0])] + pair[1]
                if (beta_perf_root + 'ω' in greek_corpus) or (
                        beta_perf_root + 'ώ' in greek_corpus):
                    perf_root = beta_perf_root
                    irregular = True
                    break

    if voice == PASSIVE:
        for pair in irregular_passive_roots:
            if ',' in pair[1]:
                # that is if many stems
                multiple_perf_roots = []
                for stem in pair[1].split(','):
                    if len(root) >= len(pair[0]) and root[-len(pair[0]):] == pair[0]:

                        beta_perf_root = root[:-len(pair[0])] + stem
                        if (beta_perf_root + 'ώ' in greek_corpus) or (beta_perf_root + 'ω' in greek_corpus) or (
                                beta_perf_root + 'εί' in greek_corpus) or (
                                beta_perf_root + 'ει' in greek_corpus):
                            multiple_perf_roots.append(beta_perf_root)

                if multiple_perf_roots:
                    perf_root = ','.join(multiple_perf_roots)
                    irregular = True
                    multiple_stems = True
                    break

            if len(root) >= len(pair[0]) and root[-len(pair[0]):] == pair[0]:

                for r in pair[1].split(','):

                    beta_perf_root = root[:-len(pair[0])] + r

                    if (beta_perf_root + 'ώ' in greek_corpus) or \
                            (beta_perf_root + 'ω' in greek_corpus) or \
                            (beta_perf_root + 'εί' in greek_corpus) or \
                            (beta_perf_root + 'ει' in greek_corpus):
                        perf_root = beta_perf_root
                        irregular = True
                        break

    if conjugation in [CON1_ACT, CON1_PASS, CON1_ACT_MODAL] and not perf_root:

        if root[-3:] == 'αίν':
            perf_root = root[:-3] + 'άν'
            if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                perf_root = root[:-3] + 'ύν'
                if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                    perf_root = root[:-3] + 'άσ'
                    if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                        perf_root = root[:-3] + 'άξ'
                        if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                            perf_root = root[:-3] + 'ήσ'
        elif root[-2:] in ['σσ', 'ττ', 'χν', 'γγ']:
            perf_root = root[:-2] + 'ξ'
        elif root[-2:] in ['φτ', 'πτ']:
            perf_root = root[:-2] + 'ψ'
        elif root[-1] in ['ν', 'θ', 'δ', 'τ']:

            perf_root = root[:-1] + 'σ'

        elif root[-1] == 'ζ':
            perf_root = root[:-1] + 'ξ'
            if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                perf_root = root[:-1] + 'σ'

        elif root[-1] in ['σκ']:
            perf_root = root[:-2] + 'ξ'
        elif root[-1] in ['κ', 'χ', 'γ']:
            perf_root = root[:-1] + 'ξ'
        elif root[-1] in ['β', 'π', 'φ']:
            perf_root = root[:-1] + 'ψ'
        elif root[-2:] in ['εύ', 'αύ']:
            perf_root = root[:-2] + put_accent_on_syllable(root[-2]) + 'ψ'
            # alternative stem on eus
            alternative_root = root + 'σ'
            if alternative_root + 'ω' in greek_corpus and perf_root + 'ω' not in greek_corpus:
                perf_root = alternative_root

            elif alternative_root + 'ω' in greek_corpus and perf_root + 'ω' in greek_corpus:
                perf_root = perf_root + ',' + alternative_root
                multiple_stems = True

        elif root[-1] in ['ύ', 'ί', 'έ']:
            perf_root = root + 'σ'

        elif root[-1] in ['ρ', 'λ', 'μ', 'ψ', 'σ']:
            perf_root = root

        elif root in ['επέστη']:
            # ancient form
            perf_root = root

    elif conjugation in [CON2A_ACT, CON2B_ACT, CON2A_PASS, CON2B_PASS, CON2C_PASS, CON2_ACT_MODAL] and \
            not perf_root:

        perf_root = root + 'ήσ'

        # εξαιρέσεις
        if root[-2:] == 'χν' and conjugation in [CON2A_ACT, CON2A_PASS] and perf_root + 'ω' not in greek_corpus:
            perf_root = root[:-1] + 'άσ'

        elif root[-2:] == 'ρν' and conjugation in [CON2A_ACT, CON2A_PASS] and perf_root + 'ω' not in greek_corpus:
            perf_root = root[:-1] + 'άσ'
        elif conjugation in [CON2B_ACT, CON2A_ACT]:
            perf_root = root + 'ίσ'

            if perf_root + 'ω' not in greek_corpus:
                perf_root = root + 'ήσ'

        if not ((perf_root + 'ω' in greek_corpus) or (perf_root + 'ου' in greek_corpus) or
                (perf_root + 'ει' in greek_corpus)):
            perf_root = root + 'άσ'

            if not (perf_root + 'ω' in greek_corpus or
                    perf_root + 'ου' in greek_corpus or
                    perf_root + 'ει' in greek_corpus):
                perf_root = root + 'έσ'
                if not ((perf_root + 'ω' in greek_corpus) or
                        (perf_root + 'ου' in greek_corpus) or
                        perf_root + 'ει' in greek_corpus):

                    perf_root = root + 'άξ'
                    if not ((perf_root + 'ω' in greek_corpus) or
                            (perf_root + 'ου' in greek_corpus) or
                            perf_root + 'ει' in greek_corpus):
                        perf_root = root + 'έξ'
                        if not ((perf_root + 'ω' in greek_corpus) or
                                (perf_root + 'ου' in greek_corpus) or
                                perf_root + 'ει' in greek_corpus):
                            perf_root = root + 'ήξ'
        # special case for compounds with ποιω that are not in my db for some reasons

        if root[-3:] == 'ποι' and conjugation in [CON2B_ACT, CON2B_PASS]:
            perf_root = root + 'ήσ'

    elif conjugation == CON2C_ACT and not perf_root:
        # my best guess is to remove 2 last syllables and to add αψα

        irregular_2c_roots = [['τρώ', 'φά'], ['λέ', 'π'], ['τρώγ', 'φάγ']]

        for pair in irregular_2c_roots:

            if len(root) >= len(pair[0]) and root[-len(pair[0]):] == pair[0]:

                beta_perf_root = root[:-len(pair[0])] + pair[1]
                if beta_perf_root + 'ω' in greek_corpus:
                    perf_root = beta_perf_root
                    break
        if root[-2:] == 'ού' and not perf_root:
            # akouw
            perf_root = root + 'σ'
        elif root[-2:] in diphtongs:
            perf_root = root[:-2] + 'άψ'
            if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                perf_root = root + 'ξ'
        else:
            perf_root = root[:-1] + 'άψ'

    elif conjugation == CON2D_ACT and not perf_root:
        # archaic on o
        perf_root = root + 'ώσ'

    if voice == PASSIVE and conjugation in [CON1_ACT, CON1_PASS, CON1_PASS_MODAL,
                                            CON2_PASS_MODAL, CON2D_ACT, CON2D_PASS] and not irregular:

        root = remove_all_diacritics(root)
        if root[-3:] == 'αιν':
            perf_root = root[:-3] + 'ανθ'
            if perf_root + 'ώ' not in greek_corpus:
                perf_root = root[:-3] + 'υνθ'
                if perf_root + 'ώ' not in greek_corpus:
                    perf_root = root[:-2] + 'θ'
                    if perf_root + 'ώ' not in greek_corpus:
                        perf_root = root[:-2] + 'χτ'
                        if perf_root + 'ώ' not in greek_corpus:
                            perf_root = root[:-2] + 'στ'
        elif root[-2:] in ['σσ', 'ττ', 'χν', 'σκ']:
            perf_root = root[:-2] + 'χτ'

        elif len(root) > 5 and root[-6:] == 'δεικνυ':

            perf_root = root[:-3] + 'χτ'

        elif root[-2:] in ['πτ', 'φτ']:
            perf_root = root[:-2] + 'φτ'

        elif root[-1] in ['ν', 'τ', 'δ']:
            perf_root = root[:-1] + 'θ'
            if perf_root + 'ώ' not in greek_corpus:
                perf_root = root + 'θ'
                if perf_root + 'ώ' not in greek_corpus:
                    perf_root = root[:-1] + 'στ'

        elif root[-1] in ['θ', 'σ']:
            perf_root = root[:-1] + 'στ'

        elif root[-1] == 'ζ':
            perf_root = root[:-1] + 'χτ'
            if perf_root + 'ώ' not in greek_corpus:
                perf_root = root[:-1] + 'στ'
                if perf_root + 'ώ' not in greek_corpus:
                    perf_root = root[:-1] + 'θ'

        elif root[-1] in ['κ', 'χ', 'γ']:
            perf_root = root[:-1] + 'χτ'
            if perf_root + 'ώ' not in greek_corpus:
                perf_root = root[:-1] + 'χτ'

        elif root[-1] in ['β', 'π', 'φ', 'ψ']:
            perf_root = root[:-1] + 'φτ'

        elif root[-2:] in ['ευ', 'αυ']:
            perf_root = root + 'τ'

        elif root[-1] in ['υ', 'ρ', 'λ', 'ι', 'μ', 'ε']:
            perf_root = root + 'ηθ'
            if perf_root + 'ώ' not in greek_corpus:
                perf_root = root + 'θ'

        if conjugation == CON2D_ACT:
            perf_root = root + 'ωθ'
        if perf_root:
            perf_root = remove_all_diacritics(perf_root)

    if voice == PASSIVE and \
            conjugation in [CON2A_ACT, CON2B_ACT, CON2C_ACT, CON2A_PASS, CON2B_PASS, CON2E_PASS,
                            CON2C_PASS, CON2AB_PASS] and not irregular:

        perf_root = root + 'ηθ'

        if root[-2:] in ['ρν', 'χν'] and (perf_root + 'ώ' not in greek_corpus):
            perf_root = root[:-1] + 'αστ'
        # εξαιρέσεις
        if not (perf_root + 'ώ' in greek_corpus):

            if conjugation in [CON2A_ACT, CON2B_ACT, CON2B_PASS, CON2B_PASS, CON2A_PASS, CON2AB]:
                perf_root = root + 'αστ'
                if not (perf_root + 'ώ' in greek_corpus):
                    perf_root = root + 'εστ'
                    if not (perf_root + 'ώ' in greek_corpus):
                        perf_root = root + "εθ"
                        if not (perf_root + 'ώ' in greek_corpus):
                            perf_root = root + "αχτ"
                            if not (perf_root + 'ώ' in greek_corpus):
                                perf_root = root + "εχτ"
                                if not (perf_root + 'ώ' in greek_corpus):
                                    perf_root = root + "ηχτ"
                                    if not (perf_root + 'ώ' in greek_corpus):
                                        perf_root = root + "ιστ"

        # σπεσιαλ case for compounds with poiw
        if root[-3:] == 'ποι' and conjugation in [CON2B_ACT, CON2B_PASS]:
            perf_root = root + 'ηθ'
        perf_root = remove_all_diacritics(perf_root)

    if not perf_root:
        return

    if (perf_root and
        ((perf_root + 'ω' in greek_corpus) or
         (perf_root + 'ώ' in greek_corpus) or
         (perf_root + 'εί' in greek_corpus))) or \
            root[-3:] == 'ποι' or \
            multiple_stems:

        return perf_root
    else:
        return None


def recognize_active_non_past_conjugation(verb, aspect=IMPERF, tense=FIN, voice=ACTIVE):
    # can be used for aspects: 'continuous', 'simple', 'simple_passive'
    # verb is expected to be in 1st person sg, else it's assumed it's modal verb
    verb = verb.strip()
    root = ''
    conjugation_ind = ''
    conjugation_imp = ''
    conjugation_part = ''

    # recognize conjugation

    if verb[-2:] == 'άω' and verb and count_syllables(verb) > 2 and verb not in ['συνφάω', 'πρωτοφάω', 'αποφάω',
                                                                                 'καταφάω', 'καλοφάω', 'γλωσσοφάω',
                                                                                 'παραφάω', 'ψωμοφάω', 'ψιλοφάω']:
        root = verb[:-2]

        conjugation_ind = CON2A_ACT
        conjugation_imp = IMPER_ACT_CONT_2A
        conjugation_part = PRESENT_ACTIVE_PART_2

    # συνηρημενα
    elif ((verb[-1:] == 'ω' and verb[-2] in ['έ', 'ά', 'ώ']) and (
            verb[-3:] not in ['δέω', 'ρέω', 'χέω'] and verb[-4:] not in ['πνέω', 'πλέω'])) or (
            verb[-1] == 'ω' and len(verb) > 2 and verb[-3:-1] in ['αί', 'ού']) or verb == 'πάω':
        root = verb[:-1]
        conjugation_ind = CON2C_ACT
        conjugation_imp = IMPER_ACT_CONT_2C
        conjugation_part = PRESENT_ACTIVE_PART_2C
    elif (verb[-1] == 'ώ') or (verb[-1:] == 'ω' and count_syllables(verb) == 1):
        root = verb[:-1]

        conjugation_ind = CON2B_ACT
        conjugation_imp = IMPER_ACT_CONT_2B
        conjugation_part = PRESENT_ACTIVE_PART_2
        # contracted άω to ώ
        if verb[:-1] + 'είς' not in greek_corpus and verb[:-1] + 'ά' in greek_corpus or (
                verb[:-1] + 'άς' in greek_corpus and
                verb[:-1] + 'άτε' in greek_corpus
        ):

            conjugation_ind = CON2A_ACT
            conjugation_imp = IMPER_ACT_CONT_2A
            conjugation_part = PRESENT_ACTIVE_PART_2


        elif verb[:-1] + 'είς' not in greek_corpus and verb[:-1] + 'οί' in greek_corpus:

            conjugation_ind = CON2D_ACT
            conjugation_imp = IMPER_ACT_CONT_2D
            conjugation_part = PRESENT_ACTIVE_PART_2

    elif verb[-1:] == 'ω':

        root = verb[:-1]
        conjugation_ind = CON1_ACT
        conjugation_imp = IMPER_ACT_CONT_1
        conjugation_part = PRESENT_ACTIVE_PART_1

    elif verb == 'είμαι':
        root = ''
        conjugation_ind = EIMAI
        conjugation_imp = IMPER_ACT_EIMAI
        conjugation_part = PRESENT_ACTIVE_PART_EIMAI

    elif len(verb) > 5 and verb[-5:] == 'είμαι':
        root = verb[:-5]
        conjugation_ind = EIMAI

        conjugation_imp = PRESENT_ACTIVE_PART_EIMAI

    elif verb == '':
        # sometimes there is no simple future form
        pass

    elif verb[-2:] in ['ει', 'εί']:
        root = verb[:-2]
        conjugation_ind = CON1_ACT_MODAL
        if verb[-2:] == 'εί':
            conjugation_ind = CON2_ACT_MODAL

    else:
        # else it's assumed it's modal
        return {'aspect': aspect, 'tense': tense, 'voice': voice, 'root': verb,
                'conjugation_ind': MODAL, 'conjugation_imp': '', 'conjugation_part': ''}

    if aspect == PERF:
        # con_ind already recognized
        conjugation_part: ''

        conjugation_imp = IMPER_ACT_AOR_A

        if count_syllables(verb) == 1:
            conjugation_imp = IMPER_ACT_AOR_C
        elif root == '':
            # sometimes there is no simple future form
            pass

        elif (root[-1] not in ['σ', 'ψ', 'ξ', 'ρ', 'λ'] or root in ['πέσ']) and verb != 'φάω':
            conjugation_imp = IMPER_ACT_AOR_B
            # anebainw
            if conjugation_ind == CON2B_ACT and put_accent_on_the_penultimate(root + 'α') in greek_corpus:
                conjugation_imp = IMPER_ACT_AOR_CA

    if aspect == 'perf' and voice == PASSIVE:
        # for future passive participle logic is implemented separately
        conjugation_part = ''

        conjugation_imp = IMPER_PASS_AOR_A
    return {'aspect': aspect, 'voice': voice, 'tense': tense,
            'root': root,
            'conjugation_ind': conjugation_ind,
            'conjugation_imp': conjugation_imp,
            'conjugation_part': conjugation_part}


def recognize_passive_present_continuous_conjugation(verb):
    verb = verb.strip()

    if verb != 'είμαι' and len(verb) < 6:
        # maybe unnecessary, but one more way to catch problematic input
        print(verb + ' doesnt seem to be a correct verb form')
        raise NotLegalVerbException

    elif verb[-4:] == 'ομαι':
        root = verb[:-4]
        conjugation_ind = CON1_PASS
        conjugation_imp = IMPER_PASS_CONT_1
        conjugation_part = PRESENT_PASSIVE_PART_1

    elif verb[-5:] == "ιέμαι":
        root = verb[:-5]
        conjugation_ind = CON2A_PASS
        conjugation_imp = IMPER_PASS_CONT_2A
        conjugation_part = PRESENT_PASSIVE_PART_2A

    elif verb[-5:] == 'ούμαι':
        root = verb[:-5]
        conjugation_ind = CON2B_PASS
        conjugation_imp = IMPER_PASS_CONT_2B
        conjugation_part = PRESENT_PASSIVE_PART_2B

    elif verb[-4:] == 'άμαι':
        root = verb[:-4]
        conjugation_ind = CON2C_PASS
        conjugation_imp = IMPER_PASS_CONT_2C
        conjugation_part = PRESENT_PASSIVE_PART_2B

    elif verb[-4:] == 'ώμαι':
        root = verb[:-4]
        conjugation_ind = CON2AB_PASS
        conjugation_imp = IMPER_PASS_CONT_2C
        conjugation_part = PRESENT_PASSIVE_PART_2AB

    elif verb[-4:] in ['εμαι', 'υμαι'] or verb[-5:] in ['είμαι', 'ειμαι']:
        root = verb[:-3]
        conjugation_ind = CON2D_PASS
        conjugation_imp = IMPER_PASS_CONT_2D
        conjugation_part = PRESENT_PASSIVE_PART_2D

    elif verb[-4:] == 'αμαι':
        root = verb[:-4]
        conjugation_ind = CON2E_PASS
        conjugation_imp = IMPER_PASS_CONT_2E
        conjugation_part = PRESENT_PASSIVE_PART_2E

    elif verb[-4:] in ['εται', 'άται', 'υται'] or verb[-5:] in ['είται', 'ειται', 'ιέται']:
        root = verb[:-4]
        if verb[-5:] in ['είται', 'ειται', 'ιέται']:
            root = verb[:-5]
        conjugation_ind = CON1_PASS_MODAL
        conjugation_imp = ''
        conjugation_part = ''

    elif verb[-5:] in ['είται', 'ειται', 'ιέται'] or verb[-4:] in ['άται', 'υται']:
        root = verb[:-5]
        if verb[-4:] in ['άται', 'εται']:
            root = verb[:-4]
        conjugation_ind = CON2_PASS_MODAL
        conjugation_imp = ''
        conjugation_part = ''

    else:
        return {'aspect': IMPERF, 'voice': PASSIVE, 'tense': FIN, 'root': verb,
                'conjugation_ind': MODAL, 'conjugation_imp': '', 'conjugation_part': ''}

    return {'aspect': IMPERF, 'voice': PASSIVE, 'tense': FIN, 'root': root,
            'conjugation_ind': conjugation_ind, 'conjugation_imp': conjugation_imp,
            'conjugation_part': conjugation_part}


def recognize_past_conjugation(verb, lemma, aspect=IMPERF, voice=ACTIVE):
    verb = verb.strip()
    root = verb[:-1]

    conjugation_ind = AOR_ACT

    if root[-3:] == 'ούσ':
        conjugation_ind = PARAT2_ACT

    elif verb in ['ήμουν', 'παραήμουν']:
        conjugation_ind = EIMAI_PARATATIKOS
        root = verb[:-5]

    elif verb[-1] in ['ν', 'η']:
        conjugation_ind = ARCH_PASS_AOR

    elif verb[-1] != 'α':
        conjugation_ind = MODAL
        root = verb
        if verb[-1] == 'ε':
            conjugation_ind = PARAT_ACT_MODAL
            root = verb[:-1]

    if voice == PASSIVE and aspect == IMPERF:
        root, conjugation_ind = recognize_passive_past_continuous_conjugation(lemma, verb)

    return {'aspect': aspect, 'voice': voice, 'tense': PAST, 'root': root,
            'conjugation_ind': conjugation_ind}


def recognize_passive_past_continuous_conjugation(lemma, verb):
    verb = verb.strip()
    root = None
    if len(verb) >= 7 and 'ιόμουν' in verb[-7:]:
        if verb[-1] == 'ν':
            root = verb[:-6]
        else:
            # if iomouna
            root = verb[:-7]
        conjugation_ind = PARAT2A_PASS

    elif len(verb) >= 6 and 'όμουν' in verb[-6:]:
        if verb[-5:] == 'όμουν':
            root = verb[:-5]
        else:
            # if omouna
            root = verb[:-6]
        conjugation_ind = PARAT1_PASS
        # if koimamai
        if lemma[-4:] == 'άμαι':
            conjugation_ind = PARAT2C_PASS
            root = verb[:-5]
        elif lemma[-4:] == 'έμαι':
            conjugation_ind = PARAT2D_PASS
            root = verb[:-5]
    elif len(verb) >= 7 and 'ούμουν' in verb[-7:]:
        if verb[-6:] == 'ούμουν':
            root = verb[:-6]
        else:
            # if ούmouna
            root = verb[:-7]
        conjugation_ind = PARAT2B_PASS

    elif len(verb) >= 6 and 'ούμην' in verb[-5:]:
        if verb[-5:] == 'ούμην':
            root = verb[:-5]

        conjugation_ind = PARAT2B_PASS_LOGIA

    elif len(verb) >= 5 and 'έμην' in verb[-4:]:

        if verb[-4:] == 'έμην':
            root = verb[:-4]

        conjugation_ind = PARAT2D_PASS
    elif len(verb) >= 5 and 'άμην' in verb[-4:]:

        if verb[-4:] == 'άμην':
            root = verb[:-4]

        conjugation_ind = PARAT2E_PASS

    elif 'ήμουν' in verb:
        root = ''
        conjugation_ind = EIMAI_PARATATIKOS

    else:
        return verb, MODAL

    if root:
        return root, conjugation_ind
    else:
        raise NotLegalVerbException
