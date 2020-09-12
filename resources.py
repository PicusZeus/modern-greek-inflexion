poses = {'def_article': 'definite article', 'indef_article': 'indefinite article', 'conj': 'conjunction', 'no_tag': 'not classified',
         'part': 'particle',
         'excl': 'exclamation', 'noun': 'noun', 'prep': 'preposition', 'adv': 'adverb', 'pron': 'pronoun', 'verb': 'verb',
         'quant': 'quantifier', 'properN': 'proper noun', 'adj': 'adjective', 'adv,adj*': "adverb adjective",
         'quant,noun': "quantifier-noun", 'pers_pron': 'personal pronoun',
         'quant,adj': 'quiantifier adjective', 'pron,noun': 'pronoun noun', 'adv,conj': 'adverb conjunctive',
         'adv,adj': 'adverb adjective', 'ind': 'indicative', 'imper': 'imperative', 'nd': 'not defined'


         }

secondary_poses = {

    'inf': 'infinitive', 'imps': 'impersonal',
    'pant': 'adverbial past active participle',
    'pcon': 'adverbial present active participle',
    'prpas': 'present passive participle',
    'praet': 'praeteritum',
    'impt': 'imperative',
    'fin': 'present',
    'pact': 'present active participle',
    'ppas': 'past passive participle',
    'perfpart': 'perfect passive participle',
    'papart': 'past active participle',
    'prespred': 'modal pres',
    'pastpred': 'modal past',
    'comp': 'comparative',
    'superl': 'superlative',
    'adv': 'adverb',
    'comp_adv': 'comparative adverb',
    'superl_adv': 'superlative adverb',
    'ind': 'indicative',
    'imp': 'imperative',
    'part': 'participle',
    'card': 'cardinal quantifiers',
    'nakc': 'weak personal pronoun',
    'akc': 'strong personal pronoun',
    'nd': 'not defined'

}

length_of_endings = {
    "1": [
        "ω",
        "ώ",
        "ά",
        "ς",
        "ν",
        "α",
        "ε"
    ],
    "2": [
        "ει",
        "άω",
        "ας",
        "άν",
        "εί",
        "με",
        "τε",
        "νε",
        "ες",
        "αν",
        "ου"
    ],
    "3": [
        "εις",
        "ετε",
        "ουν",
        "άει",
        "άμε",
        "άτε",
        "άνε",
        "ούν",
        "είς",
        "αμε",
        "ατε",
        "ανε"
    ],
    "4": [
        "ουμε",
        "ουνε",
        "ούμε",
        "ούνε",
        "είτε",
        "ομαι",
        "εσαι",
        "εται",
        "εστε",
        "άμαι",
        "άσαι",
        "άται",
        "άστε",
        "όταν",
        "είτο",
        "είσο"
    ],
    "5": [
        "ονται",
        "ιέμαι",
        "ιέσαι",
        "ιέται",
        "ιέστε",
        "ούμαι",
        "είσαι",
        "είται",
        "είστε",
        "όμουν",
        "όσουν",
        "ότανε",
        "ονταν",
        "ούντο",
        "ούμην",
        "είσθε"
    ],
    "6": [
        "όμαστε",
        "όσαστε",
        "ούμεθα",
        "ούνται",
        "όμουνα",
        "όσουνα",
        "ιόμουν",
        "ιόσουν",
        "ούμουν",
        "ούσουν",
        "ούνταν"
    ],
    "7": [
        "ιόμαστε",
        "ιόσαστε",
        "ιούνται",
        "ούμαστε",
        "όμασταν",
        "όσασταν",
        "ιόμουνα",
        "ιόσουνα",
        "ιούνταν",
        "ούσαστε"
    ],
    "8": [
        "όντουσαν",
        "ιόμασταν",
        "ιόσασταν",
        "ούμασταν",
        "ούσασταν"
    ]
}

pronouns= ['εγώ', 'εσύ', 'αυτός, αυτή, αυτό', 'εμείς', 'εσείς', 'αυτοί, αυτές, αυτά']

conjugations = {
'eimai': {'sg': {'pri': ['είμαι'], 'sec': ['είσαι'], 'ter': ['είναι']}, 'pl': {'pri': ['είμαστε'], 'sec': ['είστε', 'είσαστε'], 'ter': ['είναι']}},
'eimai_paratatikos':  {'sg': {'pri': ['ήμουν', 'ήμουνα'], 'sec': ['ησουν', 'ήσουνα'], 'ter': ['ήταν', 'ήτανε']}, 'pl': {'pri': ['ήμαστε', 'ήμασταν'], 'sec': ['ήσαστε', 'ήσασταν'], 'ter': ['ήταν', 'ήτανε']}},
'con1_act': {'sg': {'pri': ['ω'], 'sec': ['εις'], 'ter': ['ει']}, 'pl': {'pri': ['ουμε'], 'sec': ['ετε'], 'ter': ['ουν', 'ουνε']}}, 
'con2a_act': {'sg': {'pri': ['ώ', 'άω'], 'sec': ['άς'], 'ter': ['ά', 'άει']}, 'pl': {'pri': ['ούμε', 'άμε'], 'sec': ['άτε'], 'ter': ['άνε', 'άν', 'ούν', 'ούνε']}},
'con2b_act': {'sg': {'pri': ['ώ'], 'sec': ['είς'], 'ter': ['εί']}, 'pl': {'pri': ['ούμε'], 'sec': ['είτε'], 'ter': ['ούνε', 'ούν']}}, 
'con2c_act': {'sg': {'pri': ['ω'], 'sec': ['ς'], 'ter': ['ει']}, 'pl': {'pri': ['με'], 'sec': ['τε'], 'ter': ['νε', 'ν']}},
'con2d_act': {'sg': {'pri': ['ώ'], 'sec': ['οίς'], 'ter': ['οί']}, 'pl': {'pri': ['ούμε', 'ούμεν'], 'sec': ['οίτε', 'ούτε'], 'ter': ['ούνε', 'ούν']}},

'con1_pass': {'sg': {'pri': ['ομαι'], 'sec': ['εσαι'], 'ter': ['εται']}, 'pl': {'pri': ['όμαστε'], 'sec': ['εστε', 'όσαστε'], 'ter': ['ονται']}}, 
'con2a_pass': {'sg': {'pri': ['ιέμαι'], 'sec': ['ιέσαι'], 'ter': ['ιέται']}, 'pl': {'pri': ['ιόμαστε', 'ιούμαστε'], 'sec': ['ιέστε', 'ιόσαστε'], 'ter': ['ιούνται', 'ιόνται']}},
'con2ab_pass': {'sg': {'pri': ['ώμαι'], 'sec': ['άσαι'], 'ter': ['άται']}, 'pl': {'pri': ['όμαστε'], 'sec': ['άστε'],
                                                                                  'ter': ['ώνται']}},

'con2b_pass': {'sg': {'pri': ['ούμαι'], 'sec': ['είσαι'], 'ter': ['είται']}, 'pl': {'pri': ['ούμαστε', 'ούμεθα'], 'sec': ['είστε', 'είσθε'], 'ter': ['ούνται']}},
'con2c_pass': {'sg': {'pri': ['άμαι'], 'sec': ['άσαι'], 'ter': ['άται']}, 'pl': {'pri': ['όμαστε'], 'sec': ['άστε', 'όσαστε'], 'ter': ['ούνται']}},
'con2sa_pass': {'sg': {'pri': ['ούμαι'], 'sec': ['ούσαι'], 'ter': ['ούται']}, 'pl': {'pri': ['ούμεθα'], 'sec': ['ούσθε'],
                                                                                 'ter': ['ούνται']}},
'con2d_pass': {'sg': {'pri': ['μαι'], 'sec': ['σαι'], 'ter': ['ται']}, 'pl': {'pri': ['μεθα'], 'sec': ['στε'],
                                                                                 'ter': ['νται']}},
'con2e_pass': {'sg': {'pri': ['αμαι'], 'sec': ['ασαι'], 'ter': ['αται']}, 'pl': {'pri': ['άμεθα', 'όμαστε'],
                                                                                 'sec': ['ασθε', 'άστε'],
                                                                                 'ter': ['ανται']}},

'aor_act': {'sg': {'pri': ['α'], 'sec': ['ες'], 'ter': ['ε']}, 'pl': {'pri': ['αμε'], 'sec': ['ατε'], 'ter': ['αν', 'ανε']}},
'arch_pass_aor' :{'sg': {'pri': ['ην'], 'sec': ['ης'], 'ter': ['η']}, 'pl': {'pri': ['ημεν'], 'sec': ['ητε'], 'ter': ['ησαν']}},
'parat2_act': {'sg': {'pri': ['α'], 'sec': ['ες'], 'ter': ['ε']}, 'pl': {'pri': ['αμε'], 'sec': ['ατε'], 'ter': ['αν', 'ανε']}}, 
'parat1_pass': {'sg': {'pri': ['όμουν', 'όμουνα'], 'sec': ['όσουν', 'όσουνα'], 'ter': ['όταν', 'ότανε']}, 'pl': {'pri': ['όμασταν', 'όμαστε'], 'sec': ['όσασταν', 'όσαστε'], 'ter': ['ονταν', 'όντουσαν']}}, 
'parat2a_pass': {'sg': {'pri': ['ιόμουν', 'ιόμουνα'], 'sec': ['ιόσουν', 'ιόσουνα'], 'ter': ['ιόταν', 'ιότανε']}, 'pl': {'pri': ['ιόμασταν', 'ιόμαστε'], 'sec': ['ιόσασταν', 'ιόσαστε'], 'ter': ['ιούνταν', 'ιόντουσαν']}},
'parat2b_pass': {'sg': {'pri': ['ούμουν'], 'sec': ['ούσουν'], 'ter': ['είτο', 'ούνταν', 'ούντανε']}, 'pl': {'pri': ['ούμασταν', 'ούμαστε'], 'sec': ['ούσασταν', 'ούσαστε'], 'ter': ['ούνταν', 'ούντο', 'ούντανε']}},
'parat2b_pass_logia' : {'sg': {'pri': ['ούμην'], 'sec': ['είσο'], 'ter': ['είτο']}, 'pl': {'pri': ['ούμεθα'], 'sec': ['είσθε'], 'ter': ['ούντο']}},
'parat2c_pass': {'sg': {'pri': ['όμουν', 'όμουνα'], 'sec': ['όσουν', 'όσουνα'], 'ter': ['όταν', 'ότανε']}, 'pl': {'pri': ['όμασταν', 'όμαστε'], 'sec': ['όσασταν', 'όσαστε'], 'ter': ['ούνταν', 'όντουσαν']}},  
'parat2d_pass': {'sg': {'pri': ['όμουν', 'έμην'], 'sec': ['όσουν', 'εσο'], 'ter': ['όταν', 'ετο']},
                 'pl': {'pri': ['όμασταν', 'έμεθα'], 'sec': ['όσασταν', 'εσθε'], 'ter': ['ούνταν', 'εντο']}},
'parat2e_pass': {'sg': {'pri': ['άμην'], 'sec': ['ασο'], 'ter': ['ατο']}, 'pl': {'pri': ['άμεθα', 'όμαστε', 'όμασταν'],
                                                                                 'sec': ['ασθε', 'άστε', 'όσασταν',
                                                                                         'όσαστε'],
                                                                                 'ter': ['αντο']}},

'imper_act_cont_1': {'sg': {'sec': ['ε']}, 'pl':{ 'sec':['ετε'] }},
'imper_act_eimai': {'sg': {'sec': ['να είσαι']}, 'pl':{ 'sec':['να είστε'] }}, 
'imper_act_cont_2a': {'sg': {'sec': ['α', 'αγε']}, 'pl':{ 'sec':['άτε'] }},
'imper_act_cont_2b': {'sg': {'sec': ['ει']}, 'pl':{ 'sec':['είτε'] }},
'imper_act_cont_2d': {'sg': {'sec': ['ου']}, 'pl': {'sec':['ούτε', 'οίτε']}},
'imper_act_cont_2c': {'sg': {'sec': ['γε']}, 'pl':{ 'sec':['γετε', 'τε']}},
'imper_pass_cont_2d': {'sg': {'sec': ['σο']}, 'pl': {'sec': ['σθε']}},
'imper_pass_cont_2e': {'sg': {'sec': ['σο']}, 'pl': {'sec': ['σθε']}},
'imper_pass_cont_1': {'pl':{ 'sec': ['εστε']}},
'imper_pass_cont_2a': {'pl':{ 'sec': ['ιέστε']}},
'imper_pass_cont_2b': {'pl':{ 'sec': ['είστε']}},
'imper_pass_cont_2c': {'pl':{ 'sec': ['άστε']}},

'imper_act_aor_a': {'sg': {'sec': ['ε']}, 'pl': {'sec':['τε']}},
'imper_act_aor_b': {'sg': {'sec': ['ε']}, 'pl': { 'sec':['ετε'] }},
'imper_act_aor_c': {'sg': {'sec': ['ες']}, 'pl': {'sec':['έστε', 'είτε']}},
'imper_act_aor_ca':{'sg': {'sec': ['α']}, 'pl': {'sec':['είτε']}},
'imper_pass_aor_a': {'sg': {'sec': ['ου']}, 'pl':{ 'sec':['είτε']}},
'imper_pass_aor_b': { 'pl':{ 'sec':['είτε']} },
'present_active_part_1': {'nd': {'nd': ['οντας']}},
'present_active_eimai': {'nd': {'nd': ['όντας']}},
'present_active_part_2c': {'nd': {'nd': ['γοντας']}},
'present_active_part_2': {'nd': {'nd': ['ώντας']}},
'present_passive_part_1': {'sg': {'nd': ['όμενος']}},
'present_passive_part_2a': {'sg': {'nd': ['ώμενος']}},
'present_passive_part_2ab': {'sg': {'nd': ['ώμενος']}},
'present_passive_part_2b': {'sg': {'nd': ['ούμενος']}},
'present_passive_part_2d': {'sg': {'nd': ['έμενος']}},
'present_passive_part_2e': {'sg': {'nd': ['μενος']}},
'past_passive_part': {'sg': {'nd': ['μένος']}},
'modal': None
}

common_tenses = {'fin': 'present', 'past': 'past', 'fut': 'future', 'nd': 'not defined'}

# maps tenses with other data
greek_tenses = {
    'present': ['fin', 'imperf'],
    'continuous subjunctive': ['fin', 'imperf', 'να '],
    'continuous hortative': ['fin', 'imperf', 'ας '],
    'future continuous': ['fin', 'imperf', 'θα '],
    'continuous imperative': ['impt', 'imperf'],
    'simple subjunctive': ['fin', 'perf', 'να '],
    'simple future': ['fin', 'perf', 'θα '],
    'simple imperative': ['impt', 'perf'],
    'aorist': ['praet', 'perf'],
    'paratatikos': ['praet', 'imperf'],
    'perfect': ['aux_fin', 'perf'],
    'future perfect': ['aux_fin', 'perf', 'θα '],
    'past perfect': ['aux_praet', 'perf'],
    'dinitiki': ['praet', 'imperf', 'θα '],
    'optative_2': ['praet', 'imperf', 'να '],
    'first conditional': ['fin', 'perf', 'αν '],
    'second conditional': ['praet', 'imperf', 'αν '],
    'third conditional': ['aux_praet', 'perf', 'αν ']

}

cases = {'voc': 'vocative', 'gen': 'genitive', 'acc': 'accusative', 'nom': 'nominative', 'dat': 'dative', 'nd': 'not defined'}

persons = {'pri', 'sec', 'ter', 'impersonal', 'nd'}

genders = {'fem': 'feminine', 'masc': 'masculine', 'neut': 'neutral', 'nd': 'not defined'}
# will have to add some other genders specific to Polish language
numbers = {'sg', 'pl', 'dual', 'nd'}

aspects = {'imperf', 'perf', 'nd'}

voices = {'passive', 'active', 'middle', 'deponens', 'nd'}

declinations = {
    'masc_os': {'sg': {'nom': 'ος', 'acc': 'ο', 'gen': 'ου', 'voc': 'ε' }, 'pl': {'nom': 'οι', 'acc': 'ους', 'gen': 'ων', 'voc': 'οι' }},
    'feminine_h':{'sg': {'nom': 'η', 'acc': 'η', 'gen': 'ης', 'voc': 'η' }, 'pl': {'nom': 'ες', 'acc': 'ες', 'gen': 'ων', 'voc': 'ες' }}, 
    'feminine_a':{'sg': {'nom': 'α', 'acc': 'α', 'gen': 'ας', 'voc': 'α' }, 'pl': {'nom': 'ες', 'acc': 'ες', 'gen': 'ων', 'voc': 'ες' }}, 
    'neuter_o':{'sg': {'nom': 'ο', 'acc': 'ο', 'gen': 'ου', 'voc': 'ο' }, 'pl': {'nom': 'α', 'acc': 'α', 'gen': 'ων', 'voc': 'α' }}
}


# these prefixes change themselves or stem by esoteric augmentation
# I probably should change this model into key - augmented prefix, value - anaugmented, because for one augmented there are sometimes more than one unaugmented forms (para: pare, or parh)
dict_of_augmented_prefixes = {'ανα': 'ανε', 'δια': 'διε', 'εκ': 'εξε', 'συλ': 'συνε', 'απο': 'απε', 'προ': 'προε', 'κατευ': 'κατηυ', 'παρα': 'παρε', 'προεξ': 'προεξε', 'ενδια': 'ενδιε', 'περι': 'περιε', 'υπο': 'υπε', 'αμφι': 'αμφε', 'επι': 'επε', 'κατα':'κατε', 'εισ': 'εισε'}



# these prefixes do not merge with verbs at all
prefixes_list_that_allow_augmentaion = ['πολυ', 'παρα', 'καλα', 'κουτσα']

nd = 'nd'
fem = 'fem'
masc = 'masc'
neut = 'neut'

nom = 'nom'
gen = 'gen'
acc = 'acc'
voc = 'voc'

EGO_STRONG = {
    nd: {
    'sg': {
        nom: 'εγώ',
        gen: 'εμένα',
        acc: 'εμένα,μένα',
    },
    'pl': {
        nom: 'εμείς',
        gen: 'εμάς,ημών',
        acc: 'εμάς,μας',
    }
    }
}

EGO_WEAK = {
    nd: {
    'sg': {
        nom: '',
        gen: 'μου',
        acc: 'με',
    },
    'pl': {
        nom: '',
        gen: 'μας',
        acc: 'μας',
    }
    }

}

ESU_STRONG = {
    nd: {
    'sg': {
        nom: 'εσύ',
        gen: 'εσένα',
        acc: 'εσένα,σένα',
    },
    'pl': {
        nom: 'εσείς',
        gen: 'εσάς,υμών',
        acc: 'εσάς',
    }
    }
}

ESU_WEAK = {
    nd: {
    'sg': {
        nom: '',
        gen: 'σου',
        acc: 'σε',
    },
    'pl': {
        nom: '',
        gen: 'σας',
        acc: 'σας',
    }
    }
}

AUTOS_STRONG = {
    masc: {
        'sg': {
            nom: 'αυτός',
            gen: 'αυτού',
            acc: 'αυτόν,αυτό',
        },
        'pl': {
            nom: 'αυτοί',
            gen: 'αυτών',
            acc: 'αυτούς',
        }
    },
    fem: {
        'sg': {
            nom: 'αυτή',
            gen: 'αυτής',
            acc: 'αυτήν,αυτή',
        },
        'pl': {
            nom: 'αυτές',
            gen: 'αυτών',
            acc: 'αυτές,αυτάς',
        }
    },
    neut: {
        'sg': {
            nom: 'αυτό',
            gen: 'αυτού',
            acc: 'αυτό',
        },
        'pl': {
            nom: 'αυτά',
            gen: 'αυτών',
            acc: 'αυτά',
        }
    }

}

AUTOS_WEAK = {
    masc: {
        'sg': {
            nom: 'τος',
            gen: 'του',
            acc: 'τον',
        },
        'pl': {
            nom: 'τοι',
            gen: 'τους',
            acc: 'τους',
        }
    },
    fem: {
        'sg': {
            nom: 'τη',
            gen: 'της',
            acc: 'την,τη',
        },
        'pl': {
            nom: 'τες',
            gen: 'τους',
            acc: 'τις,τες',
        }
    },
    neut: {
        'sg': {
            nom: 'το',
            gen: 'του',
            acc: 'το',
        },
        'pl': {
            nom: 'τα',
            gen: 'τους',
            acc: 'τα',
        }
    }
}


TIS = {
    masc: {
        'sg': {
            nom: 'τις',
            gen: 'τίνος',
            acc: 'τίνα',
        },
        'pl': {
            nom: 'τίνες',
            gen: 'τίνων',
            acc: 'τίνας',
        }
    },
    fem: {
        'sg': {
            nom: 'τις',
            gen: 'τίνος',
            acc: 'τίνα',
        },
        'pl': {
            nom: 'τίνες',
            gen: 'τίνων',
            acc: 'τίνας',
        }
    },
    neut: {
        'sg': {
            nom: 'τι',
            gen: 'τίνος',
            acc: 'τι',
        },
        'pl': {
            nom: 'τίνα',
            gen: 'τίνων',
            acc: 'τίνα',
        }
    }
}

a = [

    ['εγώ', ['εγώ', 'ppron12:sg:nom:m.f.n:pri:akc']],
    ['μου', ['εγώ', 'ppron12:sg:gen:m.f.n:pri:nakc:npraep']],
    ['εμένα', ['εγώ', 'ppron12:sg:gen.acc:m.f.n:pri:akc:npraep']],
    ['μένα', ['εγώ', 'ppron12:sg:acc:m.f.n:pri:akc:praep']],
    ['με', ['εγώ', 'ppron12:sg:acc:m.f.n:pri:nakc:npraep']],
    ['εμείς', ['εμείς', 'ppron12:pl:nom:m.f.n:pri:akc']],
    ['εμάς', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:akc:npraep']],
    ['μας', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:akc:praep']],
    ['μας', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:nakc:npraep']],

    ['εσύ', ['εσύ', 'ppron12:sg:nom:m.f.n:sec:akc']],
    ['σου', ['εσύ', 'ppron12:sg:gen:m.f.n:sec:nakc:npraep']],
    ['εσένα', ['εσύ', 'ppron12:sg:gen.acc:m.f.n:sec:akc:npraep']],
    ['σένα', ['εσύ', 'ppron12:sg:acc:m.f.n:sec:akc:praep']],
    ['σε', ['εσύ', 'ppron12:sg:acc:m.f.n:sec:nakc:npraep']],

    ['εσείς', ['εσείς', 'ppron12:pl:nom:m.f.n:sec:akc']],
    ['εσάς', ['εσείς', 'ppron12:pl:gen.acc:m.f.n:sec:akc:npraep']],

    ['σας', ['εσείς', 'ppron12:pl:acc:m.f.n:sec:akc:praep']],

    ['σας', ['εσείς', 'ppron12:pl:gen.acc:m.f.n:sec:nakc:npraep']],

    # nom
    ['αυτός', ['αυτός', 'ppron3:sg:nom:m:ter:akc']],
    ['τoς', ['αυτός', 'ppron3:sg:nom:m:ter:nakc']],
    ['το', ['αυτός', 'ppron3:sg:nom.acc:n:ter:akc.nakc:npraep']],
    ['αυτό', ['αυτός', 'ppron3:sg:nom.acc:n:ter:akc.akc']],
    ['αυτή', ['αυτός', 'ppron3:sg:nom.acc:f:ter:akc']],
    ['τή', ['αυτός', 'ppron3:sg:nom.acc:f:ter:nakc']],
    # gen
    ['αυτού', ['αυτός', 'ppron3:pl:gen:n.m:ter:akc:praep:npraep']],
    ['του', ['αυτός', 'ppron3:sg:gen:n.m:ter:nakc:npraep']],

    ['αυτής', ['αυτός', 'ppron3:sg:gen:f:ter:akc']],
    ['της', ['αυτός', 'ppron3:sg:gen:f:ter:nakc:npraep']],
    # acc
    ['αυτόν', ['αυτός', 'ppron3:sg:acc:m:ter:akc:npraep:praep']],
    ['αυτήν', ['αυτός', 'ppron3:sg:acc:f:ter:akc']],
    ['τήν', ['αυτός', 'ppron3:sg:acc:f:ter:nakc:npraep']],
    ['τον', ['αυτός', 'ppron3:sg:gen:n:ter:nakc:npraep']],

    # nom
    ['αυτοί', ['αυτός', 'ppron3:pl:nom:m:ter:akc']],
    ['αυτές', ['αυτός', 'ppron3:pl:nom.acc:f:ter:akc']],
    ['τοι', ['αυτός', 'ppron3:pl:nom:m:ter:nakc']],
    ['τες', ['αυτός', 'ppron3:pl:nom:f:ter:nakc']],
    ['τα', ['αυτός', 'ppron3:pl:nom.acc:n:ter:nakc:npraep']],
    ['αυτά', ['αυτός', 'ppron3:pl:nom.acc:n:ter:akc.akc']],

    # gen
    ['αυτών', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:akc']],
    ['τους', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:nakc:npraep']],

    # acc
    ['τους', ['αυτός', 'ppron3:pl:acc:m:ter:nakc:npraep']],
    ['αυτούς', ['αυτός', 'ppron3:pl:acc:m:ter:akc']],
    ['τις', ['αυτός', 'ppron3:pl:acc:f:ter:akc.nakc:npraep']],
    ['τες', ['αυτός', 'ppron3:pl:acc:f:ter:akc.nakc:npraep']],

]

feminine_h_eis = ('γύρη', 'κύστη', 'παλισάνδρη', 'πίστη', 'τίγρη', 'πόλη')

feminine_os = ('άμμος', 'οδός', 'διάλεκτος', 'είσοδος', 'έξοδος', 'κάθοδος', 'λεωφόρος',
               'νήσος', 'παράγραφος', 'πρόοδος', 'περίοδος', 'χερσόνησος', 'ψήφος',
               'αεροσυνοδός', 'ακταιωρός', 'ατραπός', 'δοκός', 'επωδός', 'βάλανος', 'θαλαμηγός', 'σποδός', 'λίθος',
               'άβυσσος', 'Aειπάρθενος', 'άκανθος', 'άκατος', 'άλυσος', 'άμπελος', 'άνοδος', 'κιβωτός', 'στενωπός',
               'κόπρος', 'ασβεστοκάμινος', 'άσβεστος', 'άσφαλτος', 'ατμάκατος', 'άτρακτος', 'σιδηροδοκός', 'τροφός',
               'φηγός', 'άμμος', 'άρκτος', 'βάτος', 'Bίβλος', 'βίβλος', 'κανηφόρος', 'κανονιοφόρος', 'νηπιαγωγός',
               'βρεφοδόχος', 'γνάθος', 'δέλτος', 'δρόσος', 'ζωοφόρος', 'ζωφόρος', 'Θεοτόκος', 'πλίνθος', 'Ρόδος',
               'σορός', 'λέμβος', 'λαιμητόμος', 'λέμφος', 'λουτροφόρος', 'νηπιοκόμος', 'νήσος', 'νόσος', 'παρθένος',
               'ράβδος', 'σαρκοφάγος', 'σκευοφόρος', 'τεφροδόχος', 'τριτοτόκος', 'χοηφόρος', 'ψάμμος', 'ψηφοδόχος',
               'ψήφος', 'βάρβιτος', 'βάσανος', 'βενζινάκατος', 'Διακαινήσιμος', 'διάκεντρος', 'διάλεκτος', 'διάμεσος',
               'διάμετρος', 'διέξοδος', 'δικάσιμος', 'δίοδος', 'δωδεκάδελτος', 'εγκύκλιος', 'είσοδος', 'έλαφος', 'έξοδος',
               'επάνοδος', 'επέτειος', 'έρημος', 'έφοδος', 'ημισέληνος', 'ιερόδουλος', 'κάθετος', 'κάθοδος', 'κάμηλος',
               'κυπάρισσος', 'ημιδιάμετρος', 'ημιπερίοδος', 'ήπειρος', 'ίνδικτος', 'κάμινος', 'κέραμος', 'κλιμακτήριος',
               'λέκιθος', 'λήκυθος', 'μεγαλόνησος', 'μέθοδος', 'μεθόριος', 'μεσόφωνος', 'οκτώηχος', 'οπτόπλινθος',
               'Παμμακάριστος', 'Πανάχραντος', 'πανσέληνος', 'παράγραφος', 'παράγωγος', 'παρακαμπτήριος', 'παράμετρος',
               'πάροδος', 'Πεντάτευχος', 'πεντηκόντορος', 'περίμετρος', 'περίοδος', 'περίπολος', 'πισσάσφαλτος',
               'προβατοκάμηλος', 'πρόοδος', 'πρόσοδος', 'πύελος', 'πυραυλάκατος', 'σεληνάκατος', 'σταφιδάμπελος',
               'στρουθοκάμηλος', 'σύγκλητος', 'σύνοδος', 'τήβεννος', 'τορπιλάκατος', 'ύαλος', 'ύπαιθρος', 'υπερλεωφόρος',
               'υφήλιος', 'υψικάμινος', 'χερσόνησος', 'ωμόπλινθος')


feminine_or_masc = ('καπνοδόχος', 'άργιλος', 'τάφρος', 'κρύσταλλος', 'περιβαλλοντολόγος', 'απόστροφος', 'γιατρός',
                    'μηχανικός', 'ηθοποιός', 'νηπιαγογός', 'δικιγόρος',)

# should there be added language names on ika?
plur_tant_neut = ('Χριστούγεννα', 'χριστούγεννα', 'νιάτα', 'βαλκάνια', 'Ιωάννινα', 'Γιάννενα', 'Γιάννινα')