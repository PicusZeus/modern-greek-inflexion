import pickle
from .greek_tables import irregular_active_roots, irregular_passive_roots
from modern_greek_accentuation.accentuation import *
from modern_greek_accentuation.syllabify import modern_greek_syllabify
from .greek_tables import conjugations


with open('el_GR.pickle', 'rb') as file:
    greek_corpus = pickle.load(file)


def find_alternative_roots(ending, stem):
    # return a list of possible verb roots for a given form that consists of an ending and stem

    alternative_roots = []

    if ending in ['αμε', 'ατε', 'ανε']:
        # past tenses
        # strip accent
            
        new_root = remove_all_diacritics(stem)
        syllables = modern_greek_syllabify(new_root)

        if len(syllables) == 1:
            # add augment
            augmented_roots = []
            if not has_vowel(new_root[0]):
                e = 'έ' + new_root
                h = 'ή' + new_root
                augmented_roots.extend([e, h])
            elif new_root[:2] == 'ευ':
                hu = 'ηύ' + new_root[2:]
                augmented_roots.append(hu)
            elif new_root[0] == 'έ':
                e_h = 'ή' + new_root[1:]
                augmented_roots.append(e_h)

            alternative_roots.extend(augmented_roots)
        else:
            # internal augment
            
            # move accent
            accented_syllable = put_accent_on_syllable(syllables[-2])
            syllables[-2] = accented_syllable
            new_root = ''.join(syllables)
            alternative_roots.append(new_root)

    elif ending in ['όμαστε', 'όσαστε']:
        # if ending 4, 5 act+pass (omaste, osaste)
        syllables = modern_greek_syllabify(stem)
        accented_syllable = put_accent_on_syllable(syllables[-1])
        syllables[-1] = accented_syllable
        new_root = ''.join(syllables)
        alternative_roots.append(new_root)

    elif ending == 'ονταν':
        new_root = remove_all_diacritics(stem)

        alternative_roots.append(new_root)
        
    return alternative_roots


def augment_prefixed_stem(stem):
    # this function checks if a given stem is prefixed by an applicable prefix and augment
    # it if it is, returns list of proposed augmented stems,
    # input stem must be anaccented
    res = []
    for pref in prefix_list_that_allow_augmentaion:
        if len(stem)> len(pref) and pref == stem[:len(pref)]:
            res.append(pref + 'ε' + stem[len(pref):])

    for pref in dict_of_augmented_prefixes.keys():
        
        if len(stem)>len(pref) and pref == stem[:len(pref)]:
            
            res.append(dict_of_augmented_prefixes[pref] + stem[len(pref):])
    
    return res





def create_all_participle_forms(participle, masc_endings, fem_endings, neuter_endings):
    # input is nom sg m (agaphmenos)
    # different accentuation options are possible, (I mean movable accent)
    # you can add them later
    # endings need to be a list of class instances: endings.number.number = 'sg', or 'pl'
    # endings.case.case = case for a given ending
    result = {'sg': {'m': {}, 'f': {}, 'n': {}}, 'pl': {'m': {}, 'f': {}, 'n': {}}}
    root = participle[:-2]

    for gender, endings in [('m', masc_endings), ('f', fem_endings), ('n', neuter_endings)]:
        for ending in endings:
            number = ending.number.number
            case= ending.case.case
            result[number][gender][case] = root + ending.ending

    return result


def create_pres_active_participle(root, ending):
    # accentuation is not a problem here
    form = root + ending

    return form


def create_pres_passive_participle(root, ending):
    # returns nom sg, that can be later used to create other forms

    form = root + ending
    form = remove_all_diacritics(form)
    form = put_accent_on_the_antepenultimate(form)

    return form


def create_regular_perf_participle(pass_perf_root):
    #returns nom sg, that can be later used to create other forms
    form = None
    
    if pass_perf_root[-1] == 'θ':
        form = pass_perf_root[:-1] + 'μενος'

    elif pass_perf_root[-2:] in ['στ']:
        form = pass_perf_root[:-2] + 'σμενος'

    elif pass_perf_root[-2:] == 'χτ':
        form = pass_perf_root[:-2] + 'γμενος'

    elif pass_perf_root[-2:] == 'φτ':
        form = pass_perf_root[:-2] + 'μμενος'

    elif pass_perf_root[-3:] == 'ευτ':
        form = pass_perf_root[:-3] + 'εμμενος'

    if form:

        form = remove_all_diacritics(form)

        form = put_accent_on_the_penultimate(form)

    return form


def create_imp_pass(perf_pass_root):
    #useful for deponentia
    
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
    return form


def create_regular_perf_root(verb, voice='active'):

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
        print('conjugation not recognized: ' + verb)
        return None

    root = res['root']
    conjugation = res['conjugation_ind']

    if conjugation == 'modal':
        perf_root = root


    # the idea: to solve problem with irregular verbs that cannot be simply caught because they are combined with
    # some suffix

    # to do: verbs with ancient aorist forms (ekserragi) have to be put in manually, as there is no poin in creating
    # more code, list of such verbs: εξερράγη απεστάλη, συνέβη, συνελήφθη. But code might be useful here, especially that it wont be that complicated. But here
    # check for 1 and 3 person sing.

    if voice == 'active':
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

    if voice == 'passive':
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
                            (beta_perf_root + 'ω' in greek_corpus) or\
                            (beta_perf_root + 'εί' in greek_corpus) or\
                            (beta_perf_root + 'ει' in greek_corpus):

                        perf_root = beta_perf_root
                        irregular = True
                        break

    if conjugation in ['con1_act', 'con1_pass', 'con1_act_modal'] and not perf_root:

        if root[-3:] == 'αίν':
            perf_root = root[:-3] + 'άν'
            if perf_root + 'ω' not in greek_corpus or perf_root + 'ει' not in greek_corpus:
                perf_root = root[:-3] + 'ύν'
                if perf_root + 'ω' not in greek_corpus  or perf_root + 'ει' not in greek_corpus:
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
            if perf_root + 'ω' not in greek_corpus  or perf_root + 'ει' not in greek_corpus:
                perf_root = root[:-1] + 'σ'

        elif root[-1] in ['σκ']:
            perf_root = root[:-2] + 'ξ'
        elif root[-1] in ['κ', 'χ', 'γ']:
            perf_root = root[:-1] + 'ξ'
        elif root[-1] in ['β', 'π', 'φ']:
            perf_root = root[:-1] + 'ψ'
        elif root[-2:] in ['εύ', 'αύ']:
            perf_root = root[:-2] + put_accent_on_syllable(root[-2]) + 'ψ'
            #alternative stem on eus
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

    elif conjugation in ['con2a_act', 'con2b_act', 'con2a_pass', 'con2b_pass', 'con2c_pass', 'con2_act_modal'] and \
            not perf_root:

        perf_root = root + 'ήσ'
        # εξαιρέσεις
        if root[-2:] == 'χν' and conjugation in ['con2a_act', 'con2a_pass']:
            perf_root = root[:-1] + 'άσ'

        elif root[-2:] == 'ρν' and conjugation in ['con2a_act', 'con2a_pass']:
            perf_root = root[:-1] + 'άσ'
        elif conjugation in ['con2b_act', 'con2a_act']:
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
                        perf_root + 'ει'  in greek_corpus):

                    perf_root = root + 'άξ'
                    if not ((perf_root + 'ω' in greek_corpus) or
                            (perf_root + 'ου' in greek_corpus) or
                            perf_root + 'ει'  in greek_corpus):
                        perf_root = root + 'έξ'
                        if not ((perf_root + 'ω' in greek_corpus) or
                                (perf_root + 'ου' in greek_corpus) or
                                perf_root + 'ει' in greek_corpus):
                            perf_root = root + 'ήξ'
        # special case for compounds with ποιω that are not in my db for some reasons

        if root[-3:] == 'ποι' and conjugation in ['con2b_act', 'con2b_pass']:

            perf_root = root + 'ήσ'

    elif conjugation == 'con2c_act' and not perf_root:
        # my best guess is to remove 2 last syllables and to add αψα

        irregular_2c_roots = [['τρώ', 'φά'], ['λέ', 'π'], ['τρώγ', 'φάγ']]

        for pair in irregular_2c_roots:

            if len(root) >= len(pair[0]) and root[-len(pair[0]):] == pair[0]:

                beta_perf_root = root[:-len(pair[0])] + pair[1]
                if beta_perf_root + 'ω' in greek_corpus:
                    perf_root = beta_perf_root
                    break
        if root[-2:] == 'ού' and not perf_root:
            #akouw
            perf_root = root + 'σ'
        elif root[-2:] in diphtongs:
            perf_root = root[:-2] + 'άψ'
            if perf_root + 'ω' not in greek_corpus  or perf_root + 'ει' not in greek_corpus:
                perf_root = root + 'ξ'
        else:
            perf_root = root[:-1] + 'άψ'

    elif conjugation == 'con2d_act' and not perf_root:
        # archaic on o
        perf_root = root + 'ώσ'

    if voice == 'passive' and \
            conjugation in ['con1_act', 'con1_pass', 'con1_pass_modal', 'con2_pass_modal', 'con2d_act', 'con2d_pass'] and \
            not irregular:


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

        if conjugation == 'con2d_act':
            perf_root = root + 'ωθ'

        perf_root = remove_all_diacritics(perf_root)

    if voice == 'passive' and \
            conjugation in ['con2a_act', 'con2b_act', 'con2c_act', 'con2a_pass', 'con2b_pass', 'con2e_pass', 'con2c_pass', 'con2ab_pass'] and not irregular:

        perf_root = root + 'ηθ'

        if root[-2:] in ['ρν', 'χν'] and (perf_root + 'ώ' not in greek_corpus):
            perf_root = root[:-1] + 'αστ'
        # εξαιρέσεις
        if not (perf_root + 'ώ' in greek_corpus):

            if conjugation in ['con2a_act', 'con2b_act', 'con2b_pass', 'con2b_pass', 'con2a_pass', 'con2ab']:
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
        if root[-3:] == 'ποι' and conjugation in ['con2b_act', 'con2b_pass']:
            perf_root = root + 'ηθ'
        perf_root = remove_all_diacritics(perf_root)

    if not perf_root:
        print('perf_root not created for verb: ' + verb)
        # raise ValueError

    if (perf_root and
        ((perf_root + 'ω' in greek_corpus) or
         (perf_root + 'ώ' in greek_corpus) or
         (perf_root + 'εί' in greek_corpus))) or\
            root[-3:] == 'ποι' or\
            multiple_stems:

        return perf_root
    else:
        return None


def stemmer(root, con_type, lemma='', root2='', sqlalchemy=True):
    # lemma is always pres
    # in modals root equals to the single form
    # designed to use with sql, but with a different flag it
    # will use as source dict from resources

    # returns all personal forms for a given con_type
    # endings is a list of instances of a ending class

    forms = {'sg': {'pri': [], 'sec': [], 'ter': []}, 'pl': {'pri': [], 'sec': [], 'ter': []}}
    if con_type == 'modal':

        verb = root
        
        forms['sg']['ter'].append(verb)
        return forms

    if sqlalchemy:
        endings = ModernGreekConjugationModel.query.filter_by(
            conjugation_name=con_type).first().endings

    else:
        # mimicking sqlalchemy classes
        endings = []
        all_endings = conjugations[con_type]
        for number in all_endings.keys():
            for person in all_endings[number].keys():
                for single_ending in all_endings[number][person]:
                    ending = single_ending
                    ending_inst = Ending(number, person, ending)
                    endings.append(ending_inst)


    for ending in endings:
        # fix bug with imperative passive
        # accentuation
        number = ending.number.number
        person = ending.person.person
        form = root + ending.ending
        # special case for pass_imp
        if con_type == 'imper_pass_aor_a' and number == 'sg':
        # this logic should cover most instances of pass imper
            if root2:
                if root2[-1] == 'σ':
                    form = root2 + 'ου'
                    form = remove_all_diacritics(form)
                    form = put_accent_on_the_penultimate(form)

                else:
                    form = ''
            else:
                form = create_imp_pass(root)
                # in some cases of irregular verb it returns None

                continue

        length_of_ending = count_syllables(ending.ending)
        # some verbs have irregular accent in aorist (υπήρξα)

        if count_syllables(form) == 1:
            form = remove_all_diacritics(form)

        elif con_type == 'aor_act' and length_of_ending > 1:

            pres_form = lemma

            form = remove_all_diacritics(form)

            form = deaugment_prefixed_stem(form)

            form = put_accent_on_past_tense(form, pres_form)

        elif con_type == 'con1_pass' and number == 'pl' and person in ['pri', 'sec']:
            form = remove_all_diacritics(form)
            form = put_accent_on_the_antepenultimate(form)

        elif con_type == 'parat1_pass' and number == 'pl' and person == 'ter':

            form = remove_all_diacritics(form)
            form = put_accent_on_the_antepenultimate(form)
        elif con_type == 'parat1_pass':
            # in the rest cases it's best to simply add endings to unaccented root
            # it's only needed in the first con
            root = remove_all_diacritics(root)
            form = root + ending.ending

        elif con_type == 'imper_act_aor_b' or (con_type in ['imper_act_aor_a', 'imper_act_cont_1', 'imper_act_cont_2c',
                                                            ] and number == 'sg'):
            form = remove_all_diacritics(form)
            form = put_accent_on_the_antepenultimate(form)


        forms[number][person].append(form)

    return forms




def recognize_active_non_past_conjugation(verb, aspect='imperf', tense='fin', voice='active'):
    # can be used for aspects: 'continuous', 'simple', 'simple_passive' 
    # verb is expected to be in 1st person sg, else it's assumed it's modal verb
    
    verb = verb.strip() 
    root = ''
    conjugation_ind = ''
    conjugation_imp = ''
    conjugation_part = ''

    # recognize conjugation

    if verb[-2:] == 'άω' and verb not in ['πάω', 'φάω']:
        root = verb[:-2]
        
        conjugation_ind = 'con2a_act'
        conjugation_imp = 'imper_act_cont_2a'
        conjugation_part = 'present_active_part_2'

    # συνηρημενα
    elif ((verb[-1:] == 'ω' and verb[-2] in ['έ', 'ά', 'ώ']) and (verb[-3:] not in ['δέω', 'ρέω', 'χέω'] and verb[-4:] not in ['πνέω', 'πλέω'])) or (verb[-1] == 'ω' and len(verb) > 2 and verb[-3:-1] in ['αί', 'ού']) or verb == 'πάω':
        root = verb[:-1]
        conjugation_ind = 'con2c_act'
        conjugation_imp = 'imper_act_cont_2c'
        conjugation_part = 'present_active_part_2c'
    elif (verb[-1] == 'ώ') or (verb[-1:] == 'ω' and count_syllables(verb) == 1):
        root = verb[:-1]
       
        conjugation_ind = 'con2b_act'
        conjugation_imp = 'imper_act_cont_2b'
        conjugation_part = 'present_active_part_2'
        # contracted άω to ώ
        if verb[:-1] + 'είς' not in greek_corpus and verb[:-1] + 'ά' in greek_corpus or (
                verb[:-1] + 'άς' in greek_corpus and
                verb[:-1] + 'άτε' in greek_corpus
        ):
            conjugation_ind = 'con2a_act'
            conjugation_imp = 'imper_act_cont_2a'
            conjugation_part = 'present_active_part_2'

        elif verb[:-1] + 'ει' not in greek_corpus and verb[:-1] + 'α' in greek_corpus and count_syllables(verb) == 1:
            conjugation_ind = 'con2a_act'
            conjugation_imp = 'imper_act_cont_2a'
            conjugation_part = 'present_active_part_2'

        elif verb[:-1] + 'είς' not in greek_corpus and verb[:-1] + 'οί' in greek_corpus:

            conjugation_ind = 'con2d_act'
            conjugation_imp = 'imper_act_cont_2d'
            conjugation_part = 'present_active_part_2'

    elif verb[-1:] == 'ω':

        root = verb[:-1]
        conjugation_ind = 'con1_act'
        conjugation_imp = 'imper_act_cont_1'
        conjugation_part = 'present_active_part_1'

    elif verb == 'είμαι':
        root = ''
        conjugation_ind = 'eimai'
        conjugation_imp = 'imper_act_eimai'
        conjugation_part = 'present_active_eimai'

    elif verb == '':
        # sometimes there is no simple future form
        print('no simple conjunctive')
        pass

    elif verb[-2:] in ['ει', 'εί']:
        root = verb[:-2]
        conjugation_ind = 'con1_act_modal'
        if verb[-2:] == 'εί':
            conjugation_ind = 'con2_act_modal'

    else:
        # else it's assumed it's modal
        return {'aspect': aspect, 'tense': tense, 'voice': voice, 'root': verb,
                'conjugation_ind': 'modal', 'conjugation_imp': '', 'conjugation_part': ''}

    if aspect == 'perf':
        # con_ind already recognized
        conjugation_part: ''

        conjugation_imp = 'imper_act_aor_a'

        if count_syllables(verb) == 1:
            conjugation_imp = 'imper_act_aor_c'
        elif root == '':
            # sometimes there is no simple future form
            pass

        elif (root[-1] not in ['σ', 'ρ', 'λ'] or root in ['πέσ']) and verb != 'φάω':
            conjugation_imp = 'imper_act_aor_b'
            # anebainw
            if conjugation_ind == 'con2b_act' and put_accent_on_the_penultimate(root + 'α') in greek_corpus:
                conjugation_imp = 'imper_act_aor_ca'

        
    if aspect == 'perf' and voice == 'passive':
        # for future passive participle logic is implemented separately
        conjugation_part = ''

        conjugation_imp = 'imper_pass_aor_a'

    return {'aspect': aspect, 'voice': voice, 'tense': tense,
                    'root': root,
                    'conjugation_ind': conjugation_ind,
                    'conjugation_imp': conjugation_imp,
                    'conjugation_part': conjugation_part}

def recognize_aorist_conjugation(aorist):
    """
    returns 2 roots, one augmented and one not,
    and conjugation (there are more than one, as we take into consideration
    also rare ancient types)
    """


def recognize_passive_present_continuous_conjugation(verb):

    verb = verb.strip()

    if len(verb) < 6:
        # maybe unnecessary, but one more way to catch problematic input
        print(verb + ' doesnt seem to be a correct verb form')
        raise ValueError

    elif verb[-4:] == 'ομαι':
        root = verb[:-4]
        conjugation_ind = 'con1_pass'
        conjugation_imp = 'imper_pass_cont_1'
        conjugation_part = 'present_passive_part_1'
    
    elif verb[-5:] == "ιέμαι":
        root = verb[:-5]
        conjugation_ind = 'con2a_pass'
        conjugation_imp = 'imper_pass_cont_2a'
        conjugation_part = 'present_passive_part_2a'
    
    elif verb[-5:] == 'ούμαι':
        root = verb[:-5]
        conjugation_ind = 'con2b_pass'
        conjugation_imp = 'imper_pass_cont_2b'
        conjugation_part = 'present_passive_part_2b'

    elif verb[-4:] == 'άμαι':
        root = verb[:-4]
        conjugation_ind = 'con2c_pass'
        conjugation_imp = 'imper_pass_cont_2c'
        conjugation_part = 'present_passive_part_2b'

    elif verb[-4:] == 'ώμαι':
        root = verb[:-4]
        conjugation_ind = 'con2ab_pass'
        conjugation_imp = 'imper_pass_cont_2c'
        conjugation_part = 'present_passive_part_2ab'

    elif verb[-4:] in ['εμαι', 'υμαι'] or verb[-5:] == 'είμαι':
        root = verb[:-3]
        conjugation_ind = 'con2d_pass'
        conjugation_imp = 'imper_pass_cont_2d'
        conjugation_part = 'present_passive_part_2d'

    elif verb[-4:] == 'αμαι':
        root = verb[:-4]
        conjugation_ind = 'con2e_pass'
        conjugation_imp = 'imper_pass_cont_2e'
        conjugation_part = 'present_passive_part_2e'

    elif verb[-4:] in ['εται', 'άται', 'υται'] or verb[-5:] in ['είται', 'ειται', 'ιέται']:
        root = verb[:-4]
        if verb[-5:] in ['είται', 'ειται', 'ιέται']:
            root = verb[:-5]
        conjugation_ind = 'con1_pass_modal'
        conjugation_imp = ''
        conjugation_part = ''

    elif verb[-5:] in ['είται', 'ειται', 'ιέται'] or verb[-4:] in ['άται', 'υται']:
        root = verb[:-5]
        if verb[-4:] in ['άται', 'εται']:
            root = verb[:-4]
        conjugation_ind = 'con2_pass_modal'
        conjugation_imp = ''
        conjugation_part = ''

    else:
        return {'aspect': "imperf", 'voice': 'passive', 'tense': 'fin', 'root': verb,
                'conjugation_ind': 'modal', 'conjugation_imp': '', 'conjugation_part': ''}

    return {'aspect': 'imperf', 'voice': 'passive', 'tense': 'fin', 'root': root,
            'conjugation_ind': conjugation_ind, 'conjugation_imp': conjugation_imp,
            'conjugation_part': conjugation_part}


def recognize_past_conjugation(verb, lemma, aspect='imperf', voice='active'):

    verb = verb.strip()
    root = verb[:-1]

    conjugation_ind = 'aor_act'

    if root[-3:] == 'ούσ':
        conjugation_ind = 'parat2_act'

    elif verb in ['ήμουν', 'ήμουνα']:
        conjugation_ind = 'eimai_paratatikos'

    elif verb[-1] in ['ν', 'η']:
        conjugation_ind = 'arch_pass_aor'

    elif verb[-1] != 'α':
        conjugation_ind = 'modal'
        root = verb


    if voice == 'passive' and aspect == 'imperf':
        root, conjugation_ind = recognize_passive_past_continuous_conjugation(lemma, verb)



    return {'aspect': aspect, 'voice': voice, 'tense': 'past', 'root': root,
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
        conjugation_ind = 'parat2a_pass'
            
    elif len(verb) >= 6 and 'όμουν' in verb[-6:]:
        if verb[-5:] == 'όμουν':
            root = verb[:-5]
        else:
            # if omouna
            root = verb[:-6]
        conjugation_ind = 'parat1_pass'
        # if koimamai

        if lemma[-4:] == 'άμαι':
            conjugation_ind = 'parat2c_pass'
            root = verb[:-5]
        elif lemma[-4:] == 'έμαι':
            conjugation_ind = 'parat2d_pass'
            root = verb[:-5]
    elif len(verb)>=7 and 'ούμουν' in verb[-7:]:
        if verb[-6:] == 'ούμουν':
            root = verb[:-6]
        else:
            # if ούmouna
            root = verb[:-7]
        conjugation_ind = 'parat2b_pass'

    elif len(verb)>=6 and 'ούμην' in verb[-5:]:
        if verb[-5:] == 'ούμην':
            root = verb[:-5]

        conjugation_ind = 'parat2b_pass_logia'

    elif len(verb) >= 5 and 'έμην' in verb[-4:]:

        if verb[-4:] == 'έμην':
            root = verb[:-4]

        conjugation_ind = 'parat2d_pass'
    elif len(verb) >= 5 and 'άμην' in verb[-4:]:

        if verb[-4:] == 'άμην':
            root = verb[:-4]

        conjugation_ind = 'parat2e_pass'

    elif 'ήμουν' in verb:
        root = ''
        conjugation_ind = 'eimai paratatikos'

    else:
        return verb, 'modal'

    if root:
        return root, conjugation_ind
    else:
        print(verb)
        raise AssertionError



if __name__ == '__main__':

    res = recognize_past_conjugation('παριστάμην', 'παρίσταμαι', aspect='imperf', voice='passive')
    print(res)